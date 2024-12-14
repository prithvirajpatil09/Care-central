# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'diseaseList.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DiseaseList(object):
    def setupUi(self, DiseaseList):
        DiseaseList.setObjectName("DiseaseList")
        DiseaseList.resize(640, 480)
        self.frame = QtWidgets.QFrame(DiseaseList)
        self.frame.setGeometry(QtCore.QRect(10, 10, 621, 421))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.diseaseLabel = QtWidgets.QLabel(self.frame)
        self.diseaseLabel.setGeometry(QtCore.QRect(250, 0, 131, 41))
        self.diseaseLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.diseaseLabel.setObjectName("diseaseLabel")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(10, 91, 601, 321))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.stateComboBox = QtWidgets.QComboBox(self.frame)
        self.stateComboBox.setGeometry(QtCore.QRect(10, 50, 221, 25))
        self.stateComboBox.setObjectName("stateComboBox")
        self.cityComboBox = QtWidgets.QComboBox(self.frame)
        self.cityComboBox.setGeometry(QtCore.QRect(240, 50, 221, 25))
        self.cityComboBox.setObjectName("cityComboBox")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(470, 50, 141, 25))
        self.pushButton.setObjectName("pushButton")
        self.okbutton = QtWidgets.QPushButton(DiseaseList)
        self.okbutton.setGeometry(QtCore.QRect(280, 440, 89, 25))
        self.okbutton.setObjectName("okbutton")

        self.retranslateUi(DiseaseList)
        QtCore.QMetaObject.connectSlotsByName(DiseaseList)

    def retranslateUi(self, DiseaseList):
        _translate = QtCore.QCoreApplication.translate
        DiseaseList.setWindowTitle(_translate("DiseaseList", "Disease"))
        self.diseaseLabel.setText(_translate("DiseaseList", "Disease"))
        self.pushButton.setText(_translate("DiseaseList", "Search"))
        self.okbutton.setText(_translate("DiseaseList", "close"))

