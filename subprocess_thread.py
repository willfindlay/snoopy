#! /usr/bin/env python3

import os
import subprocess
import itertools
import time
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from text_stream import TextStream
from bpf.bpf_worker import BPFWorker
import defs

class SubprocessThread(QThread):
    sig_update_path = Signal(str)
    sig_update_directory = Signal(str)
    sig_log_output = Signal(str)
    sig_start_bpf_worker = Signal(int)

    def __init__(self, parent, path, directory):
        super(SubprocessThread, self).__init__(parent=parent)
        self.path = path
        self.directory = directory
        # this is a stream to handle console output to the GUI
        self.console_output_stream = TextStream()

        # connect slots
        self.connect_slots()

    def connect_slots(self):
        self.finished.connect(self.deleteLater)
        self.sig_update_path.connect(self.parent().update_path)
        self.sig_update_directory.connect(self.parent().update_directory)
        self.console_output_stream.new_text.connect(self.parent().log)
        self.sig_start_bpf_worker.connect(self.parent().start_bpf_worker)

    def run(self):
        def demote():
            # drop privileges
            os.setuid(int(os.environ['SUDO_UID']))
            # start the bpf worker
            pid = os.getpid()
            self.sig_start_bpf_worker.emit(pid)
            time.sleep(1)

        path = self.path
        directory = self.directory
        self.path = path
        args = path.split(" ")
        path = args[0]
        try:
            # launch the process
            process = subprocess.Popen(args, preexec_fn=demote, cwd=directory, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            self.directory = directory
            self.console_output_stream.write(f"{defs.color(5)}Running {defs.color(3)}{path} {defs.color(1)}{process.pid}")

            self.sig_update_path.emit(path)
            self.sig_update_directory.emit(directory)
            while True:
                text = f"{defs.color(5)}Output from {defs.color(3)}{path} {defs.color(1)}{process.pid}{defs.color(0)}"
                # fetch stdout and stderr output for console logging
                for line in itertools.chain(iter(process.stdout.readline, b''),
                        iter(process.stderr.readline, b'')):
                    text = "<br>".join([text, line.decode("utf-8").rstrip()])
                self.console_output_stream.write(text)
                if process.poll() is not None:
                    break

        except FileNotFoundError:
            self.console_output_stream.write(f"{defs.color(9)} ERROR: No such file or directory: {defs.color(3)}{path}")
        except PermissionError:
            self.console_output_stream.write(f"{defs.color(9)} ERROR: Not an executable: {defs.color(3)}{path}")

        print("work done!")
