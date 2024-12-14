from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Data.States import *

class removeDoctor(object):
    def setup(self, removeDoctor):
        removeDoctor.setObjectName("removeDoctor")
        removeDoctor.resize(722, 450)
        removeDoctor.setWindowTitle("")
        self.title = QtWidgets.QLabel(removeDoctor)
        self.title.setGeometry(QtCore.QRect(200, 0, 331, 51))
        self.title.setObjectName("title")
        self.removeButton = QtWidgets.QPushButton(removeDoctor)
        self.removeButton.setGeometry(QtCore.QRect(300, 410, 131, 28))
        self.removeButton.setObjectName("removeButton")
        self.frame = QtWidgets.QFrame(removeDoctor)
        self.frame.setGeometry(QtCore.QRect(10, 60, 701, 341))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.firstNameLabel = QtWidgets.QLabel(self.frame)
        self.firstNameLabel.setGeometry(QtCore.QRect(30, 50, 101, 41))
        self.firstNameLabel.setObjectName("firstNameLabel")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(60, 110, 221, 201))
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet("image: url(:/doctor_icon.png);\n"
"border-style:solid;\n"
"border-width:1px;\n"
"border-color: rgb(0, 0, 0);")
        self.widget.setObjectName("widget")
        self.lastNameLabel = QtWidgets.QLabel(self.frame)
        self.lastNameLabel.setGeometry(QtCore.QRect(350, 50, 101, 41))
        self.lastNameLabel.setObjectName("lastNameLabel")
        self.stateLabel = QtWidgets.QLabel(self.frame)
        self.stateLabel.setGeometry(QtCore.QRect(350, 120, 111, 31))
        self.stateLabel.setObjectName("stateLabel")
        self.cityLabel = QtWidgets.QLabel(self.frame)
        self.cityLabel.setGeometry(QtCore.QRect(350, 190, 111, 31))
        self.cityLabel.setObjectName("cityLabel")
        self.hospitalLabel = QtWidgets.QLabel(self.frame)
        self.hospitalLabel.setGeometry(QtCore.QRect(350, 270, 111, 31))
        self.hospitalLabel.setObjectName("hospitalLabel")
        self.firstName = QtWidgets.QLabel(self.frame)
        self.firstName.setGeometry(QtCore.QRect(140, 50, 211, 41))
        self.firstName.setStyleSheet("font-size:12pt;")
        self.firstName.setObjectName("firstName")
        self.lastName = QtWidgets.QLabel(self.frame)
        self.lastName.setGeometry(QtCore.QRect(460, 50, 211, 41))
        self.lastName.setStyleSheet("font-size:12pt;")
        self.lastName.setObjectName("lastName")
        self.state = QtWidgets.QLabel(self.frame)
        self.state.setGeometry(QtCore.QRect(460, 120, 201, 31))
        self.state.setStyleSheet("font-size:12pt;")
        self.state.setObjectName("state")
        self.city = QtWidgets.QLabel(self.frame)
        self.city.setGeometry(QtCore.QRect(460, 190, 201, 31))
        self.city.setStyleSheet("font-size:12pt;")
        self.city.setObjectName("city")
        self.hospital = QtWidgets.QLabel(self.frame)
        self.hospital.setGeometry(QtCore.QRect(460, 270, 201, 31))
        self.hospital.setStyleSheet("font-size:12pt;")
        self.hospital.setObjectName("hospital")
        self.doctorID = QtWidgets.QLabel(self.frame)
        self.doctorID.setGeometry(QtCore.QRect(140, 10, 211, 41))
        self.doctorID.setStyleSheet("font-size:12pt;\n"
"font-weight:bold;")
        self.doctorID.setObjectName("doctorID")
        self.IDLabel = QtWidgets.QLabel(self.frame)
        self.IDLabel.setGeometry(QtCore.QRect(30, 10, 101, 41))
        self.IDLabel.setObjectName("IDLabel")

        self.retranslateUi(removeDoctor)
        QtCore.QMetaObject.connectSlotsByName(removeDoctor)

    def retranslateUi(self, removeDoctor):
        _translate = QtCore.QCoreApplication.translate
        removeDoctor.setWindowTitle(_translate("removeDoctor", " "))
        self.title.setText(_translate("removeDoctor", "<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; font-weight:600; text-decoration: underline;\">Remove Doctor</span></p></body></html>"))
        self.removeButton.setText(_translate("removeDoctor", "REMOVE"))
        self.firstNameLabel.setText(_translate("removeDoctor", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">First Name : </span></p></body></html>"))
        self.lastNameLabel.setText(_translate("removeDoctor", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Last Name : </span></p></body></html>"))
        self.stateLabel.setText(_translate("removeDoctor", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">State : </span></p></body></html>"))
        self.cityLabel.setText(_translate("removeDoctor", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">City : </span></p></body></html>"))
        self.hospitalLabel.setText(_translate("removeDoctor", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Hospital : </span></p></body></html>"))
        self.firstName.setText(_translate("removeDoctor", "first_name"))
        self.lastName.setText(_translate("removeDoctor", "last_name"))
        self.state.setText(_translate("removeDoctor", "state_name"))
        self.city.setText(_translate("removeDoctor", "city_name"))
        self.hospital.setText(_translate("removeDoctor", "hospital_name"))
        self.doctorID.setText(_translate("removeDoctor", "DoctorID"))
        self.IDLabel.setText(_translate("removeDoctor", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Doctor ID :</span></p></body></html>"))

        self.clickEvents(removeDoctor)

    def clickEvents(self, parent):
        self.removeButton.clicked.connect(lambda: self.clickOnRemoveButon(parent))

    def clickOnRemoveButton(self, parent):
        pass
