# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hospitalMyProfileOption.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_hospitalMyProfileDialog(object):
    def setupUi(self, hospitalMyProfileDialog):
        hospitalMyProfileDialog.setObjectName("hospitalMyProfileDialog")
        hospitalMyProfileDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        hospitalMyProfileDialog.resize(484, 235)
        self.adminProfile = QtWidgets.QPushButton(hospitalMyProfileDialog)
        self.adminProfile.setGeometry(QtCore.QRect(80, 10, 120, 120))
        self.adminProfile.setMaximumSize(QtCore.QSize(120, 120))
        self.adminProfile.setStyleSheet("border:none;")
        self.adminProfile.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Images/add_event.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.adminProfile.setIcon(icon)
        self.adminProfile.setIconSize(QtCore.QSize(100, 100))
        self.adminProfile.setObjectName("adminProfile")
        self.hospitalProfile = QtWidgets.QPushButton(hospitalMyProfileDialog)
        self.hospitalProfile.setGeometry(QtCore.QRect(280, 10, 120, 120))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hospitalProfile.sizePolicy().hasHeightForWidth())
        self.hospitalProfile.setSizePolicy(sizePolicy)
        self.hospitalProfile.setMaximumSize(QtCore.QSize(120, 120))
        self.hospitalProfile.setStyleSheet("border:none;")
        self.hospitalProfile.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../Images/search_hospital.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.hospitalProfile.setIcon(icon1)
        self.hospitalProfile.setIconSize(QtCore.QSize(100, 100))
        self.hospitalProfile.setObjectName("hospitalProfile")
        self.hospitalProfileLabel = QtWidgets.QLabel(hospitalMyProfileDialog)
        self.hospitalProfileLabel.setGeometry(QtCore.QRect(280, 120, 126, 78))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hospitalProfileLabel.sizePolicy().hasHeightForWidth())
        self.hospitalProfileLabel.setSizePolicy(sizePolicy)
        self.hospitalProfileLabel.setObjectName("hospitalProfileLabel")
        self.adminProfileLabel = QtWidgets.QLabel(hospitalMyProfileDialog)
        self.adminProfileLabel.setGeometry(QtCore.QRect(70, 120, 126, 78))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.adminProfileLabel.sizePolicy().hasHeightForWidth())
        self.adminProfileLabel.setSizePolicy(sizePolicy)
        self.adminProfileLabel.setObjectName("adminProfileLabel")

        self.retranslateUi(hospitalMyProfileDialog)
        QtCore.QMetaObject.connectSlotsByName(hospitalMyProfileDialog)

    def retranslateUi(self, hospitalMyProfileDialog):
        _translate = QtCore.QCoreApplication.translate
        hospitalMyProfileDialog.setWindowTitle(_translate("hospitalMyProfileDialog", "Profiles"))
        self.hospitalProfileLabel.setText(_translate("hospitalMyProfileDialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; font-weight:600; text-decoration: underline;\">Hospital</span></p><p align=\"center\"><span style=\" font-size:15pt; font-weight:600; text-decoration: underline;\">Profile</span></p></body></html>"))
        self.adminProfileLabel.setText(_translate("hospitalMyProfileDialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; font-weight:600; text-decoration: underline;\">Admin<br/>Profile</span></p></body></html>"))

