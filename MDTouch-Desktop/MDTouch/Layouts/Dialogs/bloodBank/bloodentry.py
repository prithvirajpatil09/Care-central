# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bloodentry.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_bloodentry(object):
    def setupUi(self, bloodentry):
        bloodentry.setObjectName("bloodentry")
        bloodentry.setWindowModality(QtCore.Qt.ApplicationModal)
        bloodentry.resize(350, 253)
        self.frame = QtWidgets.QFrame(bloodentry)
        self.frame.setGeometry(QtCore.QRect(10, 10, 331, 181))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.bloodEntry = QtWidgets.QLabel(self.frame)
        self.bloodEntry.setGeometry(QtCore.QRect(90, 0, 191, 41))
        self.bloodEntry.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.bloodEntry.setObjectName("bloodEntry")
        self.bloodTypeLabel = QtWidgets.QLabel(self.frame)
        self.bloodTypeLabel.setGeometry(QtCore.QRect(20, 60, 151, 41))
        self.bloodTypeLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.bloodTypeLabel.setObjectName("bloodTypeLabel")
        self.quantityLabel = QtWidgets.QLabel(self.frame)
        self.quantityLabel.setGeometry(QtCore.QRect(20, 110, 151, 41))
        self.quantityLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.quantityLabel.setObjectName("quantityLabel")
        self.quantity = QtWidgets.QLineEdit(self.frame)
        self.quantity.setGeometry(QtCore.QRect(180, 120, 101, 25))
        self.quantity.setObjectName("quantity")
        self.bloodTypeComboBox = QtWidgets.QComboBox(self.frame)
        self.bloodTypeComboBox.setGeometry(QtCore.QRect(180, 70, 101, 25))
        self.bloodTypeComboBox.setObjectName("bloodTypeComboBox")
        self.bloodTypeComboBox.addItem("")
        self.bloodTypeComboBox.addItem("")
        self.bloodTypeComboBox.addItem("")
        self.bloodTypeComboBox.addItem("")
        self.bloodTypeComboBox.addItem("")
        self.bloodTypeComboBox.addItem("")
        self.bloodTypeComboBox.addItem("")
        self.bloodTypeComboBox.addItem("")
        self.addButton = QtWidgets.QPushButton(bloodentry)
        self.addButton.setGeometry(QtCore.QRect(130, 210, 89, 25))
        self.addButton.setObjectName("addButton")

        self.retranslateUi(bloodentry)
        QtCore.QMetaObject.connectSlotsByName(bloodentry)

    def retranslateUi(self, bloodentry):
        _translate = QtCore.QCoreApplication.translate
        bloodentry.setWindowTitle(_translate("bloodentry", "Blood Entry"))
        self.bloodEntry.setText(_translate("bloodentry", "<html><head/><body><p><span style=\" font-size:12pt; text-decoration: underline;\">Blood Entry</span></p></body></html>"))
        self.bloodTypeLabel.setText(_translate("bloodentry", "<html><head/><body><p>Blood Type :</p></body></html>"))
        self.quantityLabel.setText(_translate("bloodentry", "<html><head/><body><p>Quantity :</p></body></html>"))
        self.bloodTypeComboBox.setItemText(0, _translate("bloodentry", "A+"))
        self.bloodTypeComboBox.setItemText(1, _translate("bloodentry", "A-"))
        self.bloodTypeComboBox.setItemText(2, _translate("bloodentry", "B+"))
        self.bloodTypeComboBox.setItemText(3, _translate("bloodentry", "B-"))
        self.bloodTypeComboBox.setItemText(4, _translate("bloodentry", "AB+"))
        self.bloodTypeComboBox.setItemText(5, _translate("bloodentry", "AB_"))
        self.bloodTypeComboBox.setItemText(6, _translate("bloodentry", "O+"))
        self.bloodTypeComboBox.setItemText(7, _translate("bloodentry", "O-"))
        self.addButton.setText(_translate("bloodentry", "Add "))

