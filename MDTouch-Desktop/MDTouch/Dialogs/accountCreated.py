from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Dialogs.superadmin.Hospitals.adminProfile import *
from Dialogs.superadmin.BloodBanks.bloodBankProfile import *
from Dialogs.superadmin.Doctors.doctorProfile import *
from Dialogs.superadmin.Dispensaries.dispensaryProfile import *
from Dialogs.superadmin.TestCenters.testCenterProfile import *
from Dialogs.superadmin.EmergencyServices.emergencyServiceProfile import *

class accountCreated(object):
    def setup(self, accountCreated,type,data,logindata,hospitalData = None):
        accountCreated.setObjectName("accountCreated")
        accountCreated.resize(452, 272)
        accountCreated.setMinimumSize(QtCore.QSize(452, 272))
        accountCreated.setMaximumSize(QtCore.QSize(452, 272))
        self.usernameLabel = QtWidgets.QLabel(accountCreated)
        self.usernameLabel.setGeometry(QtCore.QRect(20, 140, 141, 41))
        self.usernameLabel.setObjectName("usernameLabel")
        self.passwordLabel = QtWidgets.QLabel(accountCreated)
        self.passwordLabel.setGeometry(QtCore.QRect(20, 190, 131, 31))
        self.passwordLabel.setObjectName("passwordLabel")
        self.IDLabel = QtWidgets.QLabel(accountCreated)
        self.IDLabel.setGeometry(QtCore.QRect(20, 90, 91, 41))
        self.IDLabel.setObjectName("IDLabel")
        self.ID = QtWidgets.QLabel(accountCreated)
        self.ID.setGeometry(QtCore.QRect(170, 90, 121, 41))
        self.ID.setStyleSheet("font-size:12pt;")
        self.ID.setObjectName("ID")
        self.username = QtWidgets.QLabel(accountCreated)
        self.username.setGeometry(QtCore.QRect(170, 140, 141, 41))
        self.username.setStyleSheet("font-size:12pt;")
        self.username.setObjectName("username")
        self.password = QtWidgets.QLabel(accountCreated)
        self.password.setGeometry(QtCore.QRect(170, 190, 141, 31))
        self.password.setStyleSheet("font-size:12pt;")
        self.password.setObjectName("password")
        self.frame = QtWidgets.QFrame(accountCreated)
        self.frame.setGeometry(QtCore.QRect(10, 10, 431, 80))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.notice1 = QtWidgets.QLabel(self.frame)
        self.notice1.setGeometry(QtCore.QRect(20, 10, 391, 61))
        self.notice1.setStyleSheet("")
        self.notice1.setObjectName("notice1")
        self.notice2 = QtWidgets.QLabel(accountCreated)
        self.notice2.setGeometry(QtCore.QRect(20, 230, 261, 41))
        self.notice2.setObjectName("notice2")
        self.OKButton = QtWidgets.QPushButton(accountCreated)
        self.OKButton.setGeometry(QtCore.QRect(340, 230, 80, 28))
        self.OKButton.setObjectName("OKButton")

        self.retranslateUi(accountCreated,type,data,logindata,hospitalData)
        QtCore.QMetaObject.connectSlotsByName(accountCreated)

    def retranslateUi(self, accountCreated,type,data,logindata,hospitalData):
        _translate = QtCore.QCoreApplication.translate
        accountCreated.setWindowTitle(_translate("accountCreated", "Account Created"))
        self.usernameLabel.setText(_translate("accountCreated", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">username :</span></p></body></html>"))
        self.passwordLabel.setText(_translate("accountCreated", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">password : </span></p></body></html>"))
        self.IDLabel.setText(_translate("accountCreated", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">ID : </span></p></body></html>"))
        self.ID.setText(_translate("accountCreated", "id"))
        self.username.setText(_translate("accountCreated", "username"))
        self.password.setText(_translate("accountCreated", "password"))
        self.notice1.setText(_translate("accountCreated", "<html><head/><body><p><span style=\" font-size:12pt; color:#00ff00;\">Account Created !!!</span><span style=\" font-size:12pt;\"><br/>Please send these details to the account holder</span></p></body></html>"))
        self.notice2.setText(_translate("accountCreated", "<html><head/><body><p>Click OK to view Account Profile</p></body></html>"))
        self.OKButton.setText(_translate("accountCreated", "OK"))

        #self.inputEvents(accountCreated,data,logindata)
        self.clickEvents(accountCreated,type,data,logindata,hospitalData)

    def clickEvents(self, parent,type,data,logindata,hospitalData):
        self.OKButton.clicked.connect(lambda : self.inputEvents(parent,type,data,logindata,hospitalData))
        print(data)
        print(logindata)
        self.ID.setText(str(logindata["id"]))
        self.username.setText(str(logindata["username"]))
        self.password.setText(str(logindata["password"]))
        print(logindata)

    def inputEvents(self, parent,type,data,logindata,hospitalData):
        parent.close()
        if type == "Admin":
            self.window = QDialog()
            self.dialog = adminProfile()
            self.dialog.setup(self.window,data,hospitalData)
            self.window.setModal(True)
            self.window.show()
        elif type == "BloodBank":
            self.window = QDialog()
            self.dialog = bloodBankProfile()
            self.dialog.setup(self.window,data)
            self.window.setModal(True)
            self.window.show()
        elif type == "Disensary":
            self.window = QDialog()
            self.dialog = dispensaryProfile()
            self.dialog.setup(self.window,data)
            self.window.setModal(True)
            self.window.show()
        elif type == "ES":
            self.window = QDialog()
            self.dialog = emergencyServiceProfile()
            self.dialog.setup(self.window,data)
            self.window.setModal(True)
            self.window.show()
        elif type == "Doctor":
            self.window = QDialog()
            self.dialog = doctorProfile()
            self.dialog.setup(self.window,data,hospitalData)
            self.window.setModal(True)
            self.window.show()
        elif type == "TestCenter":
            self.window = QDialog()
            self.dialog = testCenterProfile()
            self.dialog.setup(self.window,data)
            self.window.setModal(True)
            self.window.show()


