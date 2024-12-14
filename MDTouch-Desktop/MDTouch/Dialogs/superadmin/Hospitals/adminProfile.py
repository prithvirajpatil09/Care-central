from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class adminProfile(object):
    def setup(self, adminProfile,data,hdata):
        adminProfile.setObjectName("adminProfile")
        adminProfile.resize(621, 411)
        self.frame = QtWidgets.QFrame(adminProfile)
        self.frame.setGeometry(QtCore.QRect(10, 20, 601, 341))
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
        self.pushButton = QtWidgets.QPushButton(adminProfile)
        self.pushButton.setGeometry(QtCore.QRect(520, 370, 80, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(adminProfile,data,hdata)
        QtCore.QMetaObject.connectSlotsByName(adminProfile)

    def retranslateUi(self, adminProfile,data,hdata):
        _translate = QtCore.QCoreApplication.translate
        adminProfile.setWindowTitle(_translate("adminProfile", "Admin Profile"))
        self.firstNameLabel.setText(_translate("adminProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">First Name : </span></p></body></html>"))
        self.lastNameLabel.setText(_translate("adminProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Last Name : </span></p></body></html>"))
        self.stateLabel.setText(_translate("adminProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">State : </span></p></body></html>"))
        self.cityLabel.setText(_translate("adminProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">City : </span></p></body></html>"))
        self.hospitalLabel.setText(_translate("adminProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Hospital : </span></p></body></html>"))
        self.firstName.setText(_translate("adminProfile", "first_name"))
        self.lastName.setText(_translate("adminProfile", "last_name"))
        self.state.setText(_translate("adminProfile", "state"))
        self.city.setText(_translate("adminProfile", "city"))
        self.hospital.setText(_translate("adminProfile", "hospital"))
        self.pushButton.setText(_translate("adminProfile", "OK"))

        self.events(adminProfile,data,hdata)

    def events(self,parent,data,hdata):
        self.firstName.setText(data["firstName"])
        self.lastName.setText(data["lastName"])
        self.city.setText(hdata["city"])
        self.state.setText(hdata["state"])
        self.hospital.setText(hdata["name"] + "," + hdata["city"])

        self.pushButton.clicked.connect(lambda: parent.close())