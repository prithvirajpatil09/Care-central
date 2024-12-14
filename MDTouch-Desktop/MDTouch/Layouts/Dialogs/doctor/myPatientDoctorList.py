# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myPatientDoctorList.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_myPatientDoctorList(object):
    def setupUi(self, myPatientDoctorList):
        myPatientDoctorList.setObjectName("myPatientDoctorList")
        myPatientDoctorList.resize(636, 480)
        self.frame = QtWidgets.QFrame(myPatientDoctorList)
        self.frame.setGeometry(QtCore.QRect(10, 10, 621, 421))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.patientLabel = QtWidgets.QLabel(self.frame)
        self.patientLabel.setGeometry(QtCore.QRect(230, 0, 191, 41))
        self.patientLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.patientLabel.setObjectName("patientLabel")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(10, 41, 601, 371))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.okButton = QtWidgets.QPushButton(myPatientDoctorList)
        self.okButton.setGeometry(QtCore.QRect(530, 440, 89, 25))
        self.okButton.setObjectName("okButton")

        self.retranslateUi(myPatientDoctorList)
        QtCore.QMetaObject.connectSlotsByName(myPatientDoctorList)

    def retranslateUi(self, myPatientDoctorList):
        _translate = QtCore.QCoreApplication.translate
        myPatientDoctorList.setWindowTitle(_translate("myPatientDoctorList", "My Patient List"))
        self.patientLabel.setText(_translate("myPatientDoctorList", "My Patients"))
        self.okButton.setText(_translate("myPatientDoctorList", "close"))

