# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wasteRecordsList.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_wasteRecordList(object):
    def setupUi(self, wasteRecordList):
        wasteRecordList.setObjectName("wasteRecordList")
        wasteRecordList.resize(640, 480)
        self.frame = QtWidgets.QFrame(wasteRecordList)
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
        self.closebutton = QtWidgets.QPushButton(wasteRecordList)
        self.closebutton.setGeometry(QtCore.QRect(530, 440, 89, 25))
        self.closebutton.setObjectName("closebutton")

        self.retranslateUi(wasteRecordList)
        QtCore.QMetaObject.connectSlotsByName(wasteRecordList)

    def retranslateUi(self, wasteRecordList):
        _translate = QtCore.QCoreApplication.translate
        wasteRecordList.setWindowTitle(_translate("wasteRecordList", "Records"))
        self.wasteRecordLabel.setText(_translate("wasteRecordList", "Waste Records"))
        self.closebutton.setText(_translate("wasteRecordList", "close"))

