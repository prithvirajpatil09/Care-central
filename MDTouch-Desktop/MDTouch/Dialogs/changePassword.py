from PyQt5 import QtCore, QtGui, QtWidgets
from Dialogs.messageBox import *

class changePassword(object):
    def setup(self, changePassword,loginData,grandparent):
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

        self.retranslateUi(changePassword,loginData,grandparent)
        QtCore.QMetaObject.connectSlotsByName(changePassword)

    def retranslateUi(self, changePassword,loginData,grandparent):
        _translate = QtCore.QCoreApplication.translate
        changePassword.setWindowTitle(_translate("changePassword", "Change Password"))
        self.pushButton.setText(_translate("changePassword", "Change Password"))
        self.oldPasswordLabel.setText(_translate("changePassword", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Old password : </span></p></body></html>"))
        self.newPasswordLabel.setText(_translate("changePassword", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Enter new password : </span></p></body></html>"))
        self._newPassword_Label.setText(_translate("changePassword", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Reenter new password : </span></p></body></html>"))
        self.events(changePassword,loginData,grandparent)

    def events(self,parent,loginData,grandparent):
        self.pushButton.clicked.connect(lambda : self.clickOnButton(parent,loginData,grandparent))

    def clickOnButton(self,parent,loginData,grandparent):
        old_password = self.oldPassword.text()
        new_password = self.newPassword.text()
        _new_password = self._newPassword.text()
        if old_password != loginData["password"]:
            self.window = messageBox()
            self.window.warningBox("Old Password is Incorrect")
            return
        if new_password != _new_password:
            self.window = messageBox()
            self.window.warningBox("New Password Does not match")
            return
        import requests
        URL = "http://127.0.0.1:8000/MDTouch/api/login/" + str(loginData["id"])
        data = {
            "password" : new_password
        }
        r = requests.put(url=URL,data=data)
        print(r)
        print(r.json())
        grandparent.logindata = r.json()
        parent.close()
        self.window = messageBox()
        self.window.infoBox("Your Password has been changed")




