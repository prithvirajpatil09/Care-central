# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pendingAppointmentDoctorDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_pendingAppointmentDoctor(object):
    def setupUi(self, pendingAppointmentDoctor):
        pendingAppointmentDoctor.setObjectName("pendingAppointmentDoctor")
        pendingAppointmentDoctor.resize(636, 480)
        self.frame = QtWidgets.QFrame(pendingAppointmentDoctor)
        self.frame.setGeometry(QtCore.QRect(10, 10, 621, 421))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.title = QtWidgets.QLabel(self.frame)
        self.title.setGeometry(QtCore.QRect(180, 0, 251, 41))
        self.title.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.title.setObjectName("title")
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
        self.okButton = QtWidgets.QPushButton(pendingAppointmentDoctor)
        self.okButton.setGeometry(QtCore.QRect(530, 440, 89, 25))
        self.okButton.setObjectName("okButton")

        self.retranslateUi(pendingAppointmentDoctor)
        QtCore.QMetaObject.connectSlotsByName(pendingAppointmentDoctor)

    def retranslateUi(self, pendingAppointmentDoctor):
        _translate = QtCore.QCoreApplication.translate
        pendingAppointmentDoctor.setWindowTitle(_translate("pendingAppointmentDoctor", "Appointments"))
        self.title.setText(_translate("pendingAppointmentDoctor", "Pending Appointments"))
        self.okButton.setText(_translate("pendingAppointmentDoctor", "close"))

