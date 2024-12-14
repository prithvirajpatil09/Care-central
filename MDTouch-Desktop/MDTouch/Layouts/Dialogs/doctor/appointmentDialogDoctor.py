# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'appointmentDialogDoctor.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_appointmentDoctorDialog(object):
    def setupUi(self, appointmentDoctorDialog):
        appointmentDoctorDialog.setObjectName("appointmentDoctorDialog")
        appointmentDoctorDialog.resize(484, 235)
        self.pending = QtWidgets.QPushButton(appointmentDoctorDialog)
        self.pending.setGeometry(QtCore.QRect(350, 10, 120, 120))
        self.pending.setMaximumSize(QtCore.QSize(120, 120))
        self.pending.setStyleSheet("border:none;")
        self.pending.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../Images/delete_event.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pending.setIcon(icon)
        self.pending.setIconSize(QtCore.QSize(100, 100))
        self.pending.setObjectName("pending")
        self.accepted = QtWidgets.QPushButton(appointmentDoctorDialog)
        self.accepted.setGeometry(QtCore.QRect(30, 10, 120, 120))
        self.accepted.setMaximumSize(QtCore.QSize(120, 120))
        self.accepted.setStyleSheet("border:none;")
        self.accepted.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../Images/add_event.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.accepted.setIcon(icon1)
        self.accepted.setIconSize(QtCore.QSize(100, 100))
        self.accepted.setObjectName("accepted")
        self.rejected = QtWidgets.QPushButton(appointmentDoctorDialog)
        self.rejected.setGeometry(QtCore.QRect(190, 10, 120, 120))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rejected.sizePolicy().hasHeightForWidth())
        self.rejected.setSizePolicy(sizePolicy)
        self.rejected.setMaximumSize(QtCore.QSize(120, 120))
        self.rejected.setStyleSheet("border:none;")
        self.rejected.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../../Images/search_hospital.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rejected.setIcon(icon2)
        self.rejected.setIconSize(QtCore.QSize(100, 100))
        self.rejected.setObjectName("rejected")
        self.pendingLabel = QtWidgets.QLabel(appointmentDoctorDialog)
        self.pendingLabel.setGeometry(QtCore.QRect(350, 120, 112, 78))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pendingLabel.sizePolicy().hasHeightForWidth())
        self.pendingLabel.setSizePolicy(sizePolicy)
        self.pendingLabel.setObjectName("pendingLabel")
        self.acceptedLabel = QtWidgets.QLabel(appointmentDoctorDialog)
        self.acceptedLabel.setGeometry(QtCore.QRect(20, 120, 126, 78))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.acceptedLabel.sizePolicy().hasHeightForWidth())
        self.acceptedLabel.setSizePolicy(sizePolicy)
        self.acceptedLabel.setObjectName("acceptedLabel")
        self.rejectedLabel = QtWidgets.QLabel(appointmentDoctorDialog)
        self.rejectedLabel.setGeometry(QtCore.QRect(190, 120, 126, 78))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rejectedLabel.sizePolicy().hasHeightForWidth())
        self.rejectedLabel.setSizePolicy(sizePolicy)
        self.rejectedLabel.setObjectName("rejectedLabel")

        self.retranslateUi(appointmentDoctorDialog)
        QtCore.QMetaObject.connectSlotsByName(appointmentDoctorDialog)

    def retranslateUi(self, appointmentDoctorDialog):
        _translate = QtCore.QCoreApplication.translate
        appointmentDoctorDialog.setWindowTitle(_translate("appointmentDoctorDialog", "Appointments"))
        self.pendingLabel.setText(_translate("appointmentDoctorDialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; font-weight:600; text-decoration: underline;\">Pending</span></p></body></html>"))
        self.acceptedLabel.setText(_translate("appointmentDoctorDialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; font-weight:600; text-decoration: underline;\">Accepted</span></p></body></html>"))
        self.rejectedLabel.setText(_translate("appointmentDoctorDialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; font-weight:600; text-decoration: underline;\">Rejected</span></p></body></html>"))

