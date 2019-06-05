#! /usr/bin/env python3

from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

class TextStream(QObject):
    new_text = Signal(str)

    def write(self, text):
        self.new_text.emit(text)
