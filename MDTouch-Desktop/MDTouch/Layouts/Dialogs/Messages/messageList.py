# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'messageList.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_messageList(object):
    def setupUi(self, messageList):
        messageList.setObjectName("messageList")
        messageList.resize(640, 480)
        self.frame = QtWidgets.QFrame(messageList)
        self.frame.setGeometry(QtCore.QRect(10, 10, 621, 421))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.ambulanceListLabel = QtWidgets.QLabel(self.frame)
        self.ambulanceListLabel.setGeometry(QtCore.QRect(260, 0, 191, 41))
        self.ambulanceListLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.ambulanceListLabel.setObjectName("ambulanceListLabel")
        self.sendTableWidget = QtWidgets.QTableWidget(self.frame)
        self.sendTableWidget.setGeometry(QtCore.QRect(10, 41, 300, 371))
        self.sendTableWidget.setObjectName("sendTableWidget")
        self.sendTableWidget.setColumnCount(0)
        self.sendTableWidget.setRowCount(0)
        self.sendNewMessage = QtWidgets.QPushButton(self.frame)
        self.sendNewMessage.setGeometry(QtCore.QRect(438, 10, 171, 25))
        self.sendNewMessage.setObjectName("sendNewMessage")
        self.recievedTableWidget = QtWidgets.QTableWidget(self.frame)
        self.recievedTableWidget.setGeometry(QtCore.QRect(313, 40, 300, 371))
        self.recievedTableWidget.setObjectName("recievedTableWidget")
        self.recievedTableWidget.setColumnCount(0)
        self.recievedTableWidget.setRowCount(0)
        self.okButton = QtWidgets.QPushButton(messageList)
        self.okButton.setGeometry(QtCore.QRect(530, 440, 89, 25))
        self.okButton.setObjectName("okButton")

        self.retranslateUi(messageList)
        QtCore.QMetaObject.connectSlotsByName(messageList)

    def retranslateUi(self, messageList):
        _translate = QtCore.QCoreApplication.translate
        messageList.setWindowTitle(_translate("messageList", "Message List"))
        self.ambulanceListLabel.setText(_translate("messageList", "Messages"))
        self.sendNewMessage.setText(_translate("messageList", "Send New Message"))
        self.okButton.setText(_translate("messageList", "close"))

