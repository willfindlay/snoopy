#! /usr/bin/env python3

import re
import sys
import os
import datetime
import time
from collections import defaultdict
import argparse
from mainwindow import Ui_MainWindow
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
import defs
from dialogs import ExecutableDialog
from text_stream import TextStream
from debugger_model import DebuggerModel
from program import Program
from poller import Poller

class MainWindow(QMainWindow, Ui_MainWindow):
    sig_start_worker = Signal(int)
    sig_stop_worker = Signal()

    def __init__(self, args):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # --- get args and register initial program ---
        self.args = args
        self.program = Program(args.binary, args.args)

        # --- setup polling thread ---
        self.poller_thread = QThread()
        self.poll_timer = QTimer()
        self.poll_timer.setInterval(16)
        self.poll_timer.moveToThread(self.poller_thread)
        self.poller_thread.started.connect(self.poll_timer.start)
        self.poller_thread.finished.connect(self.poll_timer.deleteLater)
        self.poller = Poller(self.program)
        self.poller.moveToThread(self.poller_thread)

        # *** connect signals here
        self.poller.sig_syscalls.connect(self.log_strace)
        self.poll_timer.timeout.connect(self.poller.poll)

        self.poller_thread.start()

        # --- members ---
        self.console_output_stream = TextStream()
        self.console_output_stream.new_text.connect(self.console_log)

        # --- connect menu actions ---
        self.clear_console_button.pressed.connect(self.console_output.clear)
        self.action_Launch_Executable.triggered.connect(self.launch_executable)

        # --- display window ---
        self.resize(QDesktopWidget().availableGeometry().size() * 0.9)
        self.show()

    # --- slots ---

    def log_strace(self, strace):
        for syscall in strace:
            self.console_log(str(syscall))

    def console_log(self, text):
        now = datetime.datetime.now()
        time_str = now.strftime("[%m/%d/%Y %H:%M:%S]")
        text = "<br>".join(text.split("\n"))
        text = f"{defs.color(6)}^[{defs.color(0)}".join(text.split(""))
        self.console_output.appendHtml("".join([defs.color(4), time_str, " ", defs.color(0), text]))

    def launch_executable(self):
        self.program.snoopy_exec()

    def closeEvent(self, event):
        self.poller_thread.exit()
        event.accept()

if __name__ == "__main__":
    # check privileges
    if not (os.geteuid() == 0):
        print("This script must be run with root privileges! Exiting.")
        sys.exit(-1)
    defs.init()

    parser = argparse.ArgumentParser(description="Snoopy is a modern GNU/Linux debugger with a simple,\
            easy to use design philosophy. It leverages eBPF technology in modern Linux kernels, rendering\
            it both performant and secure.", prog="sudo snoopy")
    parser.add_argument('binary', help="Path to the binary you want to analyze.")
    parser.add_argument('args', nargs='*', help="Arguments to pass to the binary.")

    # parse arguments, first try
    args, unknown = parser.parse_known_args()
    # hack to allow arguments to be passed to the analyzed program
    sys.argv.insert(sys.argv.index(args.binary), "--")
    # parse args, second try
    args = parser.parse_args()

    app = QApplication(sys.argv)
    mainWin = MainWindow(args)
    ret = app.exec_()
    sys.exit(ret)
