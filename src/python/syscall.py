import os
import sys
import ctypes as ct

import config

class Syscall:
    def __init__(self, num, ret=0, args=[], str_args=[], finished=False):
        name, max_args, argtypes = config.SYSCALL[num]
        self.num = num
        self.name = name
        self.finished = finished

        # handle args
        self.args = list(args)
        str_args = list(str_args)
        self.args = self.args[:max_args]
        for i, arg in enumerate(self.args):
            if argtypes[i] == config.ARG_INT:
                self.args[i] = int(self.args[i])
            elif argtypes[i] == config.ARG_STR:
                self.args[i] = f"\"{ct.cast(str_args[i], ct.c_char_p).value.decode('utf-8')}\""
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

# must match the struct in bpf/defs.h
class SyscallData(ct.Structure):
    _fields_ = [("id", ct.c_uint64),
                ("pid_tgid", ct.c_uint64),
                ("args", ct.c_ulong * 6),
                ("str_args", (ct.c_char * 6) * 64),
                ("ret", ct.c_long)]

