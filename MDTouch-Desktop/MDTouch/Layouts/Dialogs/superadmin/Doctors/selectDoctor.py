# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectDoctor.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_selectDoctor(object):
    def setupUi(self, selectDoctor):
        selectDoctor.setObjectName("selectDoctor")
        selectDoctor.resize(380, 407)
        selectDoctor.setWindowTitle("")
        self.title = QtWidgets.QLabel(selectDoctor)
        self.title.setGeometry(QtCore.QRect(30, 0, 331, 51))
        self.title.setObjectName("title")
        self.frame = QtWidgets.QFrame(selectDoctor)
        self.frame.setGeometry(QtCore.QRect(10, 60, 351, 291))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.cityComboBox = QtWidgets.QComboBox(self.frame)
        self.cityComboBox.setGeometry(QtCore.QRect(160, 140, 161, 27))
        self.cityComboBox.setObjectName("cityComboBox")
        self.doctorComboBox = QtWidgets.QComboBox(self.frame)
        self.doctorComboBox.setGeometry(QtCore.QRect(160, 240, 161, 27))
        self.doctorComboBox.setObjectName("doctorComboBox")
        self.stateComboBox = QtWidgets.QComboBox(self.frame)
        self.stateComboBox.setGeometry(QtCore.QRect(160, 90, 161, 27))
        self.stateComboBox.setObjectName("stateComboBox")
        self.cityLabel = QtWidgets.QLabel(self.frame)
        self.cityLabel.setGeometry(QtCore.QRect(40, 140, 111, 31))
        self.cityLabel.setObjectName("cityLabel")
        self.bloodBankLabel = QtWidgets.QLabel(self.frame)
        self.bloodBankLabel.setGeometry(QtCore.QRect(40, 240, 111, 31))
        self.bloodBankLabel.setObjectName("bloodBankLabel")
        self.stateLabel = QtWidgets.QLabel(self.frame)
        self.stateLabel.setGeometry(QtCore.QRect(40, 90, 111, 31))
        self.stateLabel.setObjectName("stateLabel")
        self.ORLabel = QtWidgets.QLabel(self.frame)
        self.ORLabel.setGeometry(QtCore.QRect(130, 50, 111, 31))
        self.ORLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ORLabel.setObjectName("ORLabel")
        self.searchByID = QtWidgets.QLineEdit(self.frame)
        self.searchByID.setGeometry(QtCore.QRect(40, 20, 281, 27))
        self.searchByID.setObjectName("searchByID")
        self.hospitalLabel = QtWidgets.QLabel(self.frame)
        self.hospitalLabel.setGeometry(QtCore.QRect(40, 190, 111, 31))
        self.hospitalLabel.setObjectName("hospitalLabel")
        self.hospitalComboBox = QtWidgets.QComboBox(self.frame)
        self.hospitalComboBox.setGeometry(QtCore.QRect(160, 190, 161, 27))
        self.hospitalComboBox.setObjectName("hospitalComboBox")
        self.selectButton_2 = QtWidgets.QPushButton(selectDoctor)
        self.selectButton_2.setGeometry(QtCore.QRect(140, 360, 80, 28))
        self.selectButton_2.setObjectName("selectButton_2")

        self.retranslateUi(selectDoctor)
        QtCore.QMetaObject.connectSlotsByName(selectDoctor)

    def retranslateUi(self, selectDoctor):
        _translate = QtCore.QCoreApplication.translate
        self.title.setText(_translate("selectDoctor", "<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; font-weight:600; text-decoration: underline;\">Select Doctor</span></p></body></html>"))
        self.cityLabel.setText(_translate("selectDoctor", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">City : </span></p></body></html>"))
        self.bloodBankLabel.setText(_translate("selectDoctor", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Doctor :</span></p></body></html>"))
        self.stateLabel.setText(_translate("selectDoctor", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">State : </span></p></body></html>"))
        self.ORLabel.setText(_translate("selectDoctor", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">OR</span></p></body></html>"))
        self.searchByID.setPlaceholderText(_translate("selectDoctor", "Search by Doctor ID"))
        self.hospitalLabel.setText(_translate("selectDoctor", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Hospital : </span></p></body></html>"))
        self.selectButton_2.setText(_translate("selectDoctor", "SELECT"))

