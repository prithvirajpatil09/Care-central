from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Dialogs.hospital.adminList import *
from Dialogs.hospital.doctorList import *
from Dialogs.superadmin.Events.myEventList import *

from PyQt5 import QtCore, QtGui, QtWidgets

class new_hospitalProfile(object):
    def setup(self, hospitalProfile,userData):
        self.userdata = userData
        hospitalProfile.setObjectName("hospitalProfile")
        hospitalProfile.resize(553, 563)
        self.frame = QtWidgets.QFrame(hospitalProfile)
        self.frame.setGeometry(QtCore.QRect(10, 10, 531, 501))
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
        self.city.setGeometry(QtCore.QRect(100, 210, 181, 21))
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
        self.HospitalID = QtWidgets.QLabel(self.frame)
        self.HospitalID.setGeometry(QtCore.QRect(150, 0, 371, 41))
        self.HospitalID.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.HospitalID.setObjectName("HospitalID")
        self.seeDoctorsLabel = QtWidgets.QLabel(self.frame)
        self.seeDoctorsLabel.setGeometry(QtCore.QRect(30, 285, 191, 41))
        self.seeDoctorsLabel.setObjectName("seeDoctorsLabel")
        self.billingRecordsLabel = QtWidgets.QLabel(self.frame)
        self.billingRecordsLabel.setGeometry(QtCore.QRect(30, 330, 191, 31))
        self.billingRecordsLabel.setObjectName("billingRecordsLabel")
        self.eventsOrganizedLabel = QtWidgets.QLabel(self.frame)
        self.eventsOrganizedLabel.setGeometry(QtCore.QRect(30, 370, 191, 31))
        self.eventsOrganizedLabel.setObjectName("eventsOrganizedLabel")
        self.seeDoctor = QtWidgets.QPushButton(self.frame)
        self.seeDoctor.setGeometry(QtCore.QRect(230, 290, 111, 28))
        self.seeDoctor.setStyleSheet("text-decoration:underline;\n"
"color:blue;\n"
"border:none;")
        self.seeDoctor.setObjectName("seeDoctor")
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
        self.seeBedsStatusLabel = QtWidgets.QLabel(self.frame)
        self.seeBedsStatusLabel.setGeometry(QtCore.QRect(30, 410, 191, 31))
        self.seeBedsStatusLabel.setObjectName("seeBedsStatusLabel")
        self.seeBedStatus = QtWidgets.QPushButton(self.frame)
        self.seeBedStatus.setGeometry(QtCore.QRect(230, 410, 111, 28))
        self.seeBedStatus.setStyleSheet("text-decoration:underline;\n"
"color:blue;\n"
"border:none;")
        self.seeBedStatus.setObjectName("seeBedStatus")
        self.seeAdminLabel = QtWidgets.QLabel(self.frame)
        self.seeAdminLabel.setGeometry(QtCore.QRect(30, 450, 111, 31))
        self.seeAdminLabel.setObjectName("seeAdminLabel")
        self.seeAdmins = QtWidgets.QPushButton(self.frame)
        self.seeAdmins.setGeometry(QtCore.QRect(230, 450, 111, 28))
        self.seeAdmins.setStyleSheet("text-decoration:underline;\n"
"color:blue;\n"
"border:none;")
        self.seeAdmins.setObjectName("seeAdmins")
        self.pushButton = QtWidgets.QPushButton(hospitalProfile)
        self.pushButton.setGeometry(QtCore.QRect(450, 520, 80, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(hospitalProfile)
        QtCore.QMetaObject.connectSlotsByName(hospitalProfile)

    def retranslateUi(self, hospitalProfile):
        _translate = QtCore.QCoreApplication.translate
        hospitalProfile.setWindowTitle(_translate("hospitalProfile", "Hospital Profile"))
        self.nameLabel.setText(_translate("hospitalProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Name :</span></p></body></html>"))
        self.addressLabel.setText(_translate("hospitalProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Address :</span></p></body></html>"))
        self.contactLabel.setText(_translate("hospitalProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Contact No. :</span></p></body></html>"))
        self.stateLabel.setText(_translate("hospitalProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">State :</span></p></body></html>"))
        self.pinCodeLabel.setText(_translate("hospitalProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Pin Code :</span></p></body></html>"))
        self.cityLabel.setText(_translate("hospitalProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">City :</span></p></body></html>"))
        self.address.setPlaceholderText(_translate("hospitalProfile", "Street, Landmark, Area"))
        self.pinCode.setText(_translate("hospitalProfile", "PinCode"))
        self.state.setText(_translate("hospitalProfile", "State"))
        self.city.setText(_translate("hospitalProfile", "City"))
        self.contact.setText(_translate("hospitalProfile", "1234567890"))
        self.name.setText(_translate("hospitalProfile", "Name"))
        self.IDLabel.setText(_translate("hospitalProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">ID :</span></p></body></html>"))
        self.HospitalID.setText(_translate("hospitalProfile", "HospitalID"))
        self.seeDoctorsLabel.setText(_translate("hospitalProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">See Doctors:</span></p></body></html>"))
        self.billingRecordsLabel.setText(_translate("hospitalProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Billing Records :</span></p></body></html>"))
        self.eventsOrganizedLabel.setText(_translate("hospitalProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Events Orgranized :</span></p></body></html>"))
        self.seeDoctor.setText(_translate("hospitalProfile", "Check Here"))
        self.billingRecords.setText(_translate("hospitalProfile", "Check Here"))
        self.eventsOrganized.setText(_translate("hospitalProfile", "Check Here"))
        self.seeBedsStatusLabel.setText(_translate("hospitalProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">See Beds Status :</span></p></body></html>"))
        self.seeBedStatus.setText(_translate("hospitalProfile", "Check Here"))
        self.seeAdminLabel.setText(_translate("hospitalProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">See Admins :</span></p></body></html>"))
        self.seeAdmins.setText(_translate("hospitalProfile", "Check Here"))
        self.pushButton.setText(_translate("hospitalProfile", "OK"))
        self.events(hospitalProfile)

    def events(self,parent):
        data = self.userdata
        self.name.setText(str(data["name"]))
        self.HospitalID.setText(str(data["id"]))
        self.city.setText(data["city"])
        self.state.setText(data["state"])
        self.pinCode.setText(str(data["pin"]))
        self.address.setText(str(data["address"]))
        self.contact.setText(str(data["contact"]))
        self.seeAdmins.clicked.connect(lambda :self.clickOnSeeAdmins())
        self.seeDoctor.clicked.connect(lambda : self.clickOnSeeDoctors())
        self.eventsOrganized.clicked.connect(lambda : self.clickOnEventsOrganized())

        self.pushButton.clicked.connect(lambda: parent.close())

    def clickOnEventsOrganized(self):
        self.window = QDialog()
        self.dialog = myEventList()
        self.dialog.setup(self.window,'H',self.userdata)
        self.window.setModal(True)
        self.window.show()


    def clickOnSeeDoctors(self):
        self.window = QDialog()
        self.dialog = doctorList()
        self.dialog.setup(self.window,self.userdata)
        self.window.setModal(True)
        self.window.show()

    def clickOnSeeAdmins(self):
        self.window = QDialog()
        self.dialog = adminList()
        self.dialog.setup(self.window,self.userdata)
        self.window.setModal(True)
        self.window.show()
