#! /usr/bin/env python3

import re
import sys
import os
import time
from bcc import BPF
from PySide2.QtCore import QObject, Signal

number = 1

class BPFWorker(QObject):
    # --- signals ---

    def __init__(self):
        super(BPFWorker, self).__init__()
        global number
        self.number = number
        number = number + 1

    def testificate(self):
        print(f"I am a worker {self.number}!")
