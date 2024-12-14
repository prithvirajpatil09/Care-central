# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectAdmin.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_selectAdmin(object):
    def setupUi(self, selectAdmin):
        selectAdmin.setObjectName("selectAdmin")
        selectAdmin.resize(333, 408)
        selectAdmin.setWindowTitle("")
        self.title = QtWidgets.QLabel(selectAdmin)
        self.title.setGeometry(QtCore.QRect(40, 0, 261, 51))
        self.title.setObjectName("title")
        self.frame = QtWidgets.QFrame(selectAdmin)
        self.frame.setGeometry(QtCore.QRect(10, 60, 311, 291))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.cityComboBox = QtWidgets.QComboBox(self.frame)
        self.cityComboBox.setGeometry(QtCore.QRect(120, 140, 161, 27))
        self.cityComboBox.setObjectName("cityComboBox")
        self.hospitalComboBox = QtWidgets.QComboBox(self.frame)
        self.hospitalComboBox.setGeometry(QtCore.QRect(120, 190, 161, 27))
        self.hospitalComboBox.setObjectName("hospitalComboBox")
        self.stateComboBox = QtWidgets.QComboBox(self.frame)
        self.stateComboBox.setGeometry(QtCore.QRect(120, 90, 161, 27))
        self.stateComboBox.setObjectName("stateComboBox")
        self.cityLabel = QtWidgets.QLabel(self.frame)
        self.cityLabel.setGeometry(QtCore.QRect(30, 140, 111, 31))
        self.cityLabel.setObjectName("cityLabel")
        self.hospitalLabel = QtWidgets.QLabel(self.frame)
        self.hospitalLabel.setGeometry(QtCore.QRect(30, 190, 111, 31))
        self.hospitalLabel.setObjectName("hospitalLabel")
        self.stateLabel = QtWidgets.QLabel(self.frame)
        self.stateLabel.setGeometry(QtCore.QRect(30, 90, 111, 31))
        self.stateLabel.setObjectName("stateLabel")
        self.adminLabel = QtWidgets.QLabel(self.frame)
        self.adminLabel.setGeometry(QtCore.QRect(30, 240, 111, 31))
        self.adminLabel.setObjectName("adminLabel")
        self.adminComboBox = QtWidgets.QComboBox(self.frame)
        self.adminComboBox.setGeometry(QtCore.QRect(120, 240, 161, 27))
        self.adminComboBox.setObjectName("adminComboBox")
        self.ORLabel = QtWidgets.QLabel(self.frame)
        self.ORLabel.setGeometry(QtCore.QRect(110, 50, 111, 31))
        self.ORLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ORLabel.setObjectName("ORLabel")
        self.searchByID = QtWidgets.QLineEdit(self.frame)
        self.searchByID.setGeometry(QtCore.QRect(20, 20, 261, 27))
        self.searchByID.setObjectName("searchByID")
        self.selectButton = QtWidgets.QPushButton(selectAdmin)
        self.selectButton.setGeometry(QtCore.QRect(140, 360, 80, 28))
        self.selectButton.setObjectName("selectButton")

        self.retranslateUi(selectAdmin)
        QtCore.QMetaObject.connectSlotsByName(selectAdmin)

    def retranslateUi(self, selectAdmin):
        _translate = QtCore.QCoreApplication.translate
        self.title.setText(_translate("selectAdmin", "<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; font-weight:600; text-decoration: underline;\">Select Admin</span></p></body></html>"))
        self.cityLabel.setText(_translate("selectAdmin", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">City : </span></p></body></html>"))
        self.hospitalLabel.setText(_translate("selectAdmin", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Hospital : </span></p></body></html>"))
        self.stateLabel.setText(_translate("selectAdmin", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">State : </span></p></body></html>"))
        self.adminLabel.setText(_translate("selectAdmin", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Admin :</span></p></body></html>"))
        self.ORLabel.setText(_translate("selectAdmin", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">OR</span></p></body></html>"))
        self.searchByID.setPlaceholderText(_translate("selectAdmin", "Search by Admin Id"))
        self.selectButton.setText(_translate("selectAdmin", "SELECT"))

