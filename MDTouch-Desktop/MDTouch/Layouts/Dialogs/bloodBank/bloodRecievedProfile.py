# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bloodRecievedProfile.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_bloodRecievingProfile(object):
    def setupUi(self, bloodRecievingProfile):
        bloodRecievingProfile.setObjectName("bloodRecievingProfile")
        bloodRecievingProfile.setWindowModality(QtCore.Qt.ApplicationModal)
        bloodRecievingProfile.resize(335, 339)
        self.frame = QtWidgets.QFrame(bloodRecievingProfile)
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
        self.bloodTypeLabel.setGeometry(QtCore.QRect(20, 190, 151, 41))
        self.bloodTypeLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.bloodTypeLabel.setObjectName("bloodTypeLabel")
        self.quantityLabel = QtWidgets.QLabel(self.frame)
        self.quantityLabel.setGeometry(QtCore.QRect(20, 230, 151, 41))
        self.quantityLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.quantityLabel.setObjectName("quantityLabel")
        self.patientIDLabel = QtWidgets.QLabel(self.frame)
        self.patientIDLabel.setGeometry(QtCore.QRect(20, 140, 151, 41))
        self.patientIDLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.patientIDLabel.setObjectName("patientIDLabel")
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
        self.quantity = QtWidgets.QLabel(self.frame)
        self.quantity.setGeometry(QtCore.QRect(180, 240, 67, 17))
        self.quantity.setObjectName("quantity")
        self.bloodtype = QtWidgets.QLabel(self.frame)
        self.bloodtype.setGeometry(QtCore.QRect(180, 200, 67, 17))
        self.bloodtype.setObjectName("bloodtype")
        self.id = QtWidgets.QLabel(self.frame)
        self.id.setGeometry(QtCore.QRect(180, 60, 67, 17))
        self.id.setObjectName("id")
        self.exitbutton = QtWidgets.QPushButton(bloodRecievingProfile)
        self.exitbutton.setGeometry(QtCore.QRect(120, 300, 89, 25))
        self.exitbutton.setObjectName("exitbutton")

        self.retranslateUi(bloodRecievingProfile)
        QtCore.QMetaObject.connectSlotsByName(bloodRecievingProfile)

    def retranslateUi(self, bloodRecievingProfile):
        _translate = QtCore.QCoreApplication.translate
        bloodRecievingProfile.setWindowTitle(_translate("bloodRecievingProfile", "Record"))
        self.bloodDonationLabel.setText(_translate("bloodRecievingProfile", "<html><head/><body><p><span style=\" font-size:12pt; text-decoration: underline;\">Blood Recieving Bill</span></p></body></html>"))
        self.bloodTypeLabel.setText(_translate("bloodRecievingProfile", "<html><head/><body><p>Blood Type :</p></body></html>"))
        self.quantityLabel.setText(_translate("bloodRecievingProfile", "<html><head/><body><p>Quantity :</p></body></html>"))
        self.patientIDLabel.setText(_translate("bloodRecievingProfile", "<html><head/><body><p>Patient ID:</p></body></html>"))
        self.patientIDLabel_2.setText(_translate("bloodRecievingProfile", "<html><head/><body><p> ID:</p></body></html>"))
        self.patientIDLabel_3.setText(_translate("bloodRecievingProfile", "<html><head/><body><p>Date :</p></body></html>"))
        self.date.setText(_translate("bloodRecievingProfile", "TextLabel"))
        self.patientid.setText(_translate("bloodRecievingProfile", "TextLabel"))
        self.quantity.setText(_translate("bloodRecievingProfile", "TextLabel"))
        self.bloodtype.setText(_translate("bloodRecievingProfile", "TextLabel"))
        self.id.setText(_translate("bloodRecievingProfile", "TextLabel"))
        self.exitbutton.setText(_translate("bloodRecievingProfile", "Exit"))

