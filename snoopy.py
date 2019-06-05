#! /usr/bin/env python3

import re
import sys
import os
import subprocess
import datetime
from collections import defaultdict
from mainwindow import Ui_MainWindow
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
import defs
from dialogs import ExecutableDialog
from subprocess_thread import SubprocessThread
from text_stream import TextStream
from bpf.bpf_worker import BPFWorker

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # --- members ---
        self.bpf_workers = defaultdict(lambda: None)
        self.path = ""
        self.directory = ""
        self.update_timer = QTimer(self)
        self.update_timer.start(100)

        # --- connect slots ---
        self.clear_console_button.pressed.connect(self.console_output.clear)
        self.action_Launch_Executable.triggered.connect(self.launch_executable_pressed)

        # --- display window ---
        self.resize(QDesktopWidget().availableGeometry().size() * 0.9)
        self.show()

    # --- slots ---

    def process_events(self, events):
        for event in iter(self.events.popleft()):
            self.log(event)

    def log(self, text):
        try:
            path = self.path
        except:
            path = ""
        now = datetime.datetime.now()
        time_str = now.strftime("[%m/%d/%Y %H:%M:%S]")
        text = "<br>".join(text.split("\n"))
        text = f"{defs.color(6)}^[{defs.color(0)}".join(text.split(""))
        self.console_output.appendHtml("".join([defs.color(4), time_str, " ", defs.color(0), text]))

    def launch_executable_pressed(self):
        dialog = ExecutableDialog(self, command=self.path, directory=self.directory)
        dialog.result.connect(self.launch_executable)
        reply = dialog.exec_()

    def stop_bpf_worker(self,pid):
        print("STOPPING WORKER")
        bpf_worker = self.bpf_workers[pid]
        self.bpf_workers[pid] = None

    def start_bpf_worker(self, pid):
        print("starting bpf worker")
        bpf_worker = BPFWorker(pid, self)
        bpf_worker.sig_events.connect(self.process_events)
        bpf_worker.sig_all_done.connect(self.stop_bpf_worker)
        self.update_timer.timeout.connect(bpf_worker.tick)
        self.bpf_workers[bpf_worker.pid] = bpf_worker

    def launch_executable(self, path, directory):
        thread = SubprocessThread(self, path, directory)
        thread.start()

    def update_path(self, path):
        self.path = path

    def update_directory(self, directory):
        self.directory = directory


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
