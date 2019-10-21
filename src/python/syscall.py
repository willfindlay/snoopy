# Syscall parsing adapted from https://github.com/nelhage/ministrace by @nelhage

import os, sys
import re
import subprocess
import _pickle as pickle
import logging
from collections import defaultdict

from bcc.syscall import syscalls as bcc_syscalls

from .config import Config
from .utils import create_parent_dirs

log = logging.getLogger()

# Parsing stuff below this line -------------------------

def parse_names(unistd_h):
    syscalls = defaultdict(lambda: "UNKNOWN")

    for line in open(unistd_h):
        m = re.search(r'^#define\s*__NR_(\w+)\s*(\d+)', line)
        if m:
            (name, number) = m.groups()
            number = int(number)
            syscalls[number] = name

    return syscalls

def parse_args(linux):
    syscalls = defaultdict(lambda: ["ARG_UNKNOWN" for _ in range(6)])

    find = subprocess.Popen(["find"] +
            list(filter(os.path.exists, [os.path.join(linux, d) for d in
                "arch/x86 fs include ipc kernel mm net security block char".split()])) +
            ["-name", "*.c", "-print"],
            stdout = subprocess.PIPE)

    for f in find.stdout:
        f = f.decode('utf-8').strip()
        with open(f, 'r') as header:
            in_syscall = False
            text = ''
            for line in header:
                line = line.strip()
                if not in_syscall and 'SYSCALL_DEFINE' in line:
                    text = ''
                    in_syscall = True
                if in_syscall:
                    text += line
                    if line.endswith(')'):
                        in_syscall = False
                        parse_define(syscalls, text)
                    else:
                        text += ' '

    return syscalls

def parse_define(syscalls, text):
    (name, types) = None, None
    if text.startswith('SYSCALL_DEFINE('):
        m = re.search(r'^SYSCALL_DEFINE\(([^)]+)\)\(([^)]+)\)$', text)
        if not m:
            return
        name, args = m.groups()
        types = [s.strip().rsplit(" ", 1)[0] for s in args.split(",")]
    else:
        m = re.search(r'SYSCALL_DEFINE(\d)\(([^,]+)\s*(?:,\s*([^)]+))?\)$', text)
        if not m:
            return
        nargs, name, argstr = m.groups()
        if argstr is not None:
            argspec = [s.strip() for s in argstr.split(",")]
            types = argspec[0:len(argspec):2]
        else:
            types = []
    types = [parse_type(t) for t in types]
    syscalls[name] = types

def parse_type(t):
    if re.search(r'^(const\s*)?char\s*(__user\s*)?\*\s*$', t):
        return 'ARG_STR'
    if t.endswith('*'):
        return 'ARG_PTR'
    return 'ARG_INT'

def parse_syscalls(unistd_h, linux):
    syscalls = {}
    log.info(f"Parsing syscalls from {unistd_h} and {linux}")
    names_dict = parse_names(unistd_h)
    args_dict = parse_args(linux)

    for sys_num in sorted(names_dict.keys()):
        name = names_dict[sys_num]
        syscalls[sys_num] = SyscallDefinition(sys_num,
                names_dict[sys_num],
                args_dict[names_dict[sys_num]])

    return syscalls

class SyscallDefinition:
    def __init__(self, num, name, types):
        self.name = name
        self.num = num
        self.arg_types = types

    def template(self, *args):
        pargs = []
        for t, arg in zip(self.arg_types, args):
            if t == 'ARG_PTR':
                pargs.append(str(hex(arg)))
            elif t == 'ARG_STR':
                pargs.append(f"\"{arg}\"")
            elif t == 'ARG_INT':
                pargs.append(str(arg))
            elif t == 'ARG_UNKNOWN':
                pargs.append(t)
        return f"{self.name}({', '.join(pargs)})"

    def __repr__(self):
        return f"{self.name}({', '.join(self.arg_types)})"

# Write syscalls to cache
def write_to_cache(syscalls_32, syscalls_64):
    # Create cache dirs for syscalls
    create_parent_dirs(Config.syscalls_32_cache)
    create_parent_dirs(Config.syscalls_64_cache)

    with open(Config.syscalls_32_cache, 'wb') as f:
        f.write(pickle.dumps(syscalls_32))

    with open(Config.syscalls_64_cache, 'wb') as f:
        f.write(pickle.dumps(syscalls_64))

# Call this in main before importing snoopy
def init_syscalls(should_update=False):
    log.debug("Initializing syscalls")
    linux_dir = Config.linux_dir
    unistd_32 = Config.unistd_32
    unistd_64 = Config.unistd_64
    global syscalls_32
    global syscalls_64

    should_cache = False

    syscalls_32 = None
    syscalls_64 = None

    # Attempt to open cached version
    if not should_update:
        try:
            with open(Config.syscalls_32_cache, 'rb') as f:
                syscalls_32 = pickle.load(f)
                log.info("Using cached version of syscalls_32")
        except FileNotFoundError:
            log.debug("Could not find cached version of syscalls_32")
        try:
            with open(Config.syscalls_64_cache, 'rb') as f:
                syscalls_64 = pickle.load(f)
                log.info("Using cached version of syscalls_64")
        except FileNotFoundError:
            log.debug("Could not find cached version of syscalls_64")

    # Parse syscalls from the kernel source
    if not syscalls_32 or should_update:
        syscalls_32 = parse_syscalls(unistd_32, linux_dir)
        should_cache = True
    if not syscalls_64 or should_update:
        syscalls_64 = parse_syscalls(unistd_64, linux_dir)
        should_cache = True

    # Cache the syscalls
    if should_cache:
        log.info("Writing to syscall cache")
        write_to_cache(syscalls_32, syscalls_64)
