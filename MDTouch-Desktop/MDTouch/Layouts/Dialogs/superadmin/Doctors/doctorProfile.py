# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'doctorProfile.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_doctorProfile(object):
    def setupUi(self, doctorProfile):
        doctorProfile.setObjectName("doctorProfile")
        doctorProfile.resize(723, 400)
        self.frame = QtWidgets.QFrame(doctorProfile)
        self.frame.setGeometry(QtCore.QRect(10, 20, 701, 331))
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
        self.doctorIDLabel = QtWidgets.QLabel(self.frame)
        self.doctorIDLabel.setGeometry(QtCore.QRect(30, 10, 101, 41))
        self.doctorIDLabel.setObjectName("doctorIDLabel")
        self.doctorID = QtWidgets.QLabel(self.frame)
        self.doctorID.setGeometry(QtCore.QRect(140, 10, 211, 41))
        self.doctorID.setStyleSheet("font-size:12pt;\n"
"font-weight:bold;")
        self.doctorID.setObjectName("doctorID")
        self.pushButton = QtWidgets.QPushButton(doctorProfile)
        self.pushButton.setGeometry(QtCore.QRect(620, 360, 80, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(doctorProfile)
        QtCore.QMetaObject.connectSlotsByName(doctorProfile)

    def retranslateUi(self, doctorProfile):
        _translate = QtCore.QCoreApplication.translate
        doctorProfile.setWindowTitle(_translate("doctorProfile", "Doctor Profile"))
        self.firstNameLabel.setText(_translate("doctorProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">First Name : </span></p></body></html>"))
        self.lastNameLabel.setText(_translate("doctorProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Last Name : </span></p></body></html>"))
        self.stateLabel.setText(_translate("doctorProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">State : </span></p></body></html>"))
        self.cityLabel.setText(_translate("doctorProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">City : </span></p></body></html>"))
        self.hospitalLabel.setText(_translate("doctorProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Hospital : </span></p></body></html>"))
        self.firstName.setText(_translate("doctorProfile", "first_name"))
        self.lastName.setText(_translate("doctorProfile", "last_name"))
        self.state.setText(_translate("doctorProfile", "state_name"))
        self.city.setText(_translate("doctorProfile", "city_name"))
        self.hospital.setText(_translate("doctorProfile", "hospital_name"))
        self.doctorIDLabel.setText(_translate("doctorProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Doctor ID :</span></p></body></html>"))
        self.doctorID.setText(_translate("doctorProfile", "Doctor ID"))
        self.pushButton.setText(_translate("doctorProfile", "OK"))

import img_rc
