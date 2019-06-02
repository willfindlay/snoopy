# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './gui/mainwindow.ui',
# licensing of './gui/mainwindow.ui' applies.
#
# Created: Sun Jun  2 15:55:20 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/assets/img/snoopy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#centralwidget{\n"
"background: #eee;\n"
"background-image: url(:/img/assets/img/snoopy.png);\n"
"background-repeat: no-repeat;\n"
"background-position: bottom left;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.clear_console_button = QtWidgets.QPushButton(self.frame)
        self.clear_console_button.setObjectName("clear_console_button")
        self.horizontalLayout.addWidget(self.clear_console_button)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.console_output = QtWidgets.QPlainTextEdit(self.frame)
        self.console_output.setObjectName("console_output")
        self.gridLayout_2.addWidget(self.console_output, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 29))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Tracing = QtWidgets.QMenu(self.menubar)
        self.menu_Tracing.setObjectName("menu_Tracing")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_Launch_Executable = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/assets/img/icons8-launch-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Launch_Executable.setIcon(icon1)
        self.action_Launch_Executable.setObjectName("action_Launch_Executable")
        self.action_Quit = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/assets/img/icons8-shutdown-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Quit.setIcon(icon2)
        self.action_Quit.setObjectName("action_Quit")
        self.menu_File.addAction(self.action_Launch_Executable)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Quit)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Tracing.menuAction())
        self.toolBar.addAction(self.action_Launch_Executable)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_Quit)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.action_Quit, QtCore.SIGNAL("triggered()"), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "snoopy", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Console Output", None, -1))
        self.clear_console_button.setText(QtWidgets.QApplication.translate("MainWindow", "Clear", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "TextLabel", None, -1))
        self.menu_File.setTitle(QtWidgets.QApplication.translate("MainWindow", "&File", None, -1))
        self.menu_Tracing.setTitle(QtWidgets.QApplication.translate("MainWindow", "&Tracing", None, -1))
        self.toolBar.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "toolBar", None, -1))
        self.action_Launch_Executable.setText(QtWidgets.QApplication.translate("MainWindow", "&Launch Executable", None, -1))
        self.action_Launch_Executable.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+E", None, -1))
        self.action_Quit.setText(QtWidgets.QApplication.translate("MainWindow", "&Quit", None, -1))
        self.action_Quit.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+Q", None, -1))

import resources_rc
