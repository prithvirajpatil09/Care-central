# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'blooddonationProfile.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_bloodDonationProfile(object):
    def setupUi(self, bloodDonationProfile):
        bloodDonationProfile.setObjectName("bloodDonationProfile")
        bloodDonationProfile.setWindowModality(QtCore.Qt.ApplicationModal)
        bloodDonationProfile.resize(335, 411)
        self.frame = QtWidgets.QFrame(bloodDonationProfile)
        self.frame.setGeometry(QtCore.QRect(10, 10, 321, 351))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.bloodDonationLabel = QtWidgets.QLabel(self.frame)
        self.bloodDonationLabel.setGeometry(QtCore.QRect(40, 0, 251, 41))
        self.bloodDonationLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.bloodDonationLabel.setObjectName("bloodDonationLabel")
        self.bloodTypeLabel = QtWidgets.QLabel(self.frame)
        self.bloodTypeLabel.setGeometry(QtCore.QRect(20, 240, 151, 41))
        self.bloodTypeLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.bloodTypeLabel.setObjectName("bloodTypeLabel")
        self.quantityLabel = QtWidgets.QLabel(self.frame)
        self.quantityLabel.setGeometry(QtCore.QRect(20, 290, 151, 41))
        self.quantityLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.quantityLabel.setObjectName("quantityLabel")
        self.patientIDLabel = QtWidgets.QLabel(self.frame)
        self.patientIDLabel.setGeometry(QtCore.QRect(20, 140, 151, 41))
        self.patientIDLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.patientIDLabel.setObjectName("patientIDLabel")
        self.eventIDLabel = QtWidgets.QLabel(self.frame)
        self.eventIDLabel.setGeometry(QtCore.QRect(20, 190, 151, 41))
        self.eventIDLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.eventIDLabel.setObjectName("eventIDLabel")
        self.patientIDLabel_2 = QtWidgets.QLabel(self.frame)
        self.patientIDLabel_2.setGeometry(QtCore.QRect(20, 50, 91, 41))
        self.patientIDLabel_2.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.patientIDLabel_2.setObjectName("patientIDLabel_2")
        self.patientIDLabel_3 = QtWidgets.QLabel(self.frame)
        self.patientIDLabel_3.setGeometry(QtCore.QRect(20, 90, 151, 41))
        self.patientIDLabel_3.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.patientIDLabel_3.setObjectName("patientIDLabel_3")
        self.date = QtWidgets.QLabel(self.frame)
        self.date.setGeometry(QtCore.QRect(180, 100, 161, 17))
        self.date.setObjectName("date")
        self.patientid = QtWidgets.QLabel(self.frame)
        self.patientid.setGeometry(QtCore.QRect(180, 150, 111, 17))
        self.patientid.setObjectName("patientid")
        self.eventId = QtWidgets.QLabel(self.frame)
        self.eventId.setGeometry(QtCore.QRect(180, 200, 67, 17))
        self.eventId.setObjectName("eventId")
        self.quantity = QtWidgets.QLabel(self.frame)
        self.quantity.setGeometry(QtCore.QRect(180, 300, 67, 17))
        self.quantity.setObjectName("quantity")
        self.bloodtype = QtWidgets.QLabel(self.frame)
        self.bloodtype.setGeometry(QtCore.QRect(180, 250, 67, 17))
        self.bloodtype.setObjectName("bloodtype")
        self.id = QtWidgets.QLabel(self.frame)
        self.id.setGeometry(QtCore.QRect(180, 60, 67, 17))
        self.id.setObjectName("id")
        self.exitbutton = QtWidgets.QPushButton(bloodDonationProfile)
        self.exitbutton.setGeometry(QtCore.QRect(120, 370, 89, 25))
        self.exitbutton.setObjectName("exitbutton")

        self.retranslateUi(bloodDonationProfile)
        QtCore.QMetaObject.connectSlotsByName(bloodDonationProfile)

    def retranslateUi(self, bloodDonationProfile):
        _translate = QtCore.QCoreApplication.translate
        bloodDonationProfile.setWindowTitle(_translate("bloodDonationProfile", "Record"))
        self.bloodDonationLabel.setText(_translate("bloodDonationProfile", "<html><head/><body><p><span style=\" font-size:12pt; text-decoration: underline;\">Blood Donation Record</span></p></body></html>"))
        self.bloodTypeLabel.setText(_translate("bloodDonationProfile", "<html><head/><body><p>Blood Type :</p></body></html>"))
        self.quantityLabel.setText(_translate("bloodDonationProfile", "<html><head/><body><p>Quantity :</p></body></html>"))
        self.patientIDLabel.setText(_translate("bloodDonationProfile", "<html><head/><body><p>Patient ID:</p></body></html>"))
        self.eventIDLabel.setText(_translate("bloodDonationProfile", "<html><head/><body><p>Event ID <span style=\" font-size:10pt;\">(if any) </span><span style=\" font-size:12pt;\">:</span></p></body></html>"))
        self.patientIDLabel_2.setText(_translate("bloodDonationProfile", "<html><head/><body><p> ID:</p></body></html>"))
        self.patientIDLabel_3.setText(_translate("bloodDonationProfile", "<html><head/><body><p>Date :</p></body></html>"))
        self.date.setText(_translate("bloodDonationProfile", "TextLabel"))
        self.patientid.setText(_translate("bloodDonationProfile", "TextLabel"))
        self.eventId.setText(_translate("bloodDonationProfile", "TextLabel"))
        self.quantity.setText(_translate("bloodDonationProfile", "TextLabel"))
        self.bloodtype.setText(_translate("bloodDonationProfile", "TextLabel"))
        self.id.setText(_translate("bloodDonationProfile", "TextLabel"))
        self.exitbutton.setText(_translate("bloodDonationProfile", "Exit"))
