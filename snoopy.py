#! /usr/bin/env python3

import re
import sys
import os
import subprocess
import datetime
from mainwindow import Ui_MainWindow
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from bpf.bpf_worker import BPFWorker
import defs
from dialogs import ExecutableDialog

class TextStream(QObject):
    new_text = Signal(str)

    def write(self, text):
        self.new_text.emit(text)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # --- members ---
        self.workers = []
        self.path = ""
        self.directory = ""
        self.update_timer = QTimer(self)
        self.update_timer.timeout.connect(self.tick)
        self.update_timer.start(500)
        self.process_output_thread = QThread(self)
        # this is a stream to handle console output to the GUI
        self.console_output_stream = TextStream()

        # --- connect slots ---
        self.console_output_stream.new_text.connect(self.log)
        self.clear_console_button.pressed.connect(self.console_output.clear)
        self.action_Launch_Executable.triggered.connect(self.launch_executable_pressed)

        # --- display window ---
        self.resize(QDesktopWidget().availableGeometry().size() * 0.9)
        self.show()

    # --- slots ---

    def log(self, text):
        try:
            path = self.path
        except:
            path = ""
        now = datetime.datetime.now()
        time_str = now.strftime("[%m/%d/%Y %H:%M:%S]")
        text = "<br>".join(text.split("\n"))
        text = f"{defs.color(6)}^[{defs.color(0)}".join(text.split(""))
        self.console_output.appendHtml("".join([defs.color(4), time_str, defs.color(3), " ", path, "<br>", text]))

    # FIXME: actual BPF logic will go here
    def tick(self):
        for worker in self.workers:
            worker.tick()

    def launch_executable_pressed(self):
        dialog = ExecutableDialog(self, command=self.path, directory=self.directory)
        dialog.result.connect(self.launch_executable)
        reply = dialog.exec_()

    def launch_executable(self, path, directory):
        def demote():
            # drop privileges
            os.setuid(int(os.environ['SUDO_UID']))

        oldpath = self.path
        self.path = path
        args = path.split(" ")
        path = args[0]
        iserr = False
        try:
            # launch the process
            process = subprocess.Popen(args, preexec_fn=demote, cwd=directory, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            # start the bpf worker
            self.start_worker(process.pid)

            self.directory = directory
            # fetch stdout and stderr output for console logging
            text, err = process.communicate() # FIXME: we will need to use a thread fo this and read from process.stdout and process.stderr directly
            try:
                text = text.decode("utf-8")
            except:
                text = ""
            try:
                err  = err.decode("utf-8")
            except:
                err = ""
            text = "".join([defs.color(0),text,defs.color(9),err])
        except FileNotFoundError:
            text = "".join([defs.color(9), "ERR: No such file or directory ", defs.color(3), path, "<br>"])
            iserr = True
        except PermissionError:
            text = "".join([defs.color(9), "ERR: Not an executable ", defs.color(3), path, "<br>"])
            iserr = True
        self.console_output_stream.write(text)
        if iserr:
            self.path = oldpath

    def start_worker(self, pid):
        worker = BPFWorker(pid)
        worker.sig_clean.connect(worker.deleteLater)
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
