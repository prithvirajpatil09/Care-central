# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MessageDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_noticeDialog(object):
    def setupUi(self, noticeDialog):
        noticeDialog.setObjectName("noticeDialog")
        noticeDialog.resize(484, 235)
        self.broadcastMessages = QtWidgets.QPushButton(noticeDialog)
        self.broadcastMessages.setGeometry(QtCore.QRect(80, 10, 120, 120))
        self.broadcastMessages.setMaximumSize(QtCore.QSize(120, 120))
        self.broadcastMessages.setStyleSheet("border:none;")
        self.broadcastMessages.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Images/add_event.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.broadcastMessages.setIcon(icon)
        self.broadcastMessages.setIconSize(QtCore.QSize(100, 100))
        self.broadcastMessages.setObjectName("broadcastMessages")
        self.superadminMessage = QtWidgets.QPushButton(noticeDialog)
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
        self.broadcastMessageLabel = QtWidgets.QLabel(noticeDialog)
        self.broadcastMessageLabel.setGeometry(QtCore.QRect(60, 130, 161, 78))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.broadcastMessageLabel.sizePolicy().hasHeightForWidth())
        self.broadcastMessageLabel.setSizePolicy(sizePolicy)
        self.broadcastMessageLabel.setObjectName("broadcastMessageLabel")
        self.superadminMessageLabel = QtWidgets.QLabel(noticeDialog)
        self.superadminMessageLabel.setGeometry(QtCore.QRect(260, 130, 171, 78))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.superadminMessageLabel.sizePolicy().hasHeightForWidth())
        self.superadminMessageLabel.setSizePolicy(sizePolicy)
        self.superadminMessageLabel.setObjectName("superadminMessageLabel")

        self.retranslateUi(noticeDialog)
        QtCore.QMetaObject.connectSlotsByName(noticeDialog)

    def retranslateUi(self, noticeDialog):
        _translate = QtCore.QCoreApplication.translate
        noticeDialog.setWindowTitle(_translate("noticeDialog", "Messages"))
        self.broadcastMessageLabel.setText(_translate("noticeDialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; font-weight:600; text-decoration: underline;\">Broadcast</span></p><p align=\"center\"><span style=\" font-size:15pt; font-weight:600; text-decoration: underline;\">Messages</span></p></body></html>"))
        self.superadminMessageLabel.setText(_translate("noticeDialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; font-weight:600; text-decoration: underline;\">SuperAdmin</span></p><p align=\"center\"><span style=\" font-size:15pt; font-weight:600; text-decoration: underline;\">Messages</span></p></body></html>"))

