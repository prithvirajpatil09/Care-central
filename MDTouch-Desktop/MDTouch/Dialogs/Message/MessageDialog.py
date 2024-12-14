from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Dialogs.Message.messageList import *
from Dialogs.Message.broadcastList import *

class messageDialog(object):
    def setup(self, messageDialog,userdata):
        self.userdata = userdata
        messageDialog.setObjectName("messageDialog")
        messageDialog.resize(484, 235)
        self.broadcastMessages = QtWidgets.QPushButton(messageDialog)
        self.broadcastMessages.setGeometry(QtCore.QRect(80, 10, 120, 120))
        self.broadcastMessages.setMaximumSize(QtCore.QSize(120, 120))
        self.broadcastMessages.setStyleSheet("border:none;")
        self.broadcastMessages.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Images/add_event.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.broadcastMessages.setIcon(icon)
        self.broadcastMessages.setIconSize(QtCore.QSize(100, 100))
        self.broadcastMessages.setObjectName("broadcastMessages")
        self.superadminMessage = QtWidgets.QPushButton(messageDialog)
        self.superadminMessage.setGeometry(QtCore.QRect(280, 10, 120, 120))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.superadminMessage.sizePolicy().hasHeightForWidth())
        self.superadminMessage.setSizePolicy(sizePolicy)
        self.superadminMessage.setMaximumSize(QtCore.QSize(120, 120))
        self.superadminMessage.setStyleSheet("border:none;")
        self.superadminMessage.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../Images/search_hospital.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.superadminMessage.setIcon(icon1)
        self.superadminMessage.setIconSize(QtCore.QSize(100, 100))
        self.superadminMessage.setObjectName("superadminMessage")
        self.broadcastMessageLabel = QtWidgets.QLabel(messageDialog)
        self.broadcastMessageLabel.setGeometry(QtCore.QRect(60, 130, 161, 78))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.broadcastMessageLabel.sizePolicy().hasHeightForWidth())
        self.broadcastMessageLabel.setSizePolicy(sizePolicy)
        self.broadcastMessageLabel.setObjectName("broadcastMessageLabel")
        self.superadminMessageLabel = QtWidgets.QLabel(messageDialog)
        self.superadminMessageLabel.setGeometry(QtCore.QRect(260, 130, 171, 78))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.superadminMessageLabel.sizePolicy().hasHeightForWidth())
        self.superadminMessageLabel.setSizePolicy(sizePolicy)
        self.superadminMessageLabel.setObjectName("superadminMessageLabel")

        self.retranslateUi(messageDialog)
        QtCore.QMetaObject.connectSlotsByName(messageDialog)

    def retranslateUi(self, messageDialog):
        _translate = QtCore.QCoreApplication.translate
        messageDialog.setWindowTitle(_translate("messageDialog", "Messages"))
        self.broadcastMessageLabel.setText(_translate("messageDialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; font-weight:600; text-decoration: underline;\">Broadcast</span></p><p align=\"center\"><span style=\" font-size:15pt; font-weight:600; text-decoration: underline;\">Messages</span></p></body></html>"))
        self.superadminMessageLabel.setText(_translate("messageDialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; font-weight:600; text-decoration: underline;\">SuperAdmin</span></p><p align=\"center\"><span style=\" font-size:15pt; font-weight:600; text-decoration: underline;\">Messages</span></p></body></html>"))
        self.events(messageDialog)

    def events(self,parent):
        self.broadcastMessages.clicked.connect(lambda : self.clickOnBroadCast(parent))
        self.superadminMessage.clicked.connect(lambda : self.clickOnSM(parent))

    def clickOnBroadCast(self,parent):
        self.window = QDialog()
        self.dialog = broadcastList()
        self.dialog.setup(self.window)
        self.window.setModal(True)
        self.window.show()
    def clickOnSM(self,parent):
        self.window = QDialog()
        self.dialog = messageList()
        self.dialog.setup(self.window,self.userdata)
        self.window.setModal(True)
        self.window.show()
