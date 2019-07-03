import subprocess
import os
import sys
import signal

from bcc import BPF

import defs

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
        self.binary = which(binary)
        self.args = args

        # --- preferences ---
        self.drop_root = True

        self.strace = []

    def register_perf_outputs(self):
        # syscall entry point
        def on_syscall(cpu, data, size):
            event = self.bpf["syscalls"].event(data)
            syscall = Syscall(event.id)
            self.strace.append(syscall)
        self.bpf["syscalls"].open_perf_buffer(on_syscall, 128)

    def load_bpf(self):
        try:
            self.bpf.cleanup()
            self.bpf = None
        except:
            pass
        with open(defs.BPF_FILE) as f:
            text = f.read()
        text = text.replace("THE_PID", str(self.pid), 1)
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

class Syscall:
    def __init__(self, num, ret=0, args=[]):
        self.num = num
        self.name = defs.SYSCALL[num]
        self.args = args
        self.ret = ret

    def __str__(self):
        return f"{self.name}({', '.join(self.args)}) = {self.ret}"

    def __repr__(self):
        return str(self)
