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
from bpf_worker import BPFWorker
from debugger_model import DebuggerModel

class MainWindow(QMainWindow, Ui_MainWindow):
    sig_start_worker = Signal(int)
    sig_stop_worker = Signal()

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # --- members ---
        self.oldpath = ""
        self.path = ""
        self.olddirectory = ""
        self.directory = ""
        self.subprocess_pid = None
        self.console_output_stream = TextStream()
        self.console_output_stream.new_text.connect(self.console_log)

        # --- setup the QProcess ---
        self.process = TracedProcess(self)
        self.process.errorOccurred.connect(self.executable_error)
        #self.process.sig_start_bpf_worker.connect(self.start_bpf_worker)
        self.process.readyReadStandardOutput.connect(self.stdout_ready)
        self.process.readyReadStandardError.connect(self.stderr_ready)
        self.process.finished.connect(self.stop_bpf_worker)
        self.process.started.connect(self.subprocess_started)

        # --- setup separate thread for workers ---
        self.bpf_thread = QThread()
        # timer for updates
        self.update_timer = QTimer()
        self.update_timer.setInterval(16)
        self.update_timer.moveToThread(self.bpf_thread)
        self.bpf_thread.started.connect(self.update_timer.start)
        self.bpf_thread.finished.connect(self.update_timer.deleteLater)
        # worker
        self.bpf_worker = BPFWorker()
        self.bpf_worker.moveToThread(self.bpf_thread)
        self.update_timer.timeout.connect(self.bpf_worker.tick)
        self.bpf_worker.sig_events.connect(self.process_events)
        self.bpf_thread.finished.connect(self.bpf_worker.deleteLater)
        self.sig_start_worker.connect(self.bpf_worker.start_working)
        self.sig_stop_worker.connect(self.bpf_worker.stop_working)
        # start the thread
        self.bpf_thread.start()

        # --- setup the debugger list view ---
        self.debugger_model = DebuggerModel(self.debugger_view)
        self.debugger_view.setModel(self.debugger_model)

        # --- connect menu actions ---
        self.clear_console_button.pressed.connect(self.console_output.clear)
        self.action_Launch_Executable.triggered.connect(self.launch_executable_pressed)

        # --- display window ---
        self.resize(QDesktopWidget().availableGeometry().size() * 0.9)
        self.show()

    # --- slots ---

    def process_events(self, events):
        items = []
        while True:
            try:
                event, etype = events.popleft()
                # set item based on event type
                items.append(f"System call {defs.SYSCALL[event.id]} made.")
            except:
                break
        self.debugger_model.push_events(items)

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
        self.sig_stop_worker.emit()

    def start_bpf_worker(self, pid):
        self.console_log(f"{defs.color(10)}Starting eBPF worker...")
        self.sig_start_worker.emit(pid)

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
        self.start_bpf_worker(self.process.pid())

    def closeEvent(self, event):
        self.bpf_thread.exit()
        event.accept()

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
