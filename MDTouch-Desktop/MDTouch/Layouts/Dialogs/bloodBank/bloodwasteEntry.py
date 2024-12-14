# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bloodwasteEntry.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_bloodwasteEntry(object):
    def setupUi(self, bloodwasteEntry):
        bloodwasteEntry.setObjectName("bloodwasteEntry")
        bloodwasteEntry.setWindowModality(QtCore.Qt.ApplicationModal)
        bloodwasteEntry.resize(342, 402)
        self.frame = QtWidgets.QFrame(bloodwasteEntry)
        self.frame.setGeometry(QtCore.QRect(10, 10, 321, 351))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.bloodBillingLabel = QtWidgets.QLabel(self.frame)
        self.bloodBillingLabel.setGeometry(QtCore.QRect(20, 0, 291, 61))
        self.bloodBillingLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.bloodBillingLabel.setObjectName("bloodBillingLabel")
        self.bloodTypeLabel = QtWidgets.QLabel(self.frame)
        self.bloodTypeLabel.setGeometry(QtCore.QRect(20, 70, 151, 41))
        self.bloodTypeLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.bloodTypeLabel.setObjectName("bloodTypeLabel")
        self.quantityLabel = QtWidgets.QLabel(self.frame)
        self.quantityLabel.setGeometry(QtCore.QRect(20, 120, 151, 41))
        self.quantityLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.quantityLabel.setObjectName("quantityLabel")
        self.quantity = QtWidgets.QLineEdit(self.frame)
        self.quantity.setGeometry(QtCore.QRect(180, 130, 101, 25))
        self.quantity.setObjectName("quantity")
        self.bloodTypeComboBox = QtWidgets.QComboBox(self.frame)
        self.bloodTypeComboBox.setGeometry(QtCore.QRect(180, 80, 101, 25))
        self.bloodTypeComboBox.setObjectName("bloodTypeComboBox")
        self.bloodTypeComboBox.addItem("")
        self.bloodTypeComboBox.addItem("")
        self.bloodTypeComboBox.addItem("")
        self.bloodTypeComboBox.addItem("")
        self.bloodTypeComboBox.addItem("")
        self.bloodTypeComboBox.addItem("")
        self.bloodTypeComboBox.addItem("")
        self.bloodTypeComboBox.addItem("")
        self.reason = QtWidgets.QTextEdit(self.frame)
        self.reason.setGeometry(QtCore.QRect(20, 190, 301, 151))
        self.reason.setObjectName("reason")
        self.reasonLabel = QtWidgets.QLabel(self.frame)
        self.reasonLabel.setGeometry(QtCore.QRect(20, 160, 151, 41))
        self.reasonLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.reasonLabel.setObjectName("reasonLabel")
        self.addButton = QtWidgets.QPushButton(bloodwasteEntry)
        self.addButton.setGeometry(QtCore.QRect(120, 370, 89, 25))
        self.addButton.setObjectName("addButton")

        self.retranslateUi(bloodwasteEntry)
        QtCore.QMetaObject.connectSlotsByName(bloodwasteEntry)

    def retranslateUi(self, bloodwasteEntry):
        _translate = QtCore.QCoreApplication.translate
        bloodwasteEntry.setWindowTitle(_translate("bloodwasteEntry", "Blood Entry"))
        self.bloodBillingLabel.setText(_translate("bloodwasteEntry", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; text-decoration: underline;\">Blood Waste </span></p><p align=\"center\"><span style=\" font-size:12pt; text-decoration: underline;\">Entry</span></p></body></html>"))
        self.bloodTypeLabel.setText(_translate("bloodwasteEntry", "<html><head/><body><p>Blood Type :</p></body></html>"))
        self.quantityLabel.setText(_translate("bloodwasteEntry", "<html><head/><body><p>Quantity :</p></body></html>"))
        self.bloodTypeComboBox.setItemText(0, _translate("bloodwasteEntry", "A+"))
        self.bloodTypeComboBox.setItemText(1, _translate("bloodwasteEntry", "A-"))
        self.bloodTypeComboBox.setItemText(2, _translate("bloodwasteEntry", "B+"))
        self.bloodTypeComboBox.setItemText(3, _translate("bloodwasteEntry", "B-"))
        self.bloodTypeComboBox.setItemText(4, _translate("bloodwasteEntry", "AB+"))
        self.bloodTypeComboBox.setItemText(5, _translate("bloodwasteEntry", "AB_"))
        self.bloodTypeComboBox.setItemText(6, _translate("bloodwasteEntry", "O+"))
        self.bloodTypeComboBox.setItemText(7, _translate("bloodwasteEntry", "O-"))
        self.reasonLabel.setText(_translate("bloodwasteEntry", "<html><head/><body><p>Reason : </p></body></html>"))
        self.addButton.setText(_translate("bloodwasteEntry", "Add"))

