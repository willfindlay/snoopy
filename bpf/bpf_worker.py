#! /usr/bin/env python3

import re
import sys
import os
import time
from bcc import BPF
from PySide2.QtCore import QObject, Signal
import defs

number = 1

class BPFWorker(QObject):
    # --- signals ---

    def __init__(self):
        super(BPFWorker, self).__init__()
        global number
        self.id = number
        number = number + 1

        text = self.load_bpf_code()
        self.bpf = BPF(text=text)

    def load_bpf_code(self):
        with open(defs.BPF_FILE, "r") as f:
            text = f.read()
        return text

    def testificate(self):
        print(f"I am a worker {self.id}!")
