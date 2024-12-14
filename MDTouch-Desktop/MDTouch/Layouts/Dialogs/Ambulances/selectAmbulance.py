# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectAmbulance.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_selectHospital(object):
    def setupUi(self, selectHospital):
        selectHospital.setObjectName("selectHospital")
        selectHospital.resize(362, 269)
        selectHospital.setWindowTitle("")
        self.title = QtWidgets.QLabel(selectHospital)
        self.title.setGeometry(QtCore.QRect(30, 0, 321, 51))
        self.title.setObjectName("title")
        self.frame = QtWidgets.QFrame(selectHospital)
        self.frame.setGeometry(QtCore.QRect(10, 60, 341, 131))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.searchByID = QtWidgets.QLineEdit(self.frame)
        self.searchByID.setGeometry(QtCore.QRect(40, 10, 281, 27))
        self.searchByID.setObjectName("searchByID")
        self.ORLabel = QtWidgets.QLabel(self.frame)
        self.ORLabel.setGeometry(QtCore.QRect(120, 40, 111, 31))
        self.ORLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ORLabel.setObjectName("ORLabel")
        self.searchByNumber = QtWidgets.QLineEdit(self.frame)
        self.searchByNumber.setGeometry(QtCore.QRect(40, 80, 281, 27))
        self.searchByNumber.setObjectName("searchByNumber")
        self.removeButton = QtWidgets.QPushButton(selectHospital)
        self.removeButton.setGeometry(QtCore.QRect(130, 210, 80, 28))
        self.removeButton.setObjectName("removeButton")

        self.retranslateUi(selectHospital)
        QtCore.QMetaObject.connectSlotsByName(selectHospital)

    def retranslateUi(self, selectHospital):
        _translate = QtCore.QCoreApplication.translate
        self.title.setText(_translate("selectHospital", "<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; font-weight:600; text-decoration: underline;\">Select Ambulance</span></p></body></html>"))
        self.searchByID.setPlaceholderText(_translate("selectHospital", "Search by Ambulance ID"))
        self.ORLabel.setText(_translate("selectHospital", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">OR</span></p></body></html>"))
        self.searchByNumber.setPlaceholderText(_translate("selectHospital", "Search by Vechicle Number"))
        self.removeButton.setText(_translate("selectHospital", "SELECT"))

