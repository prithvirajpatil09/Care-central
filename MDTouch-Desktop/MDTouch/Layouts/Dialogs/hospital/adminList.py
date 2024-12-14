# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminList.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_adminList(object):
    def setupUi(self, adminList):
        adminList.setObjectName("adminList")
        adminList.resize(640, 480)
        self.frame = QtWidgets.QFrame(adminList)
        self.frame.setGeometry(QtCore.QRect(10, 10, 621, 421))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.adminListLabel = QtWidgets.QLabel(self.frame)
        self.adminListLabel.setGeometry(QtCore.QRect(250, 0, 131, 41))
        self.adminListLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.adminListLabel.setObjectName("adminListLabel")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(10, 41, 601, 371))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.okbutton = QtWidgets.QPushButton(adminList)
        self.okbutton.setGeometry(QtCore.QRect(530, 440, 89, 25))
        self.okbutton.setObjectName("okbutton")

        self.retranslateUi(adminList)
        QtCore.QMetaObject.connectSlotsByName(adminList)

    def retranslateUi(self, adminList):
        _translate = QtCore.QCoreApplication.translate
        adminList.setWindowTitle(_translate("adminList", "Admins"))
        self.adminListLabel.setText(_translate("adminList", "<html><head/><body><p><span style=\" text-decoration: underline;\">Admin List</span></p></body></html>"))
        self.okbutton.setText(_translate("adminList", "close"))

