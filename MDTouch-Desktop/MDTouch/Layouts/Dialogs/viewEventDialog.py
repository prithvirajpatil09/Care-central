# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewEventDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_hospitalMyProfileDialog(object):
    def setupUi(self, hospitalMyProfileDialog):
        hospitalMyProfileDialog.setObjectName("hospitalMyProfileDialog")
        hospitalMyProfileDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        hospitalMyProfileDialog.resize(484, 235)
        self.myEvents = QtWidgets.QPushButton(hospitalMyProfileDialog)
        self.myEvents.setGeometry(QtCore.QRect(80, 10, 120, 120))
        self.myEvents.setMaximumSize(QtCore.QSize(120, 120))
        self.myEvents.setStyleSheet("border:none;")
        self.myEvents.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Images/add_event.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.myEvents.setIcon(icon)
        self.myEvents.setIconSize(QtCore.QSize(100, 100))
        self.myEvents.setObjectName("myEvents")
        self.allEvents = QtWidgets.QPushButton(hospitalMyProfileDialog)
        self.allEvents.setGeometry(QtCore.QRect(280, 10, 120, 120))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.allEvents.sizePolicy().hasHeightForWidth())
        self.allEvents.setSizePolicy(sizePolicy)
        self.allEvents.setMaximumSize(QtCore.QSize(120, 120))
        self.allEvents.setStyleSheet("border:none;")
        self.allEvents.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../Images/search_hospital.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.allEvents.setIcon(icon1)
        self.allEvents.setIconSize(QtCore.QSize(100, 100))
        self.allEvents.setObjectName("allEvents")
        self.allEventsLabel = QtWidgets.QLabel(hospitalMyProfileDialog)
        self.allEventsLabel.setGeometry(QtCore.QRect(280, 120, 126, 78))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.allEventsLabel.sizePolicy().hasHeightForWidth())
        self.allEventsLabel.setSizePolicy(sizePolicy)
        self.allEventsLabel.setObjectName("allEventsLabel")
        self.myEventLabel = QtWidgets.QLabel(hospitalMyProfileDialog)
        self.myEventLabel.setGeometry(QtCore.QRect(70, 120, 126, 78))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.myEventLabel.sizePolicy().hasHeightForWidth())
        self.myEventLabel.setSizePolicy(sizePolicy)
        self.myEventLabel.setObjectName("myEventLabel")

        self.retranslateUi(hospitalMyProfileDialog)
        QtCore.QMetaObject.connectSlotsByName(hospitalMyProfileDialog)

    def retranslateUi(self, hospitalMyProfileDialog):
        _translate = QtCore.QCoreApplication.translate
        hospitalMyProfileDialog.setWindowTitle(_translate("hospitalMyProfileDialog", "Profiles"))
        self.allEventsLabel.setText(_translate("hospitalMyProfileDialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; font-weight:600; text-decoration: underline;\">All</span></p><p align=\"center\"><span style=\" font-size:15pt; font-weight:600; text-decoration: underline;\">Events</span></p></body></html>"))
        self.myEventLabel.setText(_translate("hospitalMyProfileDialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; font-weight:600; text-decoration: underline;\">My</span></p><p align=\"center\"><span style=\" font-size:15pt; font-weight:600; text-decoration: underline;\">Events</span></p><p align=\"center\"><br/></p></body></html>"))

