import subprocess
import os
import sys
import signal

from bcc import BPF
import ctypes as ct

import config
from syscall import Syscall, SyscallData

def which(binary):
    try:
        cmd = ["which", binary]
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        res = p.stdout.readlines()
        if len(res) == 0:
            raise Exception("binary not found")
        return os.path.realpath(res[0].strip())
    except:
        # fallback
        if os.path.isfile(binary):
          return os.path.realpath(binary)
        else:
            raise Exception("binary not found")

class Program:
    def __init__(self, binary, args=[]):
        self.bpf = None

        # --- binary and arguments ---
        self.set_binary(binary)
        self.args = args

        # --- preferences ---
        self.drop_root = True

        self.strace = []

    def set_binary(self, binary):
        self.binary = which(binary)

    def register_perf_outputs(self):
        # syscall entry point
        def on_syscall(cpu, data, size):
            event = ct.cast(data, ct.POINTER(SyscallData)).contents
            syscall = Syscall(event.id, args=event.args, str_args=event.str_args, ret=event.ret)
            self.strace.append(syscall)
        self.bpf["syscalls"].open_perf_buffer(on_syscall, 128)

    def load_bpf(self):
        try:
            self.bpf.cleanup()
            self.bpf = None
        except:
            pass
        with open(config.BPFFILE) as f:
            text = f.read()
        text = text.replace("THE_PID", str(self.pid))
        text = text.replace("BPFDIR", str(config.BPFDIR))
        self.bpf = BPF(text = text)
        self.register_perf_outputs()
        os.kill(self.pid, signal.SIGUSR1)

    def snoopy_exec(self):
        try:
            os.kill(self.pid, signal.SIGKILL)
        except:
            pass
        pid = os.fork()
        if pid == 0:
            binary = self.binary
            args = [self.binary] + self.args
            # we need to wait for a signal before we exec
            signal.signal(signal.SIGUSR1, lambda x,y: None)
            signal.pause()
            if self.drop_root:
                os.setuid(int(os.environ['SUDO_UID']))
            os.execvp(binary, args)
        self.pid = pid
        self.load_bpf()
