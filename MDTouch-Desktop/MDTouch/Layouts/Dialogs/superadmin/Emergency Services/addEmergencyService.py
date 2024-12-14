# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEmergencyService.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_addEmergencyService(object):
    def setupUi(self, addEmergencyService):
        addEmergencyService.setObjectName("addEmergencyService")
        addEmergencyService.resize(750, 480)
        addEmergencyService.setWindowTitle("")
        self.title = QtWidgets.QLabel(addEmergencyService)
        self.title.setGeometry(QtCore.QRect(220, 0, 371, 51))
        self.title.setObjectName("title")
        self.addButton = QtWidgets.QPushButton(addEmergencyService)
        self.addButton.setGeometry(QtCore.QRect(330, 420, 131, 41))
        self.addButton.setObjectName("addButton")
        self.frame = QtWidgets.QFrame(addEmergencyService)
        self.frame.setGeometry(QtCore.QRect(10, 60, 731, 341))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.nameLabel = QtWidgets.QLabel(self.frame)
        self.nameLabel.setGeometry(QtCore.QRect(25, 20, 71, 41))
        self.nameLabel.setObjectName("nameLabel")
        self.name = QtWidgets.QLineEdit(self.frame)
        self.name.setGeometry(QtCore.QRect(150, 20, 561, 41))
        self.name.setObjectName("name")
        self.addressLabel = QtWidgets.QLabel(self.frame)
        self.addressLabel.setGeometry(QtCore.QRect(25, 70, 91, 41))
        self.addressLabel.setObjectName("addressLabel")
        self.contactLabel = QtWidgets.QLabel(self.frame)
        self.contactLabel.setGeometry(QtCore.QRect(25, 280, 131, 41))
        self.contactLabel.setObjectName("contactLabel")
        self.stateLabel = QtWidgets.QLabel(self.frame)
        self.stateLabel.setGeometry(QtCore.QRect(25, 190, 61, 41))
        self.stateLabel.setObjectName("stateLabel")
        self.pinCodeLabel = QtWidgets.QLabel(self.frame)
        self.pinCodeLabel.setGeometry(QtCore.QRect(25, 150, 91, 41))
        self.pinCodeLabel.setObjectName("pinCodeLabel")
        self.cityLabel = QtWidgets.QLabel(self.frame)
        self.cityLabel.setGeometry(QtCore.QRect(25, 240, 61, 41))
        self.cityLabel.setObjectName("cityLabel")
        self.address = QtWidgets.QTextEdit(self.frame)
        self.address.setGeometry(QtCore.QRect(150, 70, 561, 75))
        self.address.setObjectName("address")
        self.pinCode = QtWidgets.QLineEdit(self.frame)
        self.pinCode.setGeometry(QtCore.QRect(150, 160, 181, 27))
        self.pinCode.setObjectName("pinCode")
        self.contact = QtWidgets.QLineEdit(self.frame)
        self.contact.setGeometry(QtCore.QRect(150, 290, 181, 27))
        self.contact.setInputMethodHints(QtCore.Qt.ImhNone)
        self.contact.setObjectName("contact")
        self.state = QtWidgets.QComboBox(self.frame)
        self.state.setGeometry(QtCore.QRect(150, 200, 181, 27))
        self.state.setObjectName("state")
        self.city = QtWidgets.QComboBox(self.frame)
        self.city.setGeometry(QtCore.QRect(150, 250, 181, 27))
        self.city.setObjectName("city")

        self.retranslateUi(addEmergencyService)
        QtCore.QMetaObject.connectSlotsByName(addEmergencyService)

    def retranslateUi(self, addEmergencyService):
        _translate = QtCore.QCoreApplication.translate
        self.title.setText(_translate("addEmergencyService", "<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; font-weight:600; text-decoration: underline;\">Add Emergency Service</span></p></body></html>"))
        self.addButton.setText(_translate("addEmergencyService", "ADD"))
        self.nameLabel.setText(_translate("addEmergencyService", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Name :</span></p></body></html>"))
        self.addressLabel.setText(_translate("addEmergencyService", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Address :</span></p></body></html>"))
        self.contactLabel.setText(_translate("addEmergencyService", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Contact No. :</span></p></body></html>"))
        self.stateLabel.setText(_translate("addEmergencyService", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">State :</span></p></body></html>"))
        self.pinCodeLabel.setText(_translate("addEmergencyService", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Pin Code :</span></p></body></html>"))
        self.cityLabel.setText(_translate("addEmergencyService", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">City :</span></p></body></html>"))

