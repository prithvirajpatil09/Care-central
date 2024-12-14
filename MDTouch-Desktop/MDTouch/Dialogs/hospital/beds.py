# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'beds.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_bedsDialog(object):
    def setupUi(self, bedsDialog):
        bedsDialog.setObjectName("bedsDialog")
        bedsDialog.resize(484, 214)
        self.bedRecords = QtWidgets.QPushButton(bedsDialog)
        self.bedRecords.setGeometry(QtCore.QRect(340, 10, 120, 120))
        self.bedRecords.setMaximumSize(QtCore.QSize(120, 120))
        self.bedRecords.setStyleSheet("border:none;")
        self.bedRecords.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Images/records.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bedRecords.setIcon(icon)
        self.bedRecords.setIconSize(QtCore.QSize(100, 100))
        self.bedRecords.setObjectName("bedRecords")
        self.bedRequestsLabel = QtWidgets.QLabel(bedsDialog)
        self.bedRequestsLabel.setGeometry(QtCore.QRect(175, 120, 126, 78))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bedRequestsLabel.sizePolicy().hasHeightForWidth())
        self.bedRequestsLabel.setSizePolicy(sizePolicy)
        self.bedRequestsLabel.setObjectName("bedRequestsLabel")
        self.bedRequests = QtWidgets.QPushButton(bedsDialog)
        self.bedRequests.setGeometry(QtCore.QRect(180, 10, 120, 120))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bedRequests.sizePolicy().hasHeightForWidth())
        self.bedRequests.setSizePolicy(sizePolicy)
        self.bedRequests.setMaximumSize(QtCore.QSize(120, 120))
        self.bedRequests.setStyleSheet("border:none;")
        self.bedRequests.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../Images/request.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bedRequests.setIcon(icon1)
        self.bedRequests.setIconSize(QtCore.QSize(100, 100))
        self.bedRequests.setObjectName("bedRequests")
        self.bedRecordsLabel = QtWidgets.QLabel(bedsDialog)
        self.bedRecordsLabel.setGeometry(QtCore.QRect(345, 120, 112, 78))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bedRecordsLabel.sizePolicy().hasHeightForWidth())
        self.bedRecordsLabel.setSizePolicy(sizePolicy)
        self.bedRecordsLabel.setObjectName("bedRecordsLabel")
        self.bedSystem = QtWidgets.QPushButton(bedsDialog)
        self.bedSystem.setGeometry(QtCore.QRect(20, 10, 120, 120))
        self.bedSystem.setMaximumSize(QtCore.QSize(120, 120))
        self.bedSystem.setStyleSheet("border:none;")
        self.bedSystem.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../Images/hospital_bed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bedSystem.setIcon(icon2)
        self.bedSystem.setIconSize(QtCore.QSize(100, 100))
        self.bedSystem.setObjectName("bedSystem")
        self.bedSystemLabel = QtWidgets.QLabel(bedsDialog)
        self.bedSystemLabel.setGeometry(QtCore.QRect(10, 120, 126, 78))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bedSystemLabel.sizePolicy().hasHeightForWidth())
        self.bedSystemLabel.setSizePolicy(sizePolicy)
        self.bedSystemLabel.setObjectName("bedSystemLabel")

        self.retranslateUi(bedsDialog)
        QtCore.QMetaObject.connectSlotsByName(bedsDialog)

    def retranslateUi(self, bedsDialog):
        _translate = QtCore.QCoreApplication.translate
        bedsDialog.setWindowTitle(_translate("bedsDialog", "Beds"))
        self.bedRequestsLabel.setText(_translate("bedsDialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; font-weight:600; text-decoration: underline;\">Bed<br>Requests</span></p></body></html>"))
        self.bedRecordsLabel.setText(_translate("bedsDialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; font-weight:600; text-decoration: underline;\">Bed<br>Records</span></p></body></html>"))
        self.bedSystemLabel.setText(_translate("bedsDialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; font-weight:600; text-decoration: underline;\">Bed<br>System</span></p></body></html>"))

