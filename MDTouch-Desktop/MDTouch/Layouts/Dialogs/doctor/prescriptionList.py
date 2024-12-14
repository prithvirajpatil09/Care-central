# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prescriptionList.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_prescriptionList(object):
    def setupUi(self, prescriptionList):
        prescriptionList.setObjectName("prescriptionList")
        prescriptionList.resize(640, 480)
        self.frame = QtWidgets.QFrame(prescriptionList)
        self.frame.setGeometry(QtCore.QRect(10, 10, 621, 421))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.prescriptionListLabel = QtWidgets.QLabel(self.frame)
        self.prescriptionListLabel.setGeometry(QtCore.QRect(250, 0, 131, 41))
        self.prescriptionListLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.prescriptionListLabel.setObjectName("prescriptionListLabel")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(10, 41, 601, 371))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.okbutton = QtWidgets.QPushButton(prescriptionList)
        self.okbutton.setGeometry(QtCore.QRect(530, 440, 89, 25))
        self.okbutton.setObjectName("okbutton")

        self.retranslateUi(prescriptionList)
        QtCore.QMetaObject.connectSlotsByName(prescriptionList)

    def retranslateUi(self, prescriptionList):
        _translate = QtCore.QCoreApplication.translate
        prescriptionList.setWindowTitle(_translate("prescriptionList", "Notices"))
        self.prescriptionListLabel.setText(_translate("prescriptionList", "Prescriptions"))
        self.okbutton.setText(_translate("prescriptionList", "close"))

