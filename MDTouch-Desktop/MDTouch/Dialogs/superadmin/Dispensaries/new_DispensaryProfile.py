
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class new_dispensaryProfile(object):
    def setup(self, dispensaryProfile,userdata):
        self.userdata = userdata
        dispensaryProfile.setObjectName("dispensaryProfile")
        dispensaryProfile.resize(553, 490)
        self.frame = QtWidgets.QFrame(dispensaryProfile)
        self.frame.setGeometry(QtCore.QRect(10, 10, 531, 431))
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
        self.contactLabel.setGeometry(QtCore.QRect(25, 240, 131, 41))
        self.contactLabel.setObjectName("contactLabel")
        self.stateLabel = QtWidgets.QLabel(self.frame)
        self.stateLabel.setGeometry(QtCore.QRect(295, 200, 101, 41))
        self.stateLabel.setObjectName("stateLabel")
        self.pinCodeLabel = QtWidgets.QLabel(self.frame)
        self.pinCodeLabel.setGeometry(QtCore.QRect(25, 160, 101, 41))
        self.pinCodeLabel.setObjectName("pinCodeLabel")
        self.cityLabel = QtWidgets.QLabel(self.frame)
        self.cityLabel.setGeometry(QtCore.QRect(25, 200, 101, 41))
        self.cityLabel.setObjectName("cityLabel")
        self.address = QtWidgets.QTextBrowser(self.frame)
        self.address.setGeometry(QtCore.QRect(150, 80, 371, 61))
        self.address.setStyleSheet("background-color:transparent;\n"
"border:none;")
        self.address.setObjectName("address")
        self.pinCode = QtWidgets.QLabel(self.frame)
        self.pinCode.setGeometry(QtCore.QRect(150, 170, 181, 21))
        self.pinCode.setStyleSheet("font-size:12pt;")
        self.pinCode.setObjectName("pinCode")
        self.state = QtWidgets.QLabel(self.frame)
        self.state.setGeometry(QtCore.QRect(350, 210, 181, 21))
        self.state.setStyleSheet("font-size:12pt;")
        self.state.setObjectName("state")
        self.city = QtWidgets.QLabel(self.frame)
        self.city.setGeometry(QtCore.QRect(90, 210, 181, 21))
        self.city.setStyleSheet("font-size:12pt;")
        self.city.setObjectName("city")
        self.contact = QtWidgets.QLabel(self.frame)
        self.contact.setGeometry(QtCore.QRect(150, 250, 181, 21))
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
        self.seeMedicineLabel = QtWidgets.QLabel(self.frame)
        self.seeMedicineLabel.setGeometry(QtCore.QRect(30, 285, 191, 41))
        self.seeMedicineLabel.setObjectName("seeMedicineLabel")
        self.billingRecordsLabel = QtWidgets.QLabel(self.frame)
        self.billingRecordsLabel.setGeometry(QtCore.QRect(30, 330, 191, 31))
        self.billingRecordsLabel.setObjectName("billingRecordsLabel")
        self.eventsOrganizedLabel = QtWidgets.QLabel(self.frame)
        self.eventsOrganizedLabel.setGeometry(QtCore.QRect(30, 370, 191, 31))
        self.eventsOrganizedLabel.setObjectName("eventsOrganizedLabel")
        self.seeMedicine = QtWidgets.QPushButton(self.frame)
        self.seeMedicine.setGeometry(QtCore.QRect(230, 290, 111, 28))
        self.seeMedicine.setStyleSheet("text-decoration:underline;\n"
"color:blue;\n"
"border:none;")
        self.seeMedicine.setObjectName("seeMedicine")
        self.billingRecords = QtWidgets.QPushButton(self.frame)
        self.billingRecords.setGeometry(QtCore.QRect(230, 330, 111, 28))
        self.billingRecords.setStyleSheet("text-decoration:underline;\n"
"color:blue;\n"
"border:none;")
        self.billingRecords.setObjectName("billingRecords")
        self.eventsOrganized = QtWidgets.QPushButton(self.frame)
        self.eventsOrganized.setGeometry(QtCore.QRect(230, 370, 111, 28))
        self.eventsOrganized.setStyleSheet("text-decoration:underline;\n"
"color:blue;\n"
"border:none;")
        self.eventsOrganized.setObjectName("eventsOrganized")
        self.pushButton = QtWidgets.QPushButton(dispensaryProfile)
        self.pushButton.setGeometry(QtCore.QRect(450, 450, 80, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(dispensaryProfile)
        QtCore.QMetaObject.connectSlotsByName(dispensaryProfile)

    def retranslateUi(self, dispensaryProfile):
        _translate = QtCore.QCoreApplication.translate
        dispensaryProfile.setWindowTitle(_translate("dispensaryProfile", "Dispensary Profile"))
        self.nameLabel.setText(_translate("dispensaryProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Name :</span></p></body></html>"))
        self.addressLabel.setText(_translate("dispensaryProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Address :</span></p></body></html>"))
        self.contactLabel.setText(_translate("dispensaryProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Contact No. :</span></p></body></html>"))
        self.stateLabel.setText(_translate("dispensaryProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">State :</span></p></body></html>"))
        self.pinCodeLabel.setText(_translate("dispensaryProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Pin Code :</span></p></body></html>"))
        self.cityLabel.setText(_translate("dispensaryProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">City :</span></p></body></html>"))
        self.address.setPlaceholderText(_translate("dispensaryProfile", "Street, Landmark, Area"))
        self.pinCode.setText(_translate("dispensaryProfile", "PinCode"))
        self.state.setText(_translate("dispensaryProfile", "State"))
        self.city.setText(_translate("dispensaryProfile", "City"))
        self.contact.setText(_translate("dispensaryProfile", "1234567890"))
        self.name.setText(_translate("dispensaryProfile", "Name"))
        self.IDLabel.setText(_translate("dispensaryProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">ID :</span></p></body></html>"))
        self.dispensaryID.setText(_translate("dispensaryProfile", "DispensaryID"))
        self.seeMedicineLabel.setText(_translate("dispensaryProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">See Medicines :</span></p></body></html>"))
        self.billingRecordsLabel.setText(_translate("dispensaryProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Billing Records :</span></p></body></html>"))
        self.eventsOrganizedLabel.setText(_translate("dispensaryProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Events Orgranized :</span></p></body></html>"))
        self.seeMedicine.setText(_translate("dispensaryProfile", "Check Here"))
        self.billingRecords.setText(_translate("dispensaryProfile", "Check Here"))
        self.eventsOrganized.setText(_translate("dispensaryProfile", "Check Here"))
        self.pushButton.setText(_translate("dispensaryProfile", "OK"))

        self.events(dispensaryProfile)

    def events(self,parent):
        data = self.userdata
        self.address.setText(str(data["address"]))
        self.dispensaryID.setText(str(data["id"]))
        self.pinCode.setText(str(data["pin"]))
        self.state.setText(str(data["state"]))
        self.city.setText(str(data["city"]))
        self.contact.setText(str("Nil"))
        self.name.setText(data["name"])

        self.pushButton.clicked.connect(lambda: parent.close())


