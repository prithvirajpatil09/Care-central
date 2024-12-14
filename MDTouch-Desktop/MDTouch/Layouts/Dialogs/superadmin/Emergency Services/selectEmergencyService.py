# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectEmergencyService.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_selectEmergencyService(object):
    def setupUi(self, selectEmergencyService):
        selectEmergencyService.setObjectName("selectEmergencyService")
        selectEmergencyService.resize(415, 313)
        self.title = QtWidgets.QLabel(selectEmergencyService)
        self.title.setGeometry(QtCore.QRect(10, 0, 391, 51))
        self.title.setObjectName("title")
        self.frame = QtWidgets.QFrame(selectEmergencyService)
        self.frame.setGeometry(QtCore.QRect(10, 60, 391, 211))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.cityComboBox = QtWidgets.QComboBox(self.frame)
        self.cityComboBox.setGeometry(QtCore.QRect(200, 120, 161, 27))
        self.cityComboBox.setObjectName("cityComboBox")
        self.emergencyServiceComboBox = QtWidgets.QComboBox(self.frame)
        self.emergencyServiceComboBox.setGeometry(QtCore.QRect(200, 160, 161, 27))
        self.emergencyServiceComboBox.setObjectName("emergencyServiceComboBox")
        self.stateComboBox = QtWidgets.QComboBox(self.frame)
        self.stateComboBox.setGeometry(QtCore.QRect(200, 80, 161, 27))
        self.stateComboBox.setObjectName("stateComboBox")
        self.cityLabel = QtWidgets.QLabel(self.frame)
        self.cityLabel.setGeometry(QtCore.QRect(20, 120, 111, 31))
        self.cityLabel.setObjectName("cityLabel")
        self.emergencyServiceLabel = QtWidgets.QLabel(self.frame)
        self.emergencyServiceLabel.setGeometry(QtCore.QRect(20, 160, 161, 31))
        self.emergencyServiceLabel.setObjectName("emergencyServiceLabel")
        self.stateLabel = QtWidgets.QLabel(self.frame)
        self.stateLabel.setGeometry(QtCore.QRect(20, 80, 111, 31))
        self.stateLabel.setObjectName("stateLabel")
        self.ORLabel = QtWidgets.QLabel(self.frame)
        self.ORLabel.setGeometry(QtCore.QRect(140, 40, 111, 31))
        self.ORLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ORLabel.setObjectName("ORLabel")
        self.searchByID = QtWidgets.QLineEdit(self.frame)
        self.searchByID.setGeometry(QtCore.QRect(20, 10, 341, 27))
        self.searchByID.setObjectName("searchByID")
        self.selectButton = QtWidgets.QPushButton(selectEmergencyService)
        self.selectButton.setGeometry(QtCore.QRect(170, 280, 80, 28))
        self.selectButton.setObjectName("selectButton")

        self.retranslateUi(selectEmergencyService)
        QtCore.QMetaObject.connectSlotsByName(selectEmergencyService)

    def retranslateUi(self, selectEmergencyService):
        _translate = QtCore.QCoreApplication.translate
        selectEmergencyService.setWindowTitle(_translate("selectEmergencyService", " "))
        self.title.setText(_translate("selectEmergencyService", "<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; font-weight:600; text-decoration: underline;\">Select Emergency Service</span></p></body></html>"))
        self.cityLabel.setText(_translate("selectEmergencyService", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">City : </span></p></body></html>"))
        self.emergencyServiceLabel.setText(_translate("selectEmergencyService", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Emergency Service :</span></p></body></html>"))
        self.stateLabel.setText(_translate("selectEmergencyService", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">State : </span></p></body></html>"))
        self.ORLabel.setText(_translate("selectEmergencyService", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">OR</span></p></body></html>"))
        self.searchByID.setPlaceholderText(_translate("selectEmergencyService", "Search by Emergency Service ID"))
        self.selectButton.setText(_translate("selectEmergencyService", "SELECT"))

