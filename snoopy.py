#! /usr/bin/env python3

import re
import sys
import os
from mainwindow import Ui_MainWindow
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from bpf.bpf_worker import BPFWorker

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # --- members ---
        self.workers = []
        self.update_timer = QTimer(self)
        self.update_timer.timeout.connect(self.tick)
        self.update_timer.start(500)

        # --- connect slots ---
        self.start_worker_button.pressed.connect(self.start_worker)

        # --- display window ---
        self.showMaximized()

    def tick(self):
        for worker in self.workers:
            worker.testificate()

    def start_worker(self):
        worker = BPFWorker()
        self.workers.append(worker)

if __name__ == "__main__":
    # check privileges
    if not ('SUDO_USER' in os.environ and os.geteuid() == 0):
        print("This script must be run with root privileges! Exiting.")
        sys.exit(-1)
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    ret = app.exec_()
    sys.exit(ret)
