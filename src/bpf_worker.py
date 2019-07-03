#! /usr/bin/env python3

import re
import sys
import os
import time
import ctypes as ct
from collections import deque
from bcc import BPF, USDT, utils
from PySide2.QtCore import QObject, Signal
import defs

class BPFWorker(QObject):
    # --- signals ---
    sig_events = Signal(deque)

    def __init__(self, parent=None):
        super(BPFWorker, self).__init__(parent=parent)
        self.events = deque() # maintain a deque for events

    def register_perf_buffers(self):
        # syscall entry point
        def on_syscall(cpu, data, size):
            event = self.bpf["syscalls"].event(data)
            self.events.append((event, defs.Events.SYSENTRY))
        self.bpf["syscalls"].open_perf_buffer(on_syscall, 128)

    def start_working(self, pid):
        # load the bpf program
        with open(defs.BPF_FILE, "r") as f:
            text = f.read()
        # sub in the pid
        text = text.replace("THE_PID",str(pid),1)
        # compile and start the bpf program
        self.bpf = BPF(text=text)
        self.register_perf_buffers()

    def poll_events(self, timeout=100):
        try:
            self.bpf
        except:
            return
        self.bpf.perf_buffer_poll(timeout)
        self.send_events()

    def stop_working(self):
        self.poll_events()
        self.bpf.cleanup()
        self.bpf = None

    def send_events(self):
        self.sig_events.emit(self.events.copy())
        self.events.clear()

    def tick(self):
        self.poll_events()
