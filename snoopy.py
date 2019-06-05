#! /usr/bin/env python3

import re
import sys
import os
import datetime
from collections import defaultdict
from mainwindow import Ui_MainWindow
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
import defs
from dialogs import ExecutableDialog
from tracedprocess import TracedProcess
from text_stream import TextStream
from bpf.bpf_worker import BPFWorker

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # --- members ---
        self.bpf_workers = defaultdict(lambda: None)
        self.oldpath = ""
        self.path = ""
        self.olddirectory = ""
        self.directory = ""
        self.subprocess_pid = None
        self.update_timer = QTimer(self)
        self.update_timer.start(100)
        self.console_output_stream = TextStream()
        self.console_output_stream.new_text.connect(self.console_log)

        # setup the QProcess
        self.process = TracedProcess(self)
        self.process.errorOccurred.connect(self.executable_error)
        #self.process.sig_start_bpf_worker.connect(self.start_bpf_worker)
        self.process.readyReadStandardOutput.connect(self.stdout_ready)
        self.process.readyReadStandardError.connect(self.stderr_ready)
        self.process.finished.connect(self.flag_bpf_worker_for_close)
        self.process.started.connect(self.subprocess_started)

        # --- connect slots ---
        self.clear_console_button.pressed.connect(self.console_output.clear)
        self.action_Launch_Executable.triggered.connect(self.launch_executable_pressed)

        # --- display window ---
        self.resize(QDesktopWidget().availableGeometry().size() * 0.9)
        self.show()

    # --- slots ---

    def process_events(self, events):
        while True:
            try:
                event = events.popleft()
                self.event_log(event)
            except:
                break

    def event_log(self, event):
        # TODO: make this append to the left hand side list view
        print(event)

    def console_log(self, text):
        now = datetime.datetime.now()
        time_str = now.strftime("[%m/%d/%Y %H:%M:%S]")
        text = "<br>".join(text.split("\n"))
        text = f"{defs.color(6)}^[{defs.color(0)}".join(text.split(""))
        self.console_output.appendHtml("".join([defs.color(4), time_str, " ", defs.color(0), text]))

    def stdout_ready(self):
        text = f"{defs.color(5)}Output from {defs.color(3)}{self.path} {defs.color(4)}{self.process.pid()}{defs.color(0)}"
        text = "<br>".join([text, self.process.readAllStandardOutput().data().decode('utf-8')])
        self.console_output_stream.write(text)

    def stderr_ready(self):
        text = f"{defs.color(5)}Error from {defs.color(3)}{self.path} {defs.color(4)}{self.process.pid()}{defs.color(9)}"
        text = "<br>".join([text, self.process.readAllStandardError().data().decode('utf-8'), f"{defs.color(0)}"])
        self.console_output_stream.write(text)

    def launch_executable_pressed(self):
        dialog = ExecutableDialog(self, command=self.path, directory=self.directory)
        dialog.result.connect(self.launch_executable)
        reply = dialog.exec_()

    def stop_bpf_worker(self,pid):
        self.console_log(f"{defs.color(9)}Stopping eBPF worker...")
        bpf_worker = self.bpf_workers[pid]
        self.bpf_workers[pid] = None

    def flag_bpf_worker_for_close(self):
        worker = self.bpf_workers[self.subprocess_pid]
        worker.done_work = True
        self.subprocess_pid = None

    def start_bpf_worker(self):
        self.console_log(f"{defs.color(10)}Starting eBPF worker...")
        bpf_worker = BPFWorker(self.process.pid(), self)
        bpf_worker.sig_events.connect(self.process_events)
        bpf_worker.sig_all_done.connect(self.stop_bpf_worker)
        self.update_timer.timeout.connect(bpf_worker.tick)
        self.bpf_workers[bpf_worker.pid] = bpf_worker

    def executable_error(self):
        errStr = self.process.errorString()
        if re.match("^chdir", errStr):
            self.console_output_stream.write(f"{defs.color(9)} {errStr}: {defs.color(3)}{self.directory}")
        else:
            self.console_output_stream.write(f"{defs.color(9)} {errStr}: {defs.color(3)}{self.path}")
        self.directory = self.olddirectory
        self.path = self.oldpath

    def subprocess_started(self):
        self.subprocess_pid = self.process.pid()

    def launch_executable(self, path, directory):
        self.oldpath = self.path
        self.olddirectory = self.directory
        self.path = path
        self.directory = directory
        args = path.split(" ")
        self.process.setWorkingDirectory(directory)
        self.process.start(args[0], args[1:])
        self.start_bpf_worker()

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
