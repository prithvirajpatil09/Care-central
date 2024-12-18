from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from Dialogs.messageBox import *

class removeHospital(object):
    def setup(self, removeHospital,hdata):
        removeHospital.setObjectName("removeHospital")
        removeHospital.resize(462, 454)
        self.removeButton = QtWidgets.QPushButton(removeHospital)
        self.removeButton.setGeometry(QtCore.QRect(160, 400, 131, 41))
        self.removeButton.setObjectName("removeButton")
        self.frame = QtWidgets.QFrame(removeHospital)
        self.frame.setGeometry(QtCore.QRect(10, 50, 442, 340))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.nameLabel = QtWidgets.QLabel(self.frame)
        self.nameLabel.setGeometry(QtCore.QRect(25, 30, 101, 41))
        self.nameLabel.setObjectName("nameLabel")
        self.addressLabel = QtWidgets.QLabel(self.frame)
        self.addressLabel.setGeometry(QtCore.QRect(25, 80, 101, 41))
        self.addressLabel.setObjectName("addressLabel")
        self.contactLabel = QtWidgets.QLabel(self.frame)
        self.contactLabel.setGeometry(QtCore.QRect(25, 290, 131, 21))
        self.contactLabel.setObjectName("contactLabel")
        self.stateLabel = QtWidgets.QLabel(self.frame)
        self.stateLabel.setGeometry(QtCore.QRect(25, 200, 101, 41))
        self.stateLabel.setObjectName("stateLabel")
        self.pinCodeLabel = QtWidgets.QLabel(self.frame)
        self.pinCodeLabel.setGeometry(QtCore.QRect(25, 160, 101, 41))
        self.pinCodeLabel.setObjectName("pinCodeLabel")
        self.cityLabel = QtWidgets.QLabel(self.frame)
        self.cityLabel.setGeometry(QtCore.QRect(25, 240, 101, 41))
        self.cityLabel.setObjectName("cityLabel")
        self.address = QtWidgets.QTextBrowser(self.frame)
        self.address.setGeometry(QtCore.QRect(150, 80, 271, 61))
        self.address.setStyleSheet("background-color:transparent;\n"
"border:none;")
        self.address.setObjectName("address")
        self.pinCode = QtWidgets.QLabel(self.frame)
        self.pinCode.setGeometry(QtCore.QRect(150, 170, 181, 21))
        self.pinCode.setStyleSheet("font-size:12pt;")
        self.pinCode.setObjectName("pinCode")
        self.state = QtWidgets.QLabel(self.frame)
        self.state.setGeometry(QtCore.QRect(150, 210, 181, 21))
        self.state.setStyleSheet("font-size:12pt;")
        self.state.setObjectName("state")
        self.city = QtWidgets.QLabel(self.frame)
        self.city.setGeometry(QtCore.QRect(150, 250, 181, 21))
        self.city.setStyleSheet("font-size:12pt;")
        self.city.setObjectName("city")
        self.contact = QtWidgets.QLabel(self.frame)
        self.contact.setGeometry(QtCore.QRect(150, 290, 191, 21))
        self.contact.setStyleSheet("font-size:12pt;")
        self.contact.setObjectName("contact")
        self.name = QtWidgets.QLabel(self.frame)
        self.name.setGeometry(QtCore.QRect(150, 30, 371, 41))
        self.name.setStyleSheet("font-size:12pt;")
        self.name.setObjectName("name")
        self.IDLabel = QtWidgets.QLabel(self.frame)
        self.IDLabel.setGeometry(QtCore.QRect(25, 0, 131, 41))
        self.IDLabel.setObjectName("IDLabel")
        self.dispensaryID = QtWidgets.QLabel(self.frame)
        self.dispensaryID.setGeometry(QtCore.QRect(150, 0, 371, 41))
        self.dispensaryID.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.dispensaryID.setObjectName("dispensaryID")
        self.title = QtWidgets.QLabel(removeHospital)
        self.title.setGeometry(QtCore.QRect(70, 0, 320, 50))
        self.title.setObjectName("title")

        self.retranslateUi(removeHospital,hdata)
        QtCore.QMetaObject.connectSlotsByName(removeHospital)

    def retranslateUi(self, removeHospital,hdata):
        _translate = QtCore.QCoreApplication.translate
        removeHospital.setWindowTitle(_translate("removeHospital", "removeHospital"))
        self.removeButton.setText(_translate("removeHospital", "REMOVE"))
        self.nameLabel.setText(_translate("removeHospital", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Name :</span></p></body></html>"))
        self.addressLabel.setText(_translate("removeHospital", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Address :</span></p></body></html>"))
        self.contactLabel.setText(_translate("removeHospital", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Contact No. :</span></p></body></html>"))
        self.stateLabel.setText(_translate("removeHospital", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">State :</span></p></body></html>"))
        self.pinCodeLabel.setText(_translate("removeHospital", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Pin Code :</span></p></body></html>"))
        self.cityLabel.setText(_translate("removeHospital", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">City :</span></p></body></html>"))
        self.address.setPlaceholderText(_translate("removeHospital", "Street, Landmark, Area"))
        self.pinCode.setText(_translate("removeHospital", "PinCode"))
        self.state.setText(_translate("removeHospital", "State"))
        self.city.setText(_translate("removeHospital", "City"))
        self.contact.setText(_translate("removeHospital", "1234567890"))
        self.name.setText(_translate("removeHospital", "Name"))
        self.IDLabel.setText(_translate("removeHospital", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">ID :</span></p></body></html>"))
        self.dispensaryID.setText(_translate("removeHospital", "HospitalID"))
        self.title.setText(_translate("removeHospital", "<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; font-weight:600; text-decoration: underline;\">Remove Hospital</span></p></body></html>"))

        self.clickEvents(removeHospital,hdata)
        
    def clickEvents(self, parent,hdata):
        self.dispensaryID.setText(str(hdata["id"]))
        self.state.setText(hdata["state"])
        self.city.setText(hdata["city"])
        self.name.setText(hdata["name"])
        self.address.setText(hdata["address"])
        self.contact.setText(str(hdata["contact"]))
        self.pinCode.setText(str(hdata["pin"]))
        self.removeButton.clicked.connect(lambda: self.clickOnRemoveButton(parent,hdata))

    def clickOnRemoveButton(self, parent,hdata):
        parent.close()
        self.window = messageBox()
        self.window.infoBox("Hospital with ID : " + str(hdata["id"]) + " is deleted.")

        # Deleting Hospital
        import requests
        URL = "http://127.0.0.1:8000/MDTouch/api/hospital/" + str(hdata["id"])
        r = requests.delete(url=URL)
        print(r)

