# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'doctorList.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_doctorList(object):
    def setupUi(self, doctorList):
        doctorList.setObjectName("doctorList")
        doctorList.resize(640, 539)
        self.frame = QtWidgets.QFrame(doctorList)
        self.frame.setGeometry(QtCore.QRect(10, 50, 621, 421))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(10, 41, 601, 371))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(10, 10, 321, 25))
        self.comboBox.setObjectName("comboBox")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(510, 10, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.okbutton = QtWidgets.QPushButton(doctorList)
        self.okbutton.setGeometry(QtCore.QRect(260, 480, 89, 25))
        self.okbutton.setObjectName("okbutton")
        self.titleLabel = QtWidgets.QLabel(doctorList)
        self.titleLabel.setGeometry(QtCore.QRect(160, 0, 301, 41))
        self.titleLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.titleLabel.setObjectName("titleLabel")

        self.retranslateUi(doctorList)
        QtCore.QMetaObject.connectSlotsByName(doctorList)

    def retranslateUi(self, doctorList):
        _translate = QtCore.QCoreApplication.translate
        doctorList.setWindowTitle(_translate("doctorList", "Doctors"))
        self.pushButton.setText(_translate("doctorList", "PushButton"))
        self.okbutton.setText(_translate("doctorList", "close"))
        self.titleLabel.setText(_translate("doctorList", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; text-decoration: underline;\">Search Tests</span></p></body></html>"))

