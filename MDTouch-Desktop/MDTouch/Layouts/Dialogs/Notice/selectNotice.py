# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectNotice.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_selectHospital(object):
    def setupUi(self, selectHospital):
        selectHospital.setObjectName("selectHospital")
        selectHospital.resize(209, 180)
        selectHospital.setWindowTitle("")
        self.title = QtWidgets.QLabel(selectHospital)
        self.title.setGeometry(QtCore.QRect(-50, 0, 321, 51))
        self.title.setObjectName("title")
        self.removeButton = QtWidgets.QPushButton(selectHospital)
        self.removeButton.setGeometry(QtCore.QRect(60, 120, 80, 28))
        self.removeButton.setObjectName("removeButton")
        self.searchByID = QtWidgets.QLineEdit(selectHospital)
        self.searchByID.setGeometry(QtCore.QRect(10, 70, 191, 27))
        self.searchByID.setObjectName("searchByID")

        self.retranslateUi(selectHospital)
        QtCore.QMetaObject.connectSlotsByName(selectHospital)

    def retranslateUi(self, selectHospital):
        _translate = QtCore.QCoreApplication.translate
        self.title.setText(_translate("selectHospital", "<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; font-weight:600; text-decoration: underline;\">Select Notice</span></p></body></html>"))
        self.removeButton.setText(_translate("selectHospital", "SELECT"))
        self.searchByID.setPlaceholderText(_translate("selectHospital", "Enter Notice ID"))

