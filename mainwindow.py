# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './gui/mainwindow.ui',
# licensing of './gui/mainwindow.ui' applies.
#
# Created: Sun Jun  2 13:16:16 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.start_worker_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_worker_button.setGeometry(QtCore.QRect(130, 70, 181, 35))
        self.start_worker_button.setObjectName("start_worker_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 29))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.start_worker_button.setText(QtWidgets.QApplication.translate("MainWindow", "create worker", None, -1))

import resources_rc
