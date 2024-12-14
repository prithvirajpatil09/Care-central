from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Data.States import *
from Dialogs.messageBox import *

class deleteAdmin(object):
    def setup(self, deleteAdmin,adminData,hdata):
        deleteAdmin.setObjectName("deleteAdmin")
        deleteAdmin.resize(622, 455)
        deleteAdmin.setWindowTitle("")
        self.title = QtWidgets.QLabel(deleteAdmin)
        self.title.setGeometry(QtCore.QRect(181, 0, 260, 50))
        self.title.setObjectName("title")
        self.frame = QtWidgets.QFrame(deleteAdmin)
        self.frame.setGeometry(QtCore.QRect(10, 60, 601, 341))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.firstNameLabel = QtWidgets.QLabel(self.frame)
        self.firstNameLabel.setGeometry(QtCore.QRect(30, 20, 101, 41))
        self.firstNameLabel.setObjectName("firstNameLabel")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(60, 80, 221, 201))
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet("image: url(:/adminPic.png);\n"
"border-style:solid;\n"
"border-width:1px;\n"
"border-color: rgb(0, 0, 0);")
        self.widget.setObjectName("widget")
        self.lastNameLabel = QtWidgets.QLabel(self.frame)
        self.lastNameLabel.setGeometry(QtCore.QRect(350, 20, 101, 41))
        self.lastNameLabel.setObjectName("lastNameLabel")
        self.stateLabel = QtWidgets.QLabel(self.frame)
        self.stateLabel.setGeometry(QtCore.QRect(350, 90, 111, 31))
        self.stateLabel.setObjectName("stateLabel")
        self.cityLabel = QtWidgets.QLabel(self.frame)
        self.cityLabel.setGeometry(QtCore.QRect(350, 160, 111, 31))
        self.cityLabel.setObjectName("cityLabel")
        self.hospitalLabel = QtWidgets.QLabel(self.frame)
        self.hospitalLabel.setGeometry(QtCore.QRect(350, 240, 111, 31))
        self.hospitalLabel.setObjectName("hospitalLabel")
        self.firstName = QtWidgets.QLabel(self.frame)
        self.firstName.setGeometry(QtCore.QRect(140, 20, 171, 41))
        self.firstName.setStyleSheet("font-size:12pt;")
        self.firstName.setObjectName("firstName")
        self.lastName = QtWidgets.QLabel(self.frame)
        self.lastName.setGeometry(QtCore.QRect(460, 20, 211, 41))
        self.lastName.setStyleSheet("font-size:12pt;")
        self.lastName.setObjectName("lastName")
        self.state = QtWidgets.QLabel(self.frame)
        self.state.setGeometry(QtCore.QRect(460, 90, 211, 31))
        self.state.setStyleSheet("font-size:12pt;")
        self.state.setObjectName("state")
        self.city = QtWidgets.QLabel(self.frame)
        self.city.setGeometry(QtCore.QRect(460, 160, 211, 31))
        self.city.setStyleSheet("font-size:12pt;")
        self.city.setObjectName("city")
        self.hospital = QtWidgets.QLabel(self.frame)
        self.hospital.setGeometry(QtCore.QRect(460, 240, 211, 31))
        self.hospital.setStyleSheet("font-size:12pt;")
        self.hospital.setObjectName("hospital")
        self.deleteAdmin = QtWidgets.QPushButton(deleteAdmin)
        self.deleteAdmin.setGeometry(QtCore.QRect(270, 410, 81, 31))
        self.deleteAdmin.setObjectName("deleteAdmin")

        self.retranslateUi(deleteAdmin,adminData,hdata)
        QtCore.QMetaObject.connectSlotsByName(deleteAdmin)

    def retranslateUi(self, deleteAdmin,adminData,hdata):
        _translate = QtCore.QCoreApplication.translate
        deleteAdmin.setWindowTitle(_translate("deleteAdmin", " "))
        self.title.setText(_translate("deleteAdmin", "<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; font-weight:600; text-decoration: underline;\">Delete Admin</span></p></body></html>"))
        self.firstNameLabel.setText(_translate("deleteAdmin", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">First Name : </span></p></body></html>"))
        self.lastNameLabel.setText(_translate("deleteAdmin", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Last Name : </span></p></body></html>"))
        self.stateLabel.setText(_translate("deleteAdmin", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">State : </span></p></body></html>"))
        self.cityLabel.setText(_translate("deleteAdmin", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">City : </span></p></body></html>"))
        self.hospitalLabel.setText(_translate("deleteAdmin", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Hospital : </span></p></body></html>"))
        self.firstName.setText(_translate("deleteAdmin", "first_name"))
        self.lastName.setText(_translate("deleteAdmin", "last_name"))
        self.state.setText(_translate("deleteAdmin", "state"))
        self.city.setText(_translate("deleteAdmin", "city"))
        self.hospital.setText(_translate("deleteAdmin", "hospital"))
        self.deleteAdmin.setText(_translate("deleteAdmin", "DELETE"))

        self.clickEvents(deleteAdmin,adminData,hdata)

    def clickEvents(self,parent,adminData,hdata):

        self.firstName.setText(str(adminData["firstName"]))
        self.lastName.setText(str(adminData["lastName"]))
        self.state.setText(str(hdata["state"]))
        self.hospital.setText(str(hdata["name"]))
        self.city.setText(str(hdata["city"]))
        self.deleteAdmin.clicked.connect(lambda : self.clickOnDelete(parent,adminData,hdata))
    def clickOnDelete(self, parent,adminData,hdata):
        parent.close()
        self.window = messageBox()
        self.window.infoBox("Hospital with ID : " + str(hdata["id"]) + " is deleted.")

        # Deleting Hospital
        import requests
        URL = "http://127.0.0.1:8000/MDTouch/api/login/" + str(adminData["username"])
        r = requests.delete(url=URL)
        print(r)
        

