import re
import os, sys
import time
import subprocess
import re
import signal
import logging

from bcc import BPF

from .config import Config
from .utils import abs_headers, drop_privileges, c_dir, which
from .syscall import syscalls_32, syscalls_64

log = logging.getLogger()

class Snoopy:
    def __init__(self, args):
        self.bpf = None

    # Setup the bpf program to trace PID
    def prepare_bpf_program(self, pid):
        with open(os.path.join(c_dir, 'bpf.c'), 'r') as f:
            text = f.read()
        text = abs_headers(text)
        text = re.sub("__TRACE_PID", str(pid), text)
        return text

    def trace(self, binary, args):
        try:
            pid = self.run_binary(binary, args)
        except TypeError as e:
            sys.exit(-1)
        text = self.prepare_bpf_program(pid)
        self.bpf = BPF(text=text)
        os.kill(pid, signal.SIGUSR1)

    @drop_privileges
    def run_binary(self, binary, args):
        signal.signal(signal.SIGUSR1, lambda x,y: None)
        binary = which(binary)
        args = [binary] + args
        pid = os.fork()
        # Setup traced process
        if pid == 0:
            signal.pause()
            os.execvp(binary, args)
        # Return pid of traced process
        return pid
