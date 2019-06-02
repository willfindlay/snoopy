#! /usr/bin/env python3

import re
import sys
import os
from mainwindow import Ui_MainWindow
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
import subprocess
from bpf.bpf_worker import BPFWorker
import defs

class TextStream(QObject):
    new_text = Signal(str)

    def write(self, text):
        self.new_text.emit(text[0].decode("utf-8"))

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # --- members ---
        self.workers = []
        self.update_timer = QTimer(self)
        self.update_timer.timeout.connect(self.tick)
        self.update_timer.start(500)
        # this is a stream to handle console output to the GUI
        self.console_output_stream = TextStream()

        # --- connect slots ---
        self.console_output_stream.new_text.connect(self.log)
        #self.start_worker_button.pressed.connect(self.start_worker)
        self.action_Launch_Executable.triggered.connect(self.launch_executable_pressed)

        # --- display window ---
        self.showMaximized()

    # --- slots ---

    def log(self, text):
        self.console_output.appendHtml(text)

    def tick(self):
        for worker in self.workers:
            worker.testificate()

    def launch_executable_pressed(self):
        self.launch_executable("ls")

    def launch_executable(self, path):
        process = subprocess.Popen(path, stdout=subprocess.PIPE)
        self.console_output_stream.write(process.communicate())

    def start_worker(self):
        worker = BPFWorker()
        self.workers.append(worker)

if __name__ == "__main__":
    # check privileges
    if not ('SUDO_USER' in os.environ and os.geteuid() == 0):
        print("This script must be run with root privileges! Exiting.")
        sys.exit(-1)
    defs.init()
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    ret = app.exec_()
    sys.exit(ret)
