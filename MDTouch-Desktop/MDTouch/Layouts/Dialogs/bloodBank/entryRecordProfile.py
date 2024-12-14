# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'entryRecordProfile.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_bloodentryProfile(object):
    def setupUi(self, bloodentryProfile):
        bloodentryProfile.setObjectName("bloodentryProfile")
        bloodentryProfile.setWindowModality(QtCore.Qt.ApplicationModal)
        bloodentryProfile.resize(350, 318)
        self.frame = QtWidgets.QFrame(bloodentryProfile)
        self.frame.setGeometry(QtCore.QRect(10, 10, 331, 261))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.bloodEntry = QtWidgets.QLabel(self.frame)
        self.bloodEntry.setGeometry(QtCore.QRect(60, 10, 231, 41))
        self.bloodEntry.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.bloodEntry.setObjectName("bloodEntry")
        self.bloodtype = QtWidgets.QLabel(self.frame)
        self.bloodtype.setGeometry(QtCore.QRect(160, 120, 121, 41))
        self.bloodtype.setObjectName("bloodtype")
        self.quantity = QtWidgets.QLabel(self.frame)
        self.quantity.setGeometry(QtCore.QRect(160, 170, 151, 41))
        self.quantity.setObjectName("quantity")
        self.bloodTypeLabel = QtWidgets.QLabel(self.frame)
        self.bloodTypeLabel.setGeometry(QtCore.QRect(30, 120, 151, 41))
        self.bloodTypeLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.bloodTypeLabel.setObjectName("bloodTypeLabel")
        self.quantityLabel = QtWidgets.QLabel(self.frame)
        self.quantityLabel.setGeometry(QtCore.QRect(30, 170, 151, 41))
        self.quantityLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.quantityLabel.setObjectName("quantityLabel")
        self.id = QtWidgets.QLabel(self.frame)
        self.id.setGeometry(QtCore.QRect(160, 80, 67, 17))
        self.id.setObjectName("id")
        self.idLabel = QtWidgets.QLabel(self.frame)
        self.idLabel.setGeometry(QtCore.QRect(30, 70, 51, 41))
        self.idLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.idLabel.setObjectName("idLabel")
        self.date = QtWidgets.QLabel(self.frame)
        self.date.setGeometry(QtCore.QRect(160, 230, 151, 17))
        self.date.setObjectName("date")
        self.dateLabel = QtWidgets.QLabel(self.frame)
        self.dateLabel.setGeometry(QtCore.QRect(30, 220, 81, 41))
        self.dateLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.dateLabel.setObjectName("dateLabel")
        self.closeButton = QtWidgets.QPushButton(bloodentryProfile)
        self.closeButton.setGeometry(QtCore.QRect(130, 280, 89, 25))
        self.closeButton.setObjectName("closeButton")

        self.retranslateUi(bloodentryProfile)
        QtCore.QMetaObject.connectSlotsByName(bloodentryProfile)

    def retranslateUi(self, bloodentryProfile):
        _translate = QtCore.QCoreApplication.translate
        bloodentryProfile.setWindowTitle(_translate("bloodentryProfile", "Record"))
        self.bloodEntry.setText(_translate("bloodentryProfile", "<html><head/><body><p><span style=\" font-size:12pt; text-decoration: underline;\">Blood Entry Record</span></p><p align=\"center\"><br/></p></body></html>"))
        self.bloodtype.setText(_translate("bloodentryProfile", "TextLabel"))
        self.quantity.setText(_translate("bloodentryProfile", "TextLabel"))
        self.bloodTypeLabel.setText(_translate("bloodentryProfile", "<html><head/><body><p>Blood Type :</p></body></html>"))
        self.quantityLabel.setText(_translate("bloodentryProfile", "<html><head/><body><p>Quantity :</p></body></html>"))
        self.id.setText(_translate("bloodentryProfile", "TextLabel"))
        self.idLabel.setText(_translate("bloodentryProfile", "<html><head/><body><p>ID :</p></body></html>"))
        self.date.setText(_translate("bloodentryProfile", "TextLabel"))
        self.dateLabel.setText(_translate("bloodentryProfile", "<html><head/><body><p>Date :</p></body></html>"))
        self.closeButton.setText(_translate("bloodentryProfile", "close"))

