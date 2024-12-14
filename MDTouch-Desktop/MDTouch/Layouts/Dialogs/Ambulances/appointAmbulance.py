# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'appointAmbulance.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(515, 315)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(10, 10, 491, 241))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pickUpPlaceLabel = QtWidgets.QLabel(self.frame)
        self.pickUpPlaceLabel.setGeometry(QtCore.QRect(20, 70, 141, 41))
        self.pickUpPlaceLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.pickUpPlaceLabel.setObjectName("pickUpPlaceLabel")
        self.destinationLabel = QtWidgets.QLabel(self.frame)
        self.destinationLabel.setGeometry(QtCore.QRect(20, 120, 121, 41))
        self.destinationLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.destinationLabel.setObjectName("destinationLabel")
        self.patientIDLabel = QtWidgets.QLabel(self.frame)
        self.patientIDLabel.setGeometry(QtCore.QRect(20, 20, 151, 41))
        self.patientIDLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.patientIDLabel.setObjectName("patientIDLabel")
        self.patientID = QtWidgets.QLabel(self.frame)
        self.patientID.setGeometry(QtCore.QRect(170, 30, 281, 20))
        self.patientID.setObjectName("patientID")
        self.destination = QtWidgets.QLabel(self.frame)
        self.destination.setGeometry(QtCore.QRect(170, 130, 281, 20))
        self.destination.setObjectName("destination")
        self.pickUpPlace = QtWidgets.QLabel(self.frame)
        self.pickUpPlace.setGeometry(QtCore.QRect(170, 80, 281, 20))
        self.pickUpPlace.setObjectName("pickUpPlace")
        self.ambulanceLabel = QtWidgets.QLabel(self.frame)
        self.ambulanceLabel.setGeometry(QtCore.QRect(20, 170, 121, 41))
        self.ambulanceLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.ambulanceLabel.setObjectName("ambulanceLabel")
        self.ambulanceCombobox = QtWidgets.QComboBox(self.frame)
        self.ambulanceCombobox.setGeometry(QtCore.QRect(170, 180, 251, 25))
        self.ambulanceCombobox.setObjectName("ambulanceCombobox")
        self.sendButton = QtWidgets.QPushButton(Form)
        self.sendButton.setGeometry(QtCore.QRect(160, 270, 161, 25))
        self.sendButton.setObjectName("sendButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Appoint Hospital"))
        self.pickUpPlaceLabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">Pick Up Place : </span></p></body></html>"))
        self.destinationLabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">Destination : </span></p></body></html>"))
        self.patientIDLabel.setText(_translate("Form", "<html><head/><body><p>Patient ID :</p></body></html>"))
        self.patientID.setText(_translate("Form", "TextLabel"))
        self.destination.setText(_translate("Form", "TextLabel"))
        self.pickUpPlace.setText(_translate("Form", "TextLabel"))
        self.ambulanceLabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">Ambulance : </span></p></body></html>"))
        self.sendButton.setText(_translate("Form", "Send Ambulance"))

