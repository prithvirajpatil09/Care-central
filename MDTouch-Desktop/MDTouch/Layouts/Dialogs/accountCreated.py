# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'accountCreated.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_accountInfo(object):
    def setupUi(self, accountInfo):
        accountInfo.setObjectName("accountInfo")
        accountInfo.resize(452, 272)
        accountInfo.setMinimumSize(QtCore.QSize(452, 272))
        accountInfo.setMaximumSize(QtCore.QSize(452, 272))
        self.usernameLabel = QtWidgets.QLabel(accountInfo)
        self.usernameLabel.setGeometry(QtCore.QRect(20, 140, 141, 41))
        self.usernameLabel.setObjectName("usernameLabel")
        self.passwordLabel = QtWidgets.QLabel(accountInfo)
        self.passwordLabel.setGeometry(QtCore.QRect(20, 190, 131, 31))
        self.passwordLabel.setObjectName("passwordLabel")
        self.IDLabel = QtWidgets.QLabel(accountInfo)
        self.IDLabel.setGeometry(QtCore.QRect(20, 90, 91, 41))
        self.IDLabel.setObjectName("IDLabel")
        self.ID = QtWidgets.QLabel(accountInfo)
        self.ID.setGeometry(QtCore.QRect(170, 90, 121, 41))
        self.ID.setStyleSheet("font-size:12pt;")
        self.ID.setObjectName("ID")
        self.username = QtWidgets.QLabel(accountInfo)
        self.username.setGeometry(QtCore.QRect(170, 140, 141, 41))
        self.username.setStyleSheet("font-size:12pt;")
        self.username.setObjectName("username")
        self.password = QtWidgets.QLabel(accountInfo)
        self.password.setGeometry(QtCore.QRect(170, 190, 141, 31))
        self.password.setStyleSheet("font-size:12pt;")
        self.password.setObjectName("password")
        self.frame = QtWidgets.QFrame(accountInfo)
        self.frame.setGeometry(QtCore.QRect(10, 10, 431, 80))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.notice1 = QtWidgets.QLabel(self.frame)
        self.notice1.setGeometry(QtCore.QRect(20, 10, 391, 61))
        self.notice1.setStyleSheet("")
        self.notice1.setObjectName("notice1")
        self.notice2 = QtWidgets.QLabel(accountInfo)
        self.notice2.setGeometry(QtCore.QRect(20, 230, 261, 41))
        self.notice2.setObjectName("notice2")
        self.OKButton = QtWidgets.QPushButton(accountInfo)
        self.OKButton.setGeometry(QtCore.QRect(340, 230, 80, 28))
        self.OKButton.setObjectName("OKButton")

        self.retranslateUi(accountInfo)
        QtCore.QMetaObject.connectSlotsByName(accountInfo)

    def retranslateUi(self, accountInfo):
        _translate = QtCore.QCoreApplication.translate
        accountInfo.setWindowTitle(_translate("accountInfo", "Account Created"))
        self.usernameLabel.setText(_translate("accountInfo", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">username :</span></p></body></html>"))
        self.passwordLabel.setText(_translate("accountInfo", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">password : </span></p></body></html>"))
        self.IDLabel.setText(_translate("accountInfo", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">ID : </span></p></body></html>"))
        self.ID.setText(_translate("accountInfo", "id"))
        self.username.setText(_translate("accountInfo", "username"))
        self.password.setText(_translate("accountInfo", "password"))
        self.notice1.setText(_translate("accountInfo", "<html><head/><body><p><span style=\" font-size:12pt; color:#00ff00;\">Account Created !!!</span><span style=\" font-size:12pt;\"><br/>Please send these details to the account holder</span></p></body></html>"))
        self.notice2.setText(_translate("accountInfo", "<html><head/><body><p>Click OK to view Account Profile</p></body></html>"))
        self.OKButton.setText(_translate("accountInfo", "OK"))

