# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testcenterStats.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_testcenterStats(object):
    def setupUi(self, testcenterStats):
        testcenterStats.setObjectName("testcenterStats")
        testcenterStats.resize(355, 461)
        self.titleLabel = QtWidgets.QLabel(testcenterStats)
        self.titleLabel.setGeometry(QtCore.QRect(0, 10, 361, 41))
        self.titleLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.titleLabel.setObjectName("titleLabel")
        self.close = QtWidgets.QPushButton(testcenterStats)
        self.close.setGeometry(QtCore.QRect(130, 420, 89, 25))
        self.close.setObjectName("close")
        self.searchtcButton = QtWidgets.QPushButton(testcenterStats)
        self.searchtcButton.setGeometry(QtCore.QRect(10, 190, 161, 25))
        self.searchtcButton.setObjectName("searchtcButton")
        self.allBillsButton = QtWidgets.QPushButton(testcenterStats)
        self.allBillsButton.setGeometry(QtCore.QRect(180, 190, 161, 25))
        self.allBillsButton.setObjectName("allBillsButton")
        self.titleLabel_2 = QtWidgets.QLabel(testcenterStats)
        self.titleLabel_2.setGeometry(QtCore.QRect(0, 80, 241, 41))
        self.titleLabel_2.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.titleLabel_2.setObjectName("titleLabel_2")
        self.titleLabel_3 = QtWidgets.QLabel(testcenterStats)
        self.titleLabel_3.setGeometry(QtCore.QRect(-40, 130, 241, 41))
        self.titleLabel_3.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.titleLabel_3.setObjectName("titleLabel_3")
        self.frame_2 = QtWidgets.QFrame(testcenterStats)
        self.frame_2.setGeometry(QtCore.QRect(10, 300, 341, 101))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.tcid = QtWidgets.QLineEdit(self.frame_2)
        self.tcid.setGeometry(QtCore.QRect(90, 10, 151, 25))
        self.tcid.setObjectName("tcid")
        self.goToProfile = QtWidgets.QPushButton(self.frame_2)
        self.goToProfile.setGeometry(QtCore.QRect(90, 60, 151, 25))
        self.goToProfile.setObjectName("goToProfile")
        self.billingstatsButton = QtWidgets.QPushButton(testcenterStats)
        self.billingstatsButton.setGeometry(QtCore.QRect(10, 250, 161, 25))
        self.billingstatsButton.setObjectName("billingstatsButton")
        self.locationstatsButton = QtWidgets.QPushButton(testcenterStats)
        self.locationstatsButton.setGeometry(QtCore.QRect(180, 250, 161, 25))
        self.locationstatsButton.setObjectName("locationstatsButton")
        self.tcRegistered = QtWidgets.QLabel(testcenterStats)
        self.tcRegistered.setGeometry(QtCore.QRect(250, 90, 67, 17))
        self.tcRegistered.setObjectName("tcRegistered")
        self.totalbills = QtWidgets.QLabel(testcenterStats)
        self.totalbills.setGeometry(QtCore.QRect(250, 140, 67, 17))
        self.totalbills.setObjectName("totalbills")

        self.retranslateUi(testcenterStats)
        QtCore.QMetaObject.connectSlotsByName(testcenterStats)

    def retranslateUi(self, testcenterStats):
        _translate = QtCore.QCoreApplication.translate
        testcenterStats.setWindowTitle(_translate("testcenterStats", "Stats"))
        self.titleLabel.setText(_translate("testcenterStats", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; text-decoration: underline;\">Test Center Stats</span></p><p align=\"center\"><br/></p></body></html>"))
        self.close.setText(_translate("testcenterStats", "close"))
        self.searchtcButton.setText(_translate("testcenterStats", "Search Test Centers"))
        self.allBillsButton.setText(_translate("testcenterStats", "All Test Bills"))
        self.titleLabel_2.setText(_translate("testcenterStats", "<html><head/><body><p align=\"center\">Test Center Registered :</p></body></html>"))
        self.titleLabel_3.setText(_translate("testcenterStats", "<html><head/><body><p align=\"center\">Total Test Bills:</p></body></html>"))
        self.tcid.setPlaceholderText(_translate("testcenterStats", "Enter TC ID"))
        self.goToProfile.setText(_translate("testcenterStats", "Go To Profile"))
        self.billingstatsButton.setText(_translate("testcenterStats", "Billing Stats"))
        self.locationstatsButton.setText(_translate("testcenterStats", "Location Stats"))
        self.tcRegistered.setText(_translate("testcenterStats", "TextLabel"))
        self.totalbills.setText(_translate("testcenterStats", "TextLabel"))

