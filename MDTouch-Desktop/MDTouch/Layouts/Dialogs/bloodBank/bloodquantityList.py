# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bloodquantityList.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_bloodquanityList(object):
    def setupUi(self, bloodquanityList):
        bloodquanityList.setObjectName("bloodquanityList")
        bloodquanityList.resize(291, 420)
        self.frame = QtWidgets.QFrame(bloodquanityList)
        self.frame.setGeometry(QtCore.QRect(10, 10, 271, 401))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.titlelabel = QtWidgets.QLabel(self.frame)
        self.titlelabel.setGeometry(QtCore.QRect(30, 10, 201, 41))
        self.titlelabel.setObjectName("titlelabel")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(30, 60, 211, 271))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(8)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 0, item)
        self.exit = QtWidgets.QPushButton(self.frame)
        self.exit.setGeometry(QtCore.QRect(80, 350, 89, 25))
        self.exit.setObjectName("exit")

        self.retranslateUi(bloodquanityList)
        QtCore.QMetaObject.connectSlotsByName(bloodquanityList)

    def retranslateUi(self, bloodquanityList):
        _translate = QtCore.QCoreApplication.translate
        bloodquanityList.setWindowTitle(_translate("bloodquanityList", "Form"))
        self.titlelabel.setText(_translate("bloodquanityList", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">Blood Quantity</span></p></body></html>"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("bloodquanityList", "Blood Type"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("bloodquanityList", "Quantity"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("bloodquanityList", "A+"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("bloodquanityList", "A-"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("bloodquanityList", "B+"))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("bloodquanityList", "B-"))
        item = self.tableWidget.item(4, 0)
        item.setText(_translate("bloodquanityList", "AB+"))
        item = self.tableWidget.item(5, 0)
        item.setText(_translate("bloodquanityList", "AB-"))
        item = self.tableWidget.item(6, 0)
        item.setText(_translate("bloodquanityList", "O+"))
        item = self.tableWidget.item(7, 0)
        item.setText(_translate("bloodquanityList", "O-"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.exit.setText(_translate("bloodquanityList", "Exit"))
