# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addDoctor.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_addDoctor(object):
    def setupUi(self, addDoctor):
        addDoctor.setObjectName("addDoctor")
        addDoctor.resize(750, 481)
        addDoctor.setWindowTitle("")
        self.title = QtWidgets.QLabel(addDoctor)
        self.title.setGeometry(QtCore.QRect(250, 0, 261, 51))
        self.title.setObjectName("title")
        self.addButton = QtWidgets.QPushButton(addDoctor)
        self.addButton.setGeometry(QtCore.QRect(300, 420, 131, 41))
        self.addButton.setObjectName("addButton")
        self.frame = QtWidgets.QFrame(addDoctor)
        self.frame.setGeometry(QtCore.QRect(10, 60, 731, 341))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.firstNameLabel = QtWidgets.QLabel(self.frame)
        self.firstNameLabel.setGeometry(QtCore.QRect(10, 20, 121, 41))
        self.firstNameLabel.setObjectName("firstNameLabel")
        self.firstName = QtWidgets.QLineEdit(self.frame)
        self.firstName.setGeometry(QtCore.QRect(120, 20, 211, 41))
        self.firstName.setObjectName("firstName")
        self.uploadImage = QtWidgets.QPushButton(self.frame)
        self.uploadImage.setGeometry(QtCore.QRect(90, 280, 131, 41))
        self.uploadImage.setObjectName("uploadImage")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(50, 70, 221, 201))
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet("image: url(:/doctor_icon.png);\n"
"border-style:solid;\n"
"border-width:1px;\n"
"border-color: rgb(0, 0, 0);")
        self.widget.setObjectName("widget")
        self.lastNameLabel = QtWidgets.QLabel(self.frame)
        self.lastNameLabel.setGeometry(QtCore.QRect(350, 20, 111, 41))
        self.lastNameLabel.setObjectName("lastNameLabel")
        self.lastName = QtWidgets.QLineEdit(self.frame)
        self.lastName.setGeometry(QtCore.QRect(460, 20, 211, 41))
        self.lastName.setObjectName("lastName")
        self.stateLabel = QtWidgets.QLabel(self.frame)
        self.stateLabel.setGeometry(QtCore.QRect(350, 90, 111, 31))
        self.stateLabel.setObjectName("stateLabel")
        self.cityLabel = QtWidgets.QLabel(self.frame)
        self.cityLabel.setGeometry(QtCore.QRect(350, 160, 111, 31))
        self.cityLabel.setObjectName("cityLabel")
        self.hospitalLabel = QtWidgets.QLabel(self.frame)
        self.hospitalLabel.setGeometry(QtCore.QRect(350, 240, 111, 31))
        self.hospitalLabel.setObjectName("hospitalLabel")
        self.stateComboBox = QtWidgets.QComboBox(self.frame)
        self.stateComboBox.setGeometry(QtCore.QRect(460, 90, 161, 27))
        self.stateComboBox.setObjectName("stateComboBox")
        self.cityComboBox = QtWidgets.QComboBox(self.frame)
        self.cityComboBox.setGeometry(QtCore.QRect(460, 160, 161, 27))
        self.cityComboBox.setObjectName("cityComboBox")
        self.hospitalComboBox = QtWidgets.QComboBox(self.frame)
        self.hospitalComboBox.setGeometry(QtCore.QRect(460, 240, 161, 27))
        self.hospitalComboBox.setObjectName("hospitalComboBox")

        self.retranslateUi(addDoctor)
        QtCore.QMetaObject.connectSlotsByName(addDoctor)

    def retranslateUi(self, addDoctor):
        _translate = QtCore.QCoreApplication.translate
        self.title.setText(_translate("addDoctor", "<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; font-weight:600; text-decoration: underline;\">Add Doctor</span></p></body></html>"))
        self.addButton.setText(_translate("addDoctor", "ADD"))
        self.firstNameLabel.setText(_translate("addDoctor", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">First Name : </span></p></body></html>"))
        self.uploadImage.setText(_translate("addDoctor", "Upload Image"))
        self.lastNameLabel.setText(_translate("addDoctor", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Last Name : </span></p></body></html>"))
        self.stateLabel.setText(_translate("addDoctor", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">State : </span></p></body></html>"))
        self.cityLabel.setText(_translate("addDoctor", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">City : </span></p></body></html>"))
        self.hospitalLabel.setText(_translate("addDoctor", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Hospital : </span></p></body></html>"))

import img_rc
