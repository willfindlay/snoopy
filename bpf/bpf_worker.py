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
    sig_all_done = Signal(int)

    def __init__(self, pid, parent):
        super(BPFWorker, self).__init__(parent=parent)
        self.events = deque() # maintain a deque for events
        self.ready_to_delete = False
        self.done_work = False
        self.pid = pid
        text = self.load_bpf_code()
        text = text.replace("THE_PID",str(pid),1)
        self.bpf = BPF(text=text)
        self.register_perf_buffers()

    def register_perf_buffers(self):
        # syscall entry point
        def on_syscall(cpu, data, size):
            event = self.bpf["syscalls"].event(data)
            s = f"System call {event.id} has been made!"
            print(s)
            # flag for exit if we detect a quit systemcall
            if(event.id in [60, 261]):
                self.done_work = True
            self.events.append(s)
        self.bpf["syscalls"].open_perf_buffer(on_syscall)

    def load_bpf_code(self):
        with open(defs.BPF_FILE, "r") as f:
            text = f.read()
        return text

    def send_events(self):
        self.sig_events.emit(self.events)
        self.events.clear()

    def tick(self):
        try:
            self.bpf.perf_buffer_poll(100)
            send_events()
        except:
            pass
        if self.done_work:
            send_events()
            self.bpf.cleanup()
            self.deleteLater()
