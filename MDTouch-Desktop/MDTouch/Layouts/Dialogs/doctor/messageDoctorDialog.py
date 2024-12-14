# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'messageDoctorDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_messageDoctorDialog(object):
    def setupUi(self, messageDoctorDialog):
        messageDoctorDialog.setObjectName("messageDoctorDialog")
        messageDoctorDialog.resize(348, 228)
        self.doctorMessage = QtWidgets.QPushButton(messageDoctorDialog)
        self.doctorMessage.setGeometry(QtCore.QRect(40, 10, 120, 120))
        self.doctorMessage.setMaximumSize(QtCore.QSize(120, 120))
        self.doctorMessage.setStyleSheet("border:none;")
        self.doctorMessage.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../Images/write_bill.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.doctorMessage.setIcon(icon)
        self.doctorMessage.setIconSize(QtCore.QSize(100, 100))
        self.doctorMessage.setObjectName("doctorMessage")
        self.broadcastMessage = QtWidgets.QPushButton(messageDoctorDialog)
        self.broadcastMessage.setGeometry(QtCore.QRect(190, 20, 120, 120))
        self.broadcastMessage.setMaximumSize(QtCore.QSize(120, 120))
        self.broadcastMessage.setStyleSheet("border:none;")
        self.broadcastMessage.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../Images/search_prescription.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.broadcastMessage.setIcon(icon1)
        self.broadcastMessage.setIconSize(QtCore.QSize(100, 100))
        self.broadcastMessage.setObjectName("broadcastMessage")
        self.doctorMessageLabel = QtWidgets.QLabel(messageDoctorDialog)
        self.doctorMessageLabel.setGeometry(QtCore.QRect(0, 130, 180, 80))
        self.doctorMessageLabel.setMinimumSize(QtCore.QSize(180, 80))
        self.doctorMessageLabel.setMaximumSize(QtCore.QSize(180, 40))
        self.doctorMessageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.doctorMessageLabel.setObjectName("doctorMessageLabel")
        self.broadcastMessageLabel = QtWidgets.QLabel(messageDoctorDialog)
        self.broadcastMessageLabel.setGeometry(QtCore.QRect(160, 130, 180, 80))
        self.broadcastMessageLabel.setMinimumSize(QtCore.QSize(180, 80))
        self.broadcastMessageLabel.setMaximumSize(QtCore.QSize(180, 40))
        self.broadcastMessageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.broadcastMessageLabel.setObjectName("broadcastMessageLabel")

        self.retranslateUi(messageDoctorDialog)
        QtCore.QMetaObject.connectSlotsByName(messageDoctorDialog)

    def retranslateUi(self, messageDoctorDialog):
        _translate = QtCore.QCoreApplication.translate
        messageDoctorDialog.setWindowTitle(_translate("messageDoctorDialog", "Messages"))
        self.doctorMessageLabel.setText(_translate("messageDoctorDialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">Doctors</span></p><p><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">Message</span></p></body></html>"))
        self.broadcastMessageLabel.setText(_translate("messageDoctorDialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">Broadcast</span></p><p><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">Messages</span></p></body></html>"))

