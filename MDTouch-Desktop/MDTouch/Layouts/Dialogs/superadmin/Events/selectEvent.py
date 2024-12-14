# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectEvent.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_selectEvent(object):
    def setupUi(self, selectEvent):
        selectEvent.setObjectName("selectEvent")
        selectEvent.resize(323, 315)
        self.frame = QtWidgets.QFrame(selectEvent)
        self.frame.setGeometry(QtCore.QRect(10, 60, 301, 211))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.cityComboBox = QtWidgets.QComboBox(self.frame)
        self.cityComboBox.setGeometry(QtCore.QRect(110, 120, 161, 27))
        self.cityComboBox.setObjectName("cityComboBox")
        self.eventComboBox = QtWidgets.QComboBox(self.frame)
        self.eventComboBox.setGeometry(QtCore.QRect(110, 160, 161, 27))
        self.eventComboBox.setObjectName("eventComboBox")
        self.stateComboBox = QtWidgets.QComboBox(self.frame)
        self.stateComboBox.setGeometry(QtCore.QRect(110, 80, 161, 27))
        self.stateComboBox.setObjectName("stateComboBox")
        self.cityLabel = QtWidgets.QLabel(self.frame)
        self.cityLabel.setGeometry(QtCore.QRect(20, 120, 111, 31))
        self.cityLabel.setObjectName("cityLabel")
        self.eventLabel = QtWidgets.QLabel(self.frame)
        self.eventLabel.setGeometry(QtCore.QRect(20, 160, 161, 31))
        self.eventLabel.setObjectName("eventLabel")
        self.stateLabel = QtWidgets.QLabel(self.frame)
        self.stateLabel.setGeometry(QtCore.QRect(20, 80, 111, 31))
        self.stateLabel.setObjectName("stateLabel")
        self.ORLabel = QtWidgets.QLabel(self.frame)
        self.ORLabel.setGeometry(QtCore.QRect(90, 40, 111, 31))
        self.ORLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ORLabel.setObjectName("ORLabel")
        self.searchByID = QtWidgets.QLineEdit(self.frame)
        self.searchByID.setGeometry(QtCore.QRect(20, 10, 251, 27))
        self.searchByID.setObjectName("searchByID")
        self.title = QtWidgets.QLabel(selectEvent)
        self.title.setGeometry(QtCore.QRect(10, 0, 291, 51))
        self.title.setObjectName("title")
        self.selectButton = QtWidgets.QPushButton(selectEvent)
        self.selectButton.setGeometry(QtCore.QRect(120, 280, 80, 28))
        self.selectButton.setObjectName("selectButton")

        self.retranslateUi(selectEvent)
        QtCore.QMetaObject.connectSlotsByName(selectEvent)

    def retranslateUi(self, selectEvent):
        _translate = QtCore.QCoreApplication.translate
        selectEvent.setWindowTitle(_translate("selectEvent", " "))
        self.cityLabel.setText(_translate("selectEvent", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">City : </span></p></body></html>"))
        self.eventLabel.setText(_translate("selectEvent", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Event :</span></p></body></html>"))
        self.stateLabel.setText(_translate("selectEvent", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">State : </span></p></body></html>"))
        self.ORLabel.setText(_translate("selectEvent", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">OR</span></p></body></html>"))
        self.searchByID.setPlaceholderText(_translate("selectEvent", "Search by Event ID"))
        self.title.setText(_translate("selectEvent", "<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; font-weight:600; text-decoration: underline;\">Select Event</span></p></body></html>"))
        self.selectButton.setText(_translate("selectEvent", "SELECT"))

