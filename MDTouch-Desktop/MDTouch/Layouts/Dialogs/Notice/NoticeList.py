# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NoticeList.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 480)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(10, 10, 621, 421))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.noticeListLabel = QtWidgets.QLabel(self.frame)
        self.noticeListLabel.setGeometry(QtCore.QRect(250, 0, 131, 41))
        self.noticeListLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.noticeListLabel.setObjectName("noticeListLabel")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(10, 41, 601, 371))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.okbutton = QtWidgets.QPushButton(Form)
        self.okbutton.setGeometry(QtCore.QRect(530, 440, 89, 25))
        self.okbutton.setObjectName("okbutton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Notices"))
        self.noticeListLabel.setText(_translate("Form", "Notices"))
        self.okbutton.setText(_translate("Form", "close"))

