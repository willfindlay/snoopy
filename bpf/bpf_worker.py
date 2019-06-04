#! /usr/bin/env python3

import re
import sys
import os
import time
import ctypes as ct
from bcc import BPF, USDT, utils
from PySide2.QtCore import QObject, Signal
import defs

number = 1

class BPFWorker(QObject):
    # --- signals ---
    sig_clean = Signal()
    sig_syscall_entry = Signal(ct.Structure)

    def __init__(self, pid):
        super(BPFWorker, self).__init__()
        global number
        self.id = number
        number = number + 1

        text = self.load_bpf_code()
        text = text.replace("THE_PID",str(pid),1)
        self.bpf = BPF(text=text)
        self.register_perf_buffers()

    def register_perf_buffers(self):
        def on_syscall(cpu, data, size):
            event = self.bpf["syscalls"].event(data)
            s = f"System call {event.sysnum} has been made!"
            print(s)
            self.sig_syscall_entry.emit(event)
        self.bpf["syscalls"].open_perf_buffer(on_syscall)

    def load_bpf_code(self):
        with open(defs.BPF_FILE, "r") as f:
            text = f.read()
        return text

    def tick(self):
        self.bpf.perf_buffer_poll(100)

    def cleanup(self):
        self.bpf.cleanup()
        self.sig_clean.emit()
