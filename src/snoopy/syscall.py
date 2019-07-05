import os
import sys
import ctypes as ct
from collections import defaultdict

import bcc.syscall

from . import config

ARG_UNKNOWN = 0
ARG_INT = 1
ARG_STR = 2
ARG_PTR = 3

DEFAULT_ARGS = (ARG_INT,ARG_INT,ARG_INT,ARG_INT,ARG_INT,ARG_INT)
FORMAT = defaultdict(lambda: SyscallFormat())

class Syscall:
    def __init__(self, num, ret=0, args=[], str_args=[], finished=False):
        name, max_args, argtypes = config.SYSCALL[num]
        self.format = FORMAT[num]
        print(self.format)
        self.num = num
        self.name = bcc.syscall.syscall_name(num).decode('utf-8')
        self.finished = finished

        # handle args
        self.args = list(args)
        self.str_args = list(str_args)
        self.args = self.args[:max_args]
        for i, arg in enumerate(self.args):
            if argtypes[i] == config.ARG_INT:
                self.args[i] = int(self.args[i])
            elif argtypes[i] == config.ARG_STR:
                #self.args[i] = f"\"{ct.cast(str_args[i], ct.c_char_p).value.decode('utf-8')}\""
                self.args[i] = f"\"{ct.cast(str_args[i], ct.c_char_p).value.decode('utf-8')}\""
                self.args[i] = self.args[i].replace("\n",f"{config.color(4)}\\n{config.color(1)}")
            elif argtypes[i] == config.ARG_PTR:
                self.args[i] = hex(self.args[i])
            else:
                self.args[i] = "unknown"
        self.args = map(str, self.args)
        self.ret = ret

    def __str__(self):
        return f"{self.name}({', '.join(self.args)}) = {'?' if not self.finished else self.ret}"

    def __repr__(self):
        return str(self)

class SyscallFormat:
    def __init__(self, arg_types=DEFAULT_ARGS, ret_type=ARG_INT):
        for i in range(len(arg_types), 6):
            arg_types = arg_types + (ARG_UNKNOWN)
        assert len(arg_types) == 6

        self.arg_types = arg_types
        self.ret_type = ret_type

    def flags(self, possible_flags, value):
        num_flags = len(possible_flags)

        all_flags_on = 2 ** num_flags - 1
        flag_bits = bin(value & all_flags_on)[2:].zfill(num_flags)
        flags = []

        for i,bit in enumerate(reversed(flag_bits)):
            if bit == '1':
                flags.append(possible_flags[i])

        return "|".join(flags)

    def format(self, syscall):
        args = []
        for i in range(6):
            if type(self.arg_types[i]) == tuple:
                args.append(self.flags(self.arg_types[i], syscall.args[i]))
            elif self.arg_types[i] == ARG_INT:
                args.append(int(syscall.args[i]))
            elif self.arg_types[i] == ARG_PTR:
                args.append(hex(syscall.args[i]))
            elif self.arg_types[i] == ARG_STR:
                args.append(hex(syscall.args[i]))
            else: # ARG_UNKNOWN
                break
        return f"{syscall.name}({', '.join(args)}) = {'?' if not syscall.finished else syscall.ret}"

# must match the struct in bpf/defs.h
class SyscallData(ct.Structure):
    _fields_ = [("id", ct.c_uint64),
                ("pid_tgid", ct.c_uint64),
                ("args", ct.c_ulong * 6),
                ("str_args", (ct.c_char * 6) * 64),
                ("ret", ct.c_long)]

