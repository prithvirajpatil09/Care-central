# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bloodDonationList.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_donationList(object):
    def setupUi(self, donationList):
        donationList.setObjectName("donationList")
        donationList.resize(640, 480)
        self.frame = QtWidgets.QFrame(donationList)
        self.frame.setGeometry(QtCore.QRect(10, 10, 621, 421))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.wasteRecordLabel = QtWidgets.QLabel(self.frame)
        self.wasteRecordLabel.setGeometry(QtCore.QRect(220, 0, 221, 41))
        self.wasteRecordLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.wasteRecordLabel.setObjectName("wasteRecordLabel")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(10, 41, 601, 371))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.closebutton = QtWidgets.QPushButton(donationList)
        self.closebutton.setGeometry(QtCore.QRect(530, 440, 89, 25))
        self.closebutton.setObjectName("closebutton")

        self.retranslateUi(donationList)
        QtCore.QMetaObject.connectSlotsByName(donationList)

    def retranslateUi(self, donationList):
        _translate = QtCore.QCoreApplication.translate
        donationList.setWindowTitle(_translate("donationList", "Records"))
        self.wasteRecordLabel.setText(_translate("donationList", "Donation records"))
        self.closebutton.setText(_translate("donationList", "close"))

