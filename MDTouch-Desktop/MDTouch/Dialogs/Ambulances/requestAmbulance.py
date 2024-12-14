from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(575, 354)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(10, 10, 551, 291))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.patientContactLabel = QtWidgets.QLabel(self.frame)
        self.patientContactLabel.setGeometry(QtCore.QRect(20, 120, 201, 41))
        self.patientContactLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.patientContactLabel.setObjectName("patientContactLabel")
        self.pickUpPlaceLabel = QtWidgets.QLabel(self.frame)
        self.pickUpPlaceLabel.setGeometry(QtCore.QRect(20, 170, 151, 41))
        self.pickUpPlaceLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.pickUpPlaceLabel.setObjectName("pickUpPlaceLabel")
        self.destinationLabel = QtWidgets.QLabel(self.frame)
        self.destinationLabel.setGeometry(QtCore.QRect(20, 220, 151, 41))
        self.destinationLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.destinationLabel.setObjectName("destinationLabel")
        self.patientIDLabel = QtWidgets.QLabel(self.frame)
        self.patientIDLabel.setGeometry(QtCore.QRect(20, 20, 151, 41))
        self.patientIDLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.patientIDLabel.setObjectName("patientIDLabel")
        self.patientNameLabel = QtWidgets.QLabel(self.frame)
        self.patientNameLabel.setGeometry(QtCore.QRect(20, 70, 151, 41))
        self.patientNameLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.patientNameLabel.setObjectName("patientNameLabel")
        self.patientID = QtWidgets.QLabel(self.frame)
        self.patientID.setGeometry(QtCore.QRect(170, 30, 281, 20))
        self.patientID.setObjectName("patientID")
        self.patientName = QtWidgets.QLabel(self.frame)
        self.patientName.setGeometry(QtCore.QRect(170, 80, 281, 20))
        self.patientName.setObjectName("patientName")
        self.patientContactNumber = QtWidgets.QLabel(self.frame)
        self.patientContactNumber.setGeometry(QtCore.QRect(230, 130, 281, 20))
        self.patientContactNumber.setObjectName("patientContactNumber")
        self.destination = QtWidgets.QLabel(self.frame)
        self.destination.setGeometry(QtCore.QRect(170, 230, 281, 20))
        self.destination.setObjectName("destination")
        self.pickUpPlace = QtWidgets.QLabel(self.frame)
        self.pickUpPlace.setGeometry(QtCore.QRect(170, 180, 281, 20))
        self.pickUpPlace.setObjectName("pickUpPlace")
        self.rejectButton = QtWidgets.QPushButton(Form)
        self.rejectButton.setGeometry(QtCore.QRect(470, 320, 89, 25))
        self.rejectButton.setObjectName("rejectButton")
        self.appointButton = QtWidgets.QPushButton(Form)
        self.appointButton.setGeometry(QtCore.QRect(290, 320, 161, 25))
        self.appointButton.setObjectName("appointButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Ambulance Profile"))
        self.patientContactLabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">Patient Contact Number :</span></p></body></html>"))
        self.pickUpPlaceLabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">Pick Up Place : </span></p></body></html>"))
        self.destinationLabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">Destination : </span></p></body></html>"))
        self.patientIDLabel.setText(_translate("Form", "<html><head/><body><p>Patient ID :</p></body></html>"))
        self.patientNameLabel.setText(_translate("Form", "<html><head/><body><p>Patient Name :</p></body></html>"))
        self.patientID.setText(_translate("Form", "TextLabel"))
        self.patientName.setText(_translate("Form", "TextLabel"))
        self.patientContactNumber.setText(_translate("Form", "TextLabel"))
        self.destination.setText(_translate("Form", "TextLabel"))
        self.pickUpPlace.setText(_translate("Form", "TextLabel"))
        self.rejectButton.setText(_translate("Form", "Reject"))
        self.appointButton.setText(_translate("Form", "Appoint Ambulance"))

