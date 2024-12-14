# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'blooddonation.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_bloodDonation(object):
    def setupUi(self, bloodDonation):
        bloodDonation.setObjectName("bloodDonation")
        bloodDonation.setWindowModality(QtCore.Qt.ApplicationModal)
        bloodDonation.resize(342, 336)
        self.frame = QtWidgets.QFrame(bloodDonation)
        self.frame.setGeometry(QtCore.QRect(10, 10, 321, 281))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.bloodDonationLabel = QtWidgets.QLabel(self.frame)
        self.bloodDonationLabel.setGeometry(QtCore.QRect(40, 0, 251, 41))
        self.bloodDonationLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.bloodDonationLabel.setObjectName("bloodDonationLabel")
        self.bloodTypeLabel = QtWidgets.QLabel(self.frame)
        self.bloodTypeLabel.setGeometry(QtCore.QRect(20, 160, 151, 41))
        self.bloodTypeLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.bloodTypeLabel.setObjectName("bloodTypeLabel")
        self.quantityLabel = QtWidgets.QLabel(self.frame)
        self.quantityLabel.setGeometry(QtCore.QRect(20, 210, 151, 41))
        self.quantityLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.quantityLabel.setObjectName("quantityLabel")
        self.quantity = QtWidgets.QLineEdit(self.frame)
        self.quantity.setGeometry(QtCore.QRect(180, 220, 101, 25))
        self.quantity.setObjectName("quantity")
        self.bloodTypeComboBox = QtWidgets.QComboBox(self.frame)
        self.bloodTypeComboBox.setGeometry(QtCore.QRect(180, 180, 101, 25))
        self.bloodTypeComboBox.setObjectName("bloodTypeComboBox")
        self.bloodTypeComboBox.addItem("")
        self.bloodTypeComboBox.addItem("")
        self.bloodTypeComboBox.addItem("")
        self.bloodTypeComboBox.addItem("")
        self.bloodTypeComboBox.addItem("")
        self.bloodTypeComboBox.addItem("")
        self.bloodTypeComboBox.addItem("")
        self.bloodTypeComboBox.addItem("")
        self.patientIDLabel = QtWidgets.QLabel(self.frame)
        self.patientIDLabel.setGeometry(QtCore.QRect(20, 60, 151, 41))
        self.patientIDLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.patientIDLabel.setObjectName("patientIDLabel")
        self.eventIDLabel = QtWidgets.QLabel(self.frame)
        self.eventIDLabel.setGeometry(QtCore.QRect(20, 110, 151, 41))
        self.eventIDLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.eventIDLabel.setObjectName("eventIDLabel")
        self.patientID = QtWidgets.QLineEdit(self.frame)
        self.patientID.setGeometry(QtCore.QRect(180, 70, 101, 25))
        self.patientID.setObjectName("patientID")
        self.eventID = QtWidgets.QLineEdit(self.frame)
        self.eventID.setGeometry(QtCore.QRect(180, 120, 101, 25))
        self.eventID.setObjectName("eventID")
        self.addButton = QtWidgets.QPushButton(bloodDonation)
        self.addButton.setGeometry(QtCore.QRect(120, 300, 89, 25))
        self.addButton.setObjectName("addButton")

        self.retranslateUi(bloodDonation)
        QtCore.QMetaObject.connectSlotsByName(bloodDonation)

    def retranslateUi(self, bloodDonation):
        _translate = QtCore.QCoreApplication.translate
        bloodDonation.setWindowTitle(_translate("bloodDonation", "Blood Entry"))
        self.bloodDonationLabel.setText(_translate("bloodDonation", "<html><head/><body><p><span style=\" font-size:12pt; text-decoration: underline;\">Blood Donation Entry</span></p></body></html>"))
        self.bloodTypeLabel.setText(_translate("bloodDonation", "<html><head/><body><p>Blood Type :</p></body></html>"))
        self.quantityLabel.setText(_translate("bloodDonation", "<html><head/><body><p>Quantity :</p></body></html>"))
        self.bloodTypeComboBox.setItemText(0, _translate("bloodDonation", "A+"))
        self.bloodTypeComboBox.setItemText(1, _translate("bloodDonation", "A-"))
        self.bloodTypeComboBox.setItemText(2, _translate("bloodDonation", "B+"))
        self.bloodTypeComboBox.setItemText(3, _translate("bloodDonation", "B-"))
        self.bloodTypeComboBox.setItemText(4, _translate("bloodDonation", "AB+"))
        self.bloodTypeComboBox.setItemText(5, _translate("bloodDonation", "AB_"))
        self.bloodTypeComboBox.setItemText(6, _translate("bloodDonation", "O+"))
        self.bloodTypeComboBox.setItemText(7, _translate("bloodDonation", "O-"))
        self.patientIDLabel.setText(_translate("bloodDonation", "<html><head/><body><p>Patient ID:</p></body></html>"))
        self.eventIDLabel.setText(_translate("bloodDonation", "<html><head/><body><p>Event ID <span style=\" font-size:10pt;\">(if any) </span><span style=\" font-size:12pt;\">:</span></p></body></html>"))
        self.addButton.setText(_translate("bloodDonation", "Add "))

