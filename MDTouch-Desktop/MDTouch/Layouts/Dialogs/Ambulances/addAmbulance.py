# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addAmbulance.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(575, 391)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(10, 10, 551, 311))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.ambulanceListLabel = QtWidgets.QLabel(self.frame)
        self.ambulanceListLabel.setGeometry(QtCore.QRect(210, 0, 191, 41))
        self.ambulanceListLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.ambulanceListLabel.setObjectName("ambulanceListLabel")
        self.vechicleNumberLabel = QtWidgets.QLabel(self.frame)
        self.vechicleNumberLabel.setGeometry(QtCore.QRect(20, 60, 151, 41))
        self.vechicleNumberLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.vechicleNumberLabel.setObjectName("vechicleNumberLabel")
        self.driverNameLabel = QtWidgets.QLabel(self.frame)
        self.driverNameLabel.setGeometry(QtCore.QRect(20, 110, 151, 41))
        self.driverNameLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.driverNameLabel.setObjectName("driverNameLabel")
        self.capacityLabel = QtWidgets.QLabel(self.frame)
        self.capacityLabel.setGeometry(QtCore.QRect(20, 210, 91, 41))
        self.capacityLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.capacityLabel.setObjectName("capacityLabel")
        self.mobileNumberLabel = QtWidgets.QLabel(self.frame)
        self.mobileNumberLabel.setGeometry(QtCore.QRect(20, 160, 151, 41))
        self.mobileNumberLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.mobileNumberLabel.setObjectName("mobileNumberLabel")
        self.typeLabel = QtWidgets.QLabel(self.frame)
        self.typeLabel.setGeometry(QtCore.QRect(20, 260, 71, 41))
        self.typeLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.typeLabel.setObjectName("typeLabel")
        self.capacityComboBox = QtWidgets.QComboBox(self.frame)
        self.capacityComboBox.setGeometry(QtCore.QRect(180, 220, 61, 25))
        self.capacityComboBox.setObjectName("capacityComboBox")
        self.capacityComboBox.addItem("")
        self.capacityComboBox.addItem("")
        self.capacityComboBox.addItem("")
        self.capacityComboBox.addItem("")
        self.capacityComboBox.addItem("")
        self.capacityComboBox.addItem("")
        self.capacityComboBox.addItem("")
        self.capacityComboBox.addItem("")
        self.capacityComboBox.addItem("")
        self.capacityComboBox.addItem("")
        self.capacityComboBox.addItem("")
        self.capacityComboBox.addItem("")
        self.typeCombobox = QtWidgets.QComboBox(self.frame)
        self.typeCombobox.setGeometry(QtCore.QRect(180, 270, 191, 25))
        self.typeCombobox.setObjectName("typeCombobox")
        self.typeCombobox.addItem("")
        self.typeCombobox.addItem("")
        self.typeCombobox.addItem("")
        self.typeCombobox.addItem("")
        self.typeCombobox.addItem("")
        self.vechicleNumber = QtWidgets.QLineEdit(self.frame)
        self.vechicleNumber.setGeometry(QtCore.QRect(180, 70, 351, 25))
        self.vechicleNumber.setObjectName("vechicleNumber")
        self.driverName = QtWidgets.QLineEdit(self.frame)
        self.driverName.setGeometry(QtCore.QRect(180, 120, 351, 25))
        self.driverName.setObjectName("driverName")
        self.mobileNumber = QtWidgets.QLineEdit(self.frame)
        self.mobileNumber.setGeometry(QtCore.QRect(180, 170, 351, 25))
        self.mobileNumber.setObjectName("mobileNumber")
        self.addButton = QtWidgets.QPushButton(Form)
        self.addButton.setGeometry(QtCore.QRect(240, 340, 89, 25))
        self.addButton.setObjectName("addButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Add Ambulance"))
        self.ambulanceListLabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; text-decoration: underline;\">Add Ambulance</span></p></body></html>"))
        self.vechicleNumberLabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">Vechicle Number :</span></p></body></html>"))
        self.driverNameLabel.setText(_translate("Form", "<html><head/><body><p>Driver Name : </p></body></html>"))
        self.capacityLabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">Capacity :</span></p></body></html>"))
        self.mobileNumberLabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">Mobile Number :</span></p></body></html>"))
        self.typeLabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">Type : </span></p></body></html>"))
        self.capacityComboBox.setItemText(0, _translate("Form", "1"))
        self.capacityComboBox.setItemText(1, _translate("Form", "2"))
        self.capacityComboBox.setItemText(2, _translate("Form", "3"))
        self.capacityComboBox.setItemText(3, _translate("Form", "4"))
        self.capacityComboBox.setItemText(4, _translate("Form", "5"))
        self.capacityComboBox.setItemText(5, _translate("Form", "6"))
        self.capacityComboBox.setItemText(6, _translate("Form", "7"))
        self.capacityComboBox.setItemText(7, _translate("Form", "8"))
        self.capacityComboBox.setItemText(8, _translate("Form", "9"))
        self.capacityComboBox.setItemText(9, _translate("Form", "10"))
        self.capacityComboBox.setItemText(10, _translate("Form", "11"))
        self.capacityComboBox.setItemText(11, _translate("Form", "12"))
        self.typeCombobox.setItemText(0, _translate("Form", "Car"))
        self.typeCombobox.setItemText(1, _translate("Form", "Bus"))
        self.typeCombobox.setItemText(2, _translate("Form", "Van"))
        self.typeCombobox.setItemText(3, _translate("Form", "Magic"))
        self.typeCombobox.setItemText(4, _translate("Form", "Sumo"))
        self.addButton.setText(_translate("Form", "Add "))

