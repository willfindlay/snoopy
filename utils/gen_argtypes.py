#!/usr/bin/env python3
# modified from https://github.com/nelhage/ministrace by @nelhage

import os
import sys
import re
import subprocess

def do_syscall_numbers(unistd_h):
  syscalls = {}
  for line in open(unistd_h):
    m = re.search(r'^#define\s*__NR_(\w+)\s*(\d+)', line)
    if m:
      (name, number) = m.groups()
      number = int(number)
      syscalls[number] = name

  return syscalls

def process_define(syscalls, text):
  (name, types) = None, None
  if text.startswith('SYSCALL_DEFINE('):
    m = re.search(r'^SYSCALL_DEFINE\(([^)]+)\)\(([^)]+)\)$', text)
    if not m:
      print("Unable to parse:", text)
      return
    name, args = m.groups()
    types = [s.strip().rsplit(" ", 1)[0] for s in args.split(",")]
  else:
    m = re.search(r'SYSCALL_DEFINE(\d)\(([^,]+)\s*(?:,\s*([^)]+))?\)$', text)
    if not m:
      print("Unable to parse:", text)
      return
    nargs, name, argstr = m.groups()
    if argstr is not None:
      argspec = [s.strip() for s in argstr.split(",")]
      types = argspec[0:len(argspec):2]
    else:
      types = []
  syscalls[name] = types

def find_args(linux):
  syscalls = {}
  find = subprocess.Popen(["find"] +
               [os.path.join(linux, d) for d in
                "arch/x86 fs include ipc kernel mm net security".split()] +
              ["-name", "*.c", "-print"],
              stdout = subprocess.PIPE)
  for f in find.stdout:
    fh = open(f.strip())
    in_syscall = False
    text = ''
    for line in fh:
      line = line.strip()
      if not in_syscall and 'SYSCALL_DEFINE' in line:
        text = ''
        in_syscall = True
      if in_syscall:
        text += line
        if line.endswith(')'):
          in_syscall = False
          process_define(syscalls, text)
        else:
          text += " "
  return syscalls

def parse_type(t):
  print(t)
  if re.search(r'^(const\s*)?char\s*(__user\s*)?\*\s*$', t):
    return "ARG_STR"
  if t.endswith('*'):
    return "ARG_PTR"
  return "ARG_INT"

def write_output(syscalls_h, types, numbers):
  out = open(syscalls_h, 'w')

  print("MAX_SYSCALL_NUM = %d" % (max(numbers.keys()),), file=out)
  print("SYSCALLS = [", file=out)
  #for num in sorted(numbers.keys()):
  for num in range(max(numbers.keys())):
    if num not in numbers:
      print(' ( "UNKNOWN_'+str(num)+'", 6, [ARG_UNKNOWN,ARG_UNKNOWN,ARG_UNKNOWN,ARG_UNKNOWN,ARG_UNKNOWN,ARG_UNKNOWN]),', file=out)
      continue
    name = numbers[num]
    if name in types:
      args = types[name]
    else:
      args = ["void*"] * 6

    print("     (   # %d" % (num,), file=out)
    print("    \"%s\"," % (name,), file=out)
    print("    %d," % (len(args,)), file=out)
    print("    [", file=out)
    print(", ".join([parse_type(t) for t in args] + ["ARG_UNKNOWN"] * (6 - len(args))), file=out)
    print("]),\n", file=out);
  print("]", file=out)
  out.close()

def main(args):
  if not args:
    print("Usage: %s /path/to/linux_src" % (sys.argv[0],), file=sys.stderr)
    return 1
  linux_dir = args[0]
  for (name, unistd_h) in [("32", "/usr/include/asm/unistd_32.h"), ("64", "/usr/include/asm/unistd_64.h")]:
    syscall_numbers = do_syscall_numbers(unistd_h)
    syscall_types   = find_args(linux_dir)
    write_output('syscallents_'+name+'.py', syscall_types, syscall_numbers)

if __name__ == '__main__':
  sys.exit(main(sys.argv[1:]))

