# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'removeDoctor.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_selectDoctor(object):
    def setupUi(self, selectDoctor):
        selectDoctor.setObjectName("selectDoctor")
        selectDoctor.resize(722, 450)
        selectDoctor.setWindowTitle("")
        self.title = QtWidgets.QLabel(selectDoctor)
        self.title.setGeometry(QtCore.QRect(200, 0, 331, 51))
        self.title.setObjectName("title")
        self.selectButton = QtWidgets.QPushButton(selectDoctor)
        self.selectButton.setGeometry(QtCore.QRect(300, 410, 131, 28))
        self.selectButton.setObjectName("selectButton")
        self.frame = QtWidgets.QFrame(selectDoctor)
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

        self.retranslateUi(selectDoctor)
        QtCore.QMetaObject.connectSlotsByName(selectDoctor)

    def retranslateUi(self, selectDoctor):
        _translate = QtCore.QCoreApplication.translate
        self.title.setText(_translate("selectDoctor", "<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; font-weight:600; text-decoration: underline;\">Remove Doctor</span></p></body></html>"))
        self.selectButton.setText(_translate("selectDoctor", "REMOVE"))
        self.firstNameLabel.setText(_translate("selectDoctor", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">First Name : </span></p></body></html>"))
        self.lastNameLabel.setText(_translate("selectDoctor", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Last Name : </span></p></body></html>"))
        self.stateLabel.setText(_translate("selectDoctor", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">State : </span></p></body></html>"))
        self.cityLabel.setText(_translate("selectDoctor", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">City : </span></p></body></html>"))
        self.hospitalLabel.setText(_translate("selectDoctor", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Hospital : </span></p></body></html>"))
        self.firstName.setText(_translate("selectDoctor", "first_name"))
        self.lastName.setText(_translate("selectDoctor", "last_name"))
        self.state.setText(_translate("selectDoctor", "state_name"))
        self.city.setText(_translate("selectDoctor", "city_name"))
        self.hospital.setText(_translate("selectDoctor", "hospital_name"))
        self.doctorID.setText(_translate("selectDoctor", "DoctorID"))
        self.IDLabel.setText(_translate("selectDoctor", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Doctor ID :</span></p></body></html>"))

import img_rc
