from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Dialogs.Ambulances.ambulanceBill import *
from Dialogs.Ambulances.ambulancesList import *
from Dialogs.Ambulances.esBill import *


class new_emergencyServiceProfile(object):
    def setup(self, emergencyServiceProfile,userData):
        self.userdata = userData
        emergencyServiceProfile.setObjectName("emergencyServiceProfile")
        emergencyServiceProfile.resize(553, 428)
        self.frame = QtWidgets.QFrame(emergencyServiceProfile)
        self.frame.setGeometry(QtCore.QRect(10, 10, 531, 371))
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
        self.seeAmbulancesLabel = QtWidgets.QLabel(self.frame)
        self.seeAmbulancesLabel.setGeometry(QtCore.QRect(30, 285, 191, 41))
        self.seeAmbulancesLabel.setObjectName("seeAmbulancesLabel")
        self.billingRecordsLabel = QtWidgets.QLabel(self.frame)
        self.billingRecordsLabel.setGeometry(QtCore.QRect(30, 330, 191, 31))
        self.billingRecordsLabel.setObjectName("billingRecordsLabel")
        self.seeAmbulances = QtWidgets.QPushButton(self.frame)
        self.seeAmbulances.setGeometry(QtCore.QRect(230, 290, 111, 28))
        self.seeAmbulances.setStyleSheet("text-decoration:underline;\n"
"color:blue;\n"
"border:none;")
        self.seeAmbulances.setObjectName("seeAmbulances")
        self.billingRecords = QtWidgets.QPushButton(self.frame)
        self.billingRecords.setGeometry(QtCore.QRect(230, 330, 111, 28))
        self.billingRecords.setStyleSheet("text-decoration:underline;\n"
"color:blue;\n"
"border:none;")
        self.billingRecords.setObjectName("billingRecords")
        self.pushButton = QtWidgets.QPushButton(emergencyServiceProfile)
        self.pushButton.setGeometry(QtCore.QRect(450, 390, 80, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(emergencyServiceProfile)
        QtCore.QMetaObject.connectSlotsByName(emergencyServiceProfile)

    def retranslateUi(self, emergencyServiceProfile):
        _translate = QtCore.QCoreApplication.translate
        emergencyServiceProfile.setWindowTitle(_translate("emergencyServiceProfile", "Emergency Service Profile"))
        self.nameLabel.setText(_translate("emergencyServiceProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Name :</span></p></body></html>"))
        self.addressLabel.setText(_translate("emergencyServiceProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Address :</span></p></body></html>"))
        self.contactLabel.setText(_translate("emergencyServiceProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Contact No. :</span></p></body></html>"))
        self.stateLabel.setText(_translate("emergencyServiceProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">State :</span></p></body></html>"))
        self.pinCodeLabel.setText(_translate("emergencyServiceProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Pin Code :</span></p></body></html>"))
        self.cityLabel.setText(_translate("emergencyServiceProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">City :</span></p></body></html>"))
        self.address.setPlaceholderText(_translate("emergencyServiceProfile", "Street, Landmark, Area"))
        self.pinCode.setText(_translate("emergencyServiceProfile", "PinCode"))
        self.state.setText(_translate("emergencyServiceProfile", "State"))
        self.city.setText(_translate("emergencyServiceProfile", "City"))
        self.contact.setText(_translate("emergencyServiceProfile", "1234567890"))
        self.name.setText(_translate("emergencyServiceProfile", "Name"))
        self.IDLabel.setText(_translate("emergencyServiceProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">ID :</span></p></body></html>"))
        self.dispensaryID.setText(_translate("emergencyServiceProfile", "DispensaryID"))
        self.seeAmbulancesLabel.setText(_translate("emergencyServiceProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">See Ambulances :</span></p></body></html>"))
        self.billingRecordsLabel.setText(_translate("emergencyServiceProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Billing Records :</span></p></body></html>"))
        self.seeAmbulances.setText(_translate("emergencyServiceProfile", "Check Here"))
        self.billingRecords.setText(_translate("emergencyServiceProfile", "Check Here"))
        self.pushButton.setText(_translate("emergencyServiceProfile", "OK"))
        self.clickevents(emergencyServiceProfile)

    def clickevents(self,parent):
        self.pushButton.clicked.connect(lambda : parent.close())
        self.address.setText(str(self.userdata["address"]))
        self.dispensaryID.setText(str(self.userdata["id"]))
        self.pinCode.setText(str(self.userdata["pin"]))
        self.state.setText(str(self.userdata["state"]))
        self.city.setText(str(self.userdata["city"]))
        self.contact.setText(self.userdata["contact_number"])
        self.name.setText(self.userdata["name"])

        self.seeAmbulances.clicked.connect(lambda : self.clickOnSeeAmbulances(parent))
        self.billingRecords.clicked.connect(lambda : self.clickOnSeeBillingRecords(parent))

    def clickOnSeeAmbulances(self,parent):
        self.window = QDialog()
        self.dialog = ambulanceList()
        self.dialog.setup(self.window,self.userdata["id"])
        self.window.setModal(True)
        self.window.show()

    def clickOnSeeBillingRecords(self,parent):
        self.window = QDialog()
        self.dialog = esBillTable()
        self.dialog.setup(self.window,self.userdata["id"])
        self.window.setModal(True)
        self.window.show()




