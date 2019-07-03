#! /usr/bin/env python3

import os
import re
from executabledialog import Ui_ExecutableDialog
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

class ExecutableDialog(QDialog, Ui_ExecutableDialog):
    result = Signal(str, str)

    def __init__(self, parent=None, command="", directory=""):
        super(ExecutableDialog, self).__init__(parent)
        self.setupUi(self)
        self.command.setText(command)
        self.command.setFocus()
        self.command.selectAll()

        self.directory.setPlaceholderText(re.sub(f"^{os.path.expanduser('~')}", "~", os.getcwd()))
        if directory == os.getcwd():
            directory = ""
        directory = re.sub(f"^{os.path.expanduser('~')}", "~", directory)
        self.directory.setText(directory)

        self.accepted.connect(self.send_result)

        self.resize(QDesktopWidget().availableGeometry().size() * 0.6)

    def accept(self):
        super().accept()

    def send_result(self):
        command = self.command.text()
        directory = self.directory.text()
        if directory.isspace() or not directory:
            directory = os.getcwd()
        directory=os.path.expanduser(directory)
        self.result.emit(command, directory)
