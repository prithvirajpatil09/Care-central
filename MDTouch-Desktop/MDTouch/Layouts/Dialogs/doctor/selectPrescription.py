# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectPrescription.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_selectPrescription(object):
    def setupUi(self, selectPrescription):
        selectPrescription.setObjectName("selectPrescription")
        selectPrescription.resize(279, 295)
        selectPrescription.setWindowTitle("")
        self.title = QtWidgets.QLabel(selectPrescription)
        self.title.setGeometry(QtCore.QRect(-20, 0, 321, 51))
        self.title.setObjectName("title")
        self.selectButton = QtWidgets.QPushButton(selectPrescription)
        self.selectButton.setGeometry(QtCore.QRect(100, 230, 80, 28))
        self.selectButton.setObjectName("selectButton")
        self.patientID = QtWidgets.QLineEdit(selectPrescription)
        self.patientID.setGeometry(QtCore.QRect(50, 70, 191, 27))
        self.patientID.setObjectName("patientID")
        self.prescriptionId = QtWidgets.QLineEdit(selectPrescription)
        self.prescriptionId.setGeometry(QtCore.QRect(50, 170, 191, 27))
        self.prescriptionId.setObjectName("prescriptionId")
        self.orLabel = QtWidgets.QLabel(selectPrescription)
        self.orLabel.setGeometry(QtCore.QRect(30, 110, 221, 41))
        self.orLabel.setObjectName("orLabel")

        self.retranslateUi(selectPrescription)
        QtCore.QMetaObject.connectSlotsByName(selectPrescription)

    def retranslateUi(self, selectPrescription):
        _translate = QtCore.QCoreApplication.translate
        self.title.setText(_translate("selectPrescription", "<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; font-weight:600; text-decoration: underline;\">Select Prescription</span></p></body></html>"))
        self.selectButton.setText(_translate("selectPrescription", "SELECT"))
        self.patientID.setPlaceholderText(_translate("selectPrescription", "Enter Patient ID"))
        self.prescriptionId.setPlaceholderText(_translate("selectPrescription", "Enter Prescription ID"))
        self.orLabel.setText(_translate("selectPrescription", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">OR</span></p></body></html>"))

