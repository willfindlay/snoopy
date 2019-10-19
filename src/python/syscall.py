# Syscall parsing adapted from https://github.com/nelhage/ministrace by @nelhage

import os, sys
import re
import subprocess

from bcc.syscall import syscalls as bcc_syscalls

# Argument type functions below this line ----------------

def unknown_arg(v):
    return "UNKNOWN_ARG"

def str_arg(v):
    return f"\"{str(v)}\""

def int_arg(v):
    try:
        return f"{int(v)}"
    except:
        return unknown_arg(v)

def hex_arg(v):
    try:
        return f"{hex(v)}"
    except:
        return unknown_arg(v)

def argument_type(t):
arguments = {'ARG_UNKNOWN': unknown_arg,
        'ARG_PTR': hex_arg,
        'ARG_INT': int_arg,
        'ARG_STR': str_arg}
    return arguments.get(t.lower(), d='unk')

# Parsing stuff below this line -------------------------

def parse_numbers(unistd_h):
    numbers = {}

    return numbers

def parse_args(linux):
    args = {}

    find = subprocess.Popen(["find"] +
            [os.path.join(linux, d) for d in
                "arch/x86 fs include ipc kernel mm net security".split()] +
            ["-name", "*.c", "-print"],
            stdout = subprocess.PIPE)

    for f in find.stdout:
        pass

    return args

def parse_type(t):
    if re.search(r'^(const\s*)?char\s*(__user\s*)?\*\s*$', t):
        return argument_type('ARG_STR')
    if t.endswith('*'):
        return argument_type('ARG_PTR')
    return argument_type('ARG_INT')

def parse_syscalls(unistd_h, linux):
    syscalls = {}

    return syscalls

class Syscall:
    def __init__(self, num, name, types):
        self.name = syscall_name(num)
        self.num = num
        self.arg_types = []
        self.args = []

syscalls = parse_syscalls()
