# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectDispensary.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_removeDispensary(object):
    def setupUi(self, removeDispensary):
        removeDispensary.setObjectName("removeDispensary")
        removeDispensary.resize(362, 330)
        self.title = QtWidgets.QLabel(removeDispensary)
        self.title.setGeometry(QtCore.QRect(30, 0, 321, 51))
        self.title.setObjectName("title")
        self.frame = QtWidgets.QFrame(removeDispensary)
        self.frame.setGeometry(QtCore.QRect(10, 60, 341, 211))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.cityComboBox = QtWidgets.QComboBox(self.frame)
        self.cityComboBox.setGeometry(QtCore.QRect(160, 120, 161, 27))
        self.cityComboBox.setObjectName("cityComboBox")
        self.dispensaryComboBox = QtWidgets.QComboBox(self.frame)
        self.dispensaryComboBox.setGeometry(QtCore.QRect(160, 170, 161, 27))
        self.dispensaryComboBox.setObjectName("dispensaryComboBox")
        self.stateComboBox = QtWidgets.QComboBox(self.frame)
        self.stateComboBox.setGeometry(QtCore.QRect(160, 70, 161, 27))
        self.stateComboBox.setObjectName("stateComboBox")
        self.cityLabel = QtWidgets.QLabel(self.frame)
        self.cityLabel.setGeometry(QtCore.QRect(40, 120, 111, 31))
        self.cityLabel.setObjectName("cityLabel")
        self.dispensaryLabel = QtWidgets.QLabel(self.frame)
        self.dispensaryLabel.setGeometry(QtCore.QRect(40, 170, 111, 31))
        self.dispensaryLabel.setObjectName("dispensaryLabel")
        self.stateLabel = QtWidgets.QLabel(self.frame)
        self.stateLabel.setGeometry(QtCore.QRect(40, 70, 111, 31))
        self.stateLabel.setObjectName("stateLabel")
        self.searchByID = QtWidgets.QLineEdit(self.frame)
        self.searchByID.setGeometry(QtCore.QRect(40, 10, 281, 27))
        self.searchByID.setObjectName("searchByID")
        self.ORLabel = QtWidgets.QLabel(self.frame)
        self.ORLabel.setGeometry(QtCore.QRect(120, 40, 111, 31))
        self.ORLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ORLabel.setObjectName("ORLabel")
        self.removeButton = QtWidgets.QPushButton(removeDispensary)
        self.removeButton.setGeometry(QtCore.QRect(140, 290, 80, 28))
        self.removeButton.setObjectName("removeButton")

        self.retranslateUi(removeDispensary)
        QtCore.QMetaObject.connectSlotsByName(removeDispensary)

    def retranslateUi(self, removeDispensary):
        _translate = QtCore.QCoreApplication.translate
        removeDispensary.setWindowTitle(_translate("removeDispensary", " "))
        self.title.setText(_translate("removeDispensary", "<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; font-weight:600; text-decoration: underline;\">Select Dispensary</span></p></body></html>"))
        self.cityLabel.setText(_translate("removeDispensary", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">City : </span></p></body></html>"))
        self.dispensaryLabel.setText(_translate("removeDispensary", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Dispensary :</span></p></body></html>"))
        self.stateLabel.setText(_translate("removeDispensary", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">State : </span></p></body></html>"))
        self.searchByID.setPlaceholderText(_translate("removeDispensary", "Search by Dispensary ID"))
        self.ORLabel.setText(_translate("removeDispensary", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">OR</span></p></body></html>"))
        self.removeButton.setText(_translate("removeDispensary", "SELECT"))

