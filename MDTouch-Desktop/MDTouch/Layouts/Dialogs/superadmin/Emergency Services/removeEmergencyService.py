# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'removeEmergencyService.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_selectEmergencyService(object):
    def setupUi(self, selectEmergencyService):
        selectEmergencyService.setObjectName("selectEmergencyService")
        selectEmergencyService.resize(555, 453)
        selectEmergencyService.setWindowTitle("")
        self.frame = QtWidgets.QFrame(selectEmergencyService)
        self.frame.setGeometry(QtCore.QRect(10, 50, 531, 341))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.state = QtWidgets.QLabel(self.frame)
        self.state.setGeometry(QtCore.QRect(140, 220, 181, 21))
        self.state.setStyleSheet("font-size:12pt;")
        self.state.setObjectName("state")
        self.name = QtWidgets.QLabel(self.frame)
        self.name.setGeometry(QtCore.QRect(140, 40, 371, 41))
        self.name.setStyleSheet("font-size:12pt;")
        self.name.setObjectName("name")
        self.pinCode = QtWidgets.QLabel(self.frame)
        self.pinCode.setGeometry(QtCore.QRect(140, 180, 181, 21))
        self.pinCode.setStyleSheet("font-size:12pt;")
        self.pinCode.setObjectName("pinCode")
        self.stateLabel = QtWidgets.QLabel(self.frame)
        self.stateLabel.setGeometry(QtCore.QRect(15, 210, 101, 41))
        self.stateLabel.setObjectName("stateLabel")
        self.contact = QtWidgets.QLabel(self.frame)
        self.contact.setGeometry(QtCore.QRect(140, 300, 191, 21))
        self.contact.setStyleSheet("font-size:12pt;")
        self.contact.setObjectName("contact")
        self.cityLabel = QtWidgets.QLabel(self.frame)
        self.cityLabel.setGeometry(QtCore.QRect(15, 250, 101, 41))
        self.cityLabel.setObjectName("cityLabel")
        self.IDLabel = QtWidgets.QLabel(self.frame)
        self.IDLabel.setGeometry(QtCore.QRect(15, 10, 131, 41))
        self.IDLabel.setObjectName("IDLabel")
        self.nameLabel = QtWidgets.QLabel(self.frame)
        self.nameLabel.setGeometry(QtCore.QRect(15, 40, 101, 41))
        self.nameLabel.setObjectName("nameLabel")
        self.pinCodeLabel = QtWidgets.QLabel(self.frame)
        self.pinCodeLabel.setGeometry(QtCore.QRect(15, 170, 101, 41))
        self.pinCodeLabel.setObjectName("pinCodeLabel")
        self.contactLabel = QtWidgets.QLabel(self.frame)
        self.contactLabel.setGeometry(QtCore.QRect(15, 300, 131, 21))
        self.contactLabel.setObjectName("contactLabel")
        self.address = QtWidgets.QTextBrowser(self.frame)
        self.address.setGeometry(QtCore.QRect(140, 90, 371, 61))
        self.address.setStyleSheet("background-color:transparent;\n"
"border:none;")
        self.address.setObjectName("address")
        self.addressLabel = QtWidgets.QLabel(self.frame)
        self.addressLabel.setGeometry(QtCore.QRect(15, 90, 101, 41))
        self.addressLabel.setObjectName("addressLabel")
        self.city = QtWidgets.QLabel(self.frame)
        self.city.setGeometry(QtCore.QRect(140, 260, 181, 21))
        self.city.setStyleSheet("font-size:12pt;")
        self.city.setObjectName("city")
        self.dispensaryID = QtWidgets.QLabel(self.frame)
        self.dispensaryID.setGeometry(QtCore.QRect(140, 10, 371, 41))
        self.dispensaryID.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.dispensaryID.setObjectName("dispensaryID")
        self.addButton = QtWidgets.QPushButton(selectEmergencyService)
        self.addButton.setGeometry(QtCore.QRect(210, 400, 131, 41))
        self.addButton.setObjectName("addButton")
        self.title = QtWidgets.QLabel(selectEmergencyService)
        self.title.setGeometry(QtCore.QRect(40, 0, 451, 51))
        self.title.setObjectName("title")

        self.retranslateUi(selectEmergencyService)
        QtCore.QMetaObject.connectSlotsByName(selectEmergencyService)

    def retranslateUi(self, selectEmergencyService):
        _translate = QtCore.QCoreApplication.translate
        self.state.setText(_translate("selectEmergencyService", "State"))
        self.name.setText(_translate("selectEmergencyService", "Name"))
        self.pinCode.setText(_translate("selectEmergencyService", "PinCode"))
        self.stateLabel.setText(_translate("selectEmergencyService", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">State :</span></p></body></html>"))
        self.contact.setText(_translate("selectEmergencyService", "1234567890"))
        self.cityLabel.setText(_translate("selectEmergencyService", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">City :</span></p></body></html>"))
        self.IDLabel.setText(_translate("selectEmergencyService", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">ID :</span></p></body></html>"))
        self.nameLabel.setText(_translate("selectEmergencyService", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Name :</span></p></body></html>"))
        self.pinCodeLabel.setText(_translate("selectEmergencyService", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Pin Code :</span></p></body></html>"))
        self.contactLabel.setText(_translate("selectEmergencyService", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Contact No. :</span></p></body></html>"))
        self.address.setPlaceholderText(_translate("selectEmergencyService", "Street, Landmark, Area"))
        self.addressLabel.setText(_translate("selectEmergencyService", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Address :</span></p></body></html>"))
        self.city.setText(_translate("selectEmergencyService", "City"))
        self.dispensaryID.setText(_translate("selectEmergencyService", "EmergencyServiceID"))
        self.addButton.setText(_translate("selectEmergencyService", "REMOVE"))
        self.title.setText(_translate("selectEmergencyService", "<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; font-weight:600; text-decoration: underline;\">Remove Emergency Service</span></p></body></html>"))

