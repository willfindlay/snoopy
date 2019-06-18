#! /usr/bin/env python3

from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from enum import Enum

class DebuggerModel(QAbstractListModel):
    def __init__(self, parent=None):
        super(DebuggerModel, self).__init__(parent)
        self.list = []

    class Roles(Enum):
        SYSENTRY = Qt.UserRole + 1

    def rowCount(self, parent=QModelIndex()):
        return len(self.list)

    def columnCount(self, parent=QModelIndex()):
        return 1

    def data(self, index, role):
        if not index.isValid():
            return "nil"
        if role == Qt.DisplayRole:
            # TODO: change this up potentially based on what I want to display
            return self.list[index.row()]

    def push_events(self, events, parent = QModelIndex()):
        self.beginInsertRows(parent, len(self.list), len(self.list) + len(events) - 1)
        for event in events:
            self.list.append(event)
        self.endInsertRows()
        return True
