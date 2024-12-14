# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectHospital.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_selectHospital(object):
    def setupUi(self, selectHospital):
        selectHospital.setObjectName("selectHospital")
        selectHospital.resize(362, 331)
        self.title = QtWidgets.QLabel(selectHospital)
        self.title.setGeometry(QtCore.QRect(30, 0, 321, 51))
        self.title.setObjectName("title")
        self.frame = QtWidgets.QFrame(selectHospital)
        self.frame.setGeometry(QtCore.QRect(10, 60, 341, 211))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.cityComboBox = QtWidgets.QComboBox(self.frame)
        self.cityComboBox.setGeometry(QtCore.QRect(160, 120, 161, 27))
        self.cityComboBox.setObjectName("cityComboBox")
        self.dispensaryComboBox = QtWidgets.QComboBox(self.frame)
        self.dispensaryComboBox.setGeometry(QtCore.QRect(160, 170, 161, 27))
        self.dispensaryComboBox.setObjectName("dispensaryComboBox")
        self.stateComboBox = QtWidgets.QComboBox(self.frame)
        self.stateComboBox.setGeometry(QtCore.QRect(160, 70, 161, 27))
        self.stateComboBox.setObjectName("stateComboBox")
        self.cityLabel = QtWidgets.QLabel(self.frame)
        self.cityLabel.setGeometry(QtCore.QRect(40, 120, 111, 31))
        self.cityLabel.setObjectName("cityLabel")
        self.dispensaryLabel = QtWidgets.QLabel(self.frame)
        self.dispensaryLabel.setGeometry(QtCore.QRect(40, 170, 111, 31))
        self.dispensaryLabel.setObjectName("dispensaryLabel")
        self.stateLabel = QtWidgets.QLabel(self.frame)
        self.stateLabel.setGeometry(QtCore.QRect(40, 70, 111, 31))
        self.stateLabel.setObjectName("stateLabel")
        self.searchByID = QtWidgets.QLineEdit(self.frame)
        self.searchByID.setGeometry(QtCore.QRect(40, 10, 281, 27))
        self.searchByID.setObjectName("searchByID")
        self.ORLabel = QtWidgets.QLabel(self.frame)
        self.ORLabel.setGeometry(QtCore.QRect(120, 40, 111, 31))
        self.ORLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ORLabel.setObjectName("ORLabel")
        self.removeButton = QtWidgets.QPushButton(selectHospital)
        self.removeButton.setGeometry(QtCore.QRect(140, 290, 80, 28))
        self.removeButton.setObjectName("removeButton")

        self.retranslateUi(selectHospital)
        QtCore.QMetaObject.connectSlotsByName(selectHospital)

    def retranslateUi(self, selectHospital):
        _translate = QtCore.QCoreApplication.translate
        selectHospital.setWindowTitle(_translate("selectHospital", " "))
        self.title.setText(_translate("selectHospital", "<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; font-weight:600; text-decoration: underline;\">Select Hospital</span></p></body></html>"))
        self.cityLabel.setText(_translate("selectHospital", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">City : </span></p></body></html>"))
        self.dispensaryLabel.setText(_translate("selectHospital", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Hospital</span></p></body></html>"))
        self.stateLabel.setText(_translate("selectHospital", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">State : </span></p></body></html>"))
        self.searchByID.setPlaceholderText(_translate("selectHospital", "Search by Hospital ID"))
        self.ORLabel.setText(_translate("selectHospital", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">OR</span></p></body></html>"))
        self.removeButton.setText(_translate("selectHospital", "SELECT"))

