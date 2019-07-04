# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './gui/executabledialog.ui',
# licensing of './gui/executabledialog.ui' applies.
#
# Created: Wed Jul  3 15:06:04 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ExecutableDialog(object):
    def setupUi(self, ExecutableDialog):
        ExecutableDialog.setObjectName("ExecutableDialog")
        ExecutableDialog.resize(616, 502)
        self.gridLayout_2 = QtWidgets.QGridLayout(ExecutableDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.buttonBox = QtWidgets.QDialogButtonBox(ExecutableDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 8, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 7, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 4, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(ExecutableDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 1, 1, 1)
        self.directory = QtWidgets.QLineEdit(ExecutableDialog)
        self.directory.setPlaceholderText("")
        self.directory.setClearButtonEnabled(True)
        self.directory.setObjectName("directory")
        self.gridLayout.addWidget(self.directory, 3, 2, 1, 1)
        self.label = QtWidgets.QLabel(ExecutableDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 1, 1, 1)
        self.command = QtWidgets.QLineEdit(ExecutableDialog)
        self.command.setClearButtonEnabled(True)
        self.command.setObjectName("command")
        self.gridLayout.addWidget(self.command, 2, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 3, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(ExecutableDialog)
        self.label_3.setScaledContents(False)
        self.label_3.setWordWrap(True)
        self.label_3.setMargin(50)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.gridLayout_2.addLayout(self.horizontalLayout, 5, 0, 1, 1)

        self.retranslateUi(ExecutableDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), ExecutableDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), ExecutableDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ExecutableDialog)
        ExecutableDialog.setTabOrder(self.command, self.directory)

    def retranslateUi(self, ExecutableDialog):
        ExecutableDialog.setWindowTitle(QtWidgets.QApplication.translate("ExecutableDialog", "Dialog", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("ExecutableDialog", "Directory", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("ExecutableDialog", "Command", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("ExecutableDialog", "Enter the command you want in the first box.\n"
"\n"
"If you want to execute the command in a different working directory, enter the desired directory in the second box.", None, -1))

