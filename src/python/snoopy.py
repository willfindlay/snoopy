import re
import os, sys
import time
import subprocess
import re
import signal
import logging
import ctypes as ct

from bcc import BPF

from .config import Config
from .utils import abs_headers, drop_privileges, c_dir, which
from .syscall import syscalls_32, syscalls_64

log = logging.getLogger()

class Snoopy:
    def __init__(self, args):
        self.bpf = None

    def trace(self, binary, args):
        # Run the tracee and pause before execve until ready
        try:
            pid = self.run_binary(binary, args)
        except TypeError as e:
            sys.exit(-1)
        # Run eBPF program
        text = self.prepare_bpf_program(pid)
        self.bpf = BPF(text=text)
        self.register_perf_buffers(self.bpf)
        # Wakeup tracee
        os.kill(pid, signal.SIGUSR1)
        # Do the tracing
        while True:
            self.bpf.perf_buffer_poll(Config.perf_poll_timeout)
            try:
                # Poll for child
                os.kill(pid, 0)
            except:
                # One last flush of perf buffers
                self.bpf.perf_buffer_poll(Config.perf_poll_timeout)
                log.info("Child process has exited")
                break
            time.sleep(Config.tick_delay)

    @drop_privileges
    def run_binary(self, binary, args):
        # Wake up and do nothing on SIGCLHD
        signal.signal(signal.SIGUSR1, lambda x,y: None)
        # Reap zombies
        signal.signal(signal.SIGCHLD, lambda x,y: os.wait())
        binary = which(binary)
        args = [binary] + args
        pid = os.fork()
        # Setup traced process
        if pid == 0:
            signal.pause()
            os.execvp(binary, args)
        # Return pid of traced process
        return pid

    # BPF stuff below this line --------------------------------

    # Setup the bpf program to trace PID
    def prepare_bpf_program(self, pid):
        with open(os.path.join(c_dir, 'bpf.c'), 'r') as f:
            text = f.read()
        text = abs_headers(text)
        text = re.sub("__TRACE_PID", str(pid), text)
        return text

    # Register perf buffers for communication with eBPF program
    def register_perf_buffers(self, bpf):
        # Returns a lost callback for a perf buffer with name buff_name
        def lost_cb(buff_name):
            def closure(lost):
                log.warning(f"Lost {lost} samples from perf_buffer {buff_name}")
            return closure

        # executable has been processed in ebpH_on_do_open_execat
        def on_syscall(cpu, data, size):
            event = bpf["on_syscall"].event(data)
            syscall = syscalls_64[event.num]
            args = event.args
            s = f"{syscalls_64[event.num].template(*[arg for arg in args])}"
            print(s)
        bpf["on_syscall"].open_perf_buffer(on_syscall, lost_cb=lost_cb("on_syscall"), page_cnt=2**8)

        log.debug(f'Registered perf buffers successfully')
