# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'changePassword.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_changePassword(object):
    def setupUi(self, changePassword):
        changePassword.setObjectName("changePassword")
        changePassword.resize(400, 248)
        self.pushButton = QtWidgets.QPushButton(changePassword)
        self.pushButton.setGeometry(QtCore.QRect(230, 200, 151, 28))
        self.pushButton.setObjectName("pushButton")
        self.oldPasswordLabel = QtWidgets.QLabel(changePassword)
        self.oldPasswordLabel.setGeometry(QtCore.QRect(10, 30, 151, 31))
        self.oldPasswordLabel.setObjectName("oldPasswordLabel")
        self.newPasswordLabel = QtWidgets.QLabel(changePassword)
        self.newPasswordLabel.setGeometry(QtCore.QRect(10, 90, 201, 31))
        self.newPasswordLabel.setObjectName("newPasswordLabel")
        self._newPassword_Label = QtWidgets.QLabel(changePassword)
        self._newPassword_Label.setGeometry(QtCore.QRect(10, 150, 251, 31))
        self._newPassword_Label.setObjectName("_newPassword_Label")
        self.oldPassword = QtWidgets.QLineEdit(changePassword)
        self.oldPassword.setGeometry(QtCore.QRect(220, 30, 171, 27))
        self.oldPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.oldPassword.setObjectName("oldPassword")
        self.newPassword = QtWidgets.QLineEdit(changePassword)
        self.newPassword.setGeometry(QtCore.QRect(220, 90, 171, 27))
        self.newPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newPassword.setObjectName("newPassword")
        self._newPassword = QtWidgets.QLineEdit(changePassword)
        self._newPassword.setGeometry(QtCore.QRect(220, 150, 171, 27))
        self._newPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self._newPassword.setObjectName("_newPassword")

        self.retranslateUi(changePassword)
        QtCore.QMetaObject.connectSlotsByName(changePassword)

    def retranslateUi(self, changePassword):
        _translate = QtCore.QCoreApplication.translate
        changePassword.setWindowTitle(_translate("changePassword", "Change Password"))
        self.pushButton.setText(_translate("changePassword", "Change Password"))
        self.oldPasswordLabel.setText(_translate("changePassword", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Old password : </span></p></body></html>"))
        self.newPasswordLabel.setText(_translate("changePassword", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Enter new password : </span></p></body></html>"))
        self._newPassword_Label.setText(_translate("changePassword", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Reenter new password : </span></p></body></html>"))

