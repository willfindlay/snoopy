#! /usr/bin/env python3

import os
import itertools
import time
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from bpf.bpf_worker import BPFWorker
import defs

class TracedProcess(QProcess):
    sig_start_bpf_worker = Signal(int)

    def __init__(self, parent):
        super(TracedProcess, self).__init__(parent=parent)

    def setupChildProcess(self):
        # start the bpf worker
        pid = os.getpid()
        self.sig_start_bpf_worker.emit(pid)
        time.sleep(1)
        # drop privileges
        os.setuid(int(os.environ['SUDO_UID']))
