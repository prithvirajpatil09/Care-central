# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ambulanceBill.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(508, 556)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(10, 10, 491, 501))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pickUpPlaceLabel = QtWidgets.QLabel(self.frame)
        self.pickUpPlaceLabel.setGeometry(QtCore.QRect(20, 110, 141, 41))
        self.pickUpPlaceLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.pickUpPlaceLabel.setObjectName("pickUpPlaceLabel")
        self.destinationLabel = QtWidgets.QLabel(self.frame)
        self.destinationLabel.setGeometry(QtCore.QRect(20, 160, 121, 41))
        self.destinationLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.destinationLabel.setObjectName("destinationLabel")
        self.patientIDLabel = QtWidgets.QLabel(self.frame)
        self.patientIDLabel.setGeometry(QtCore.QRect(20, 60, 151, 41))
        self.patientIDLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.patientIDLabel.setObjectName("patientIDLabel")
        self.patientID = QtWidgets.QLabel(self.frame)
        self.patientID.setGeometry(QtCore.QRect(170, 70, 281, 20))
        self.patientID.setObjectName("patientID")
        self.destination = QtWidgets.QLabel(self.frame)
        self.destination.setGeometry(QtCore.QRect(170, 170, 281, 20))
        self.destination.setObjectName("destination")
        self.pickUpPlace = QtWidgets.QLabel(self.frame)
        self.pickUpPlace.setGeometry(QtCore.QRect(170, 120, 281, 20))
        self.pickUpPlace.setObjectName("pickUpPlace")
        self.ambulanceLabel = QtWidgets.QLabel(self.frame)
        self.ambulanceLabel.setGeometry(QtCore.QRect(20, 210, 121, 41))
        self.ambulanceLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.ambulanceLabel.setObjectName("ambulanceLabel")
        self.ambulanceID = QtWidgets.QLabel(self.frame)
        self.ambulanceID.setGeometry(QtCore.QRect(170, 220, 281, 20))
        self.ambulanceID.setObjectName("ambulanceID")
        self.ambulanceLabel_2 = QtWidgets.QLabel(self.frame)
        self.ambulanceLabel_2.setGeometry(QtCore.QRect(20, 360, 121, 41))
        self.ambulanceLabel_2.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.ambulanceLabel_2.setObjectName("ambulanceLabel_2")
        self.ambulanceLabel_3 = QtWidgets.QLabel(self.frame)
        self.ambulanceLabel_3.setGeometry(QtCore.QRect(20, 460, 121, 41))
        self.ambulanceLabel_3.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.ambulanceLabel_3.setObjectName("ambulanceLabel_3")
        self.ambulanceLabel_4 = QtWidgets.QLabel(self.frame)
        self.ambulanceLabel_4.setGeometry(QtCore.QRect(20, 410, 121, 41))
        self.ambulanceLabel_4.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.ambulanceLabel_4.setObjectName("ambulanceLabel_4")
        self.ambulanceLabel_5 = QtWidgets.QLabel(self.frame)
        self.ambulanceLabel_5.setGeometry(QtCore.QRect(20, 260, 121, 41))
        self.ambulanceLabel_5.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.ambulanceLabel_5.setObjectName("ambulanceLabel_5")
        self.requestID = QtWidgets.QLabel(self.frame)
        self.requestID.setGeometry(QtCore.QRect(170, 270, 281, 20))
        self.requestID.setObjectName("requestID")
        self.esID = QtWidgets.QLabel(self.frame)
        self.esID.setGeometry(QtCore.QRect(170, 320, 281, 20))
        self.esID.setObjectName("esID")
        self.startTime = QtWidgets.QLabel(self.frame)
        self.startTime.setGeometry(QtCore.QRect(170, 370, 281, 20))
        self.startTime.setObjectName("startTime")
        self.distance = QtWidgets.QLabel(self.frame)
        self.distance.setGeometry(QtCore.QRect(170, 420, 281, 20))
        self.distance.setObjectName("distance")
        self.endTime = QtWidgets.QLabel(self.frame)
        self.endTime.setGeometry(QtCore.QRect(170, 470, 281, 20))
        self.endTime.setObjectName("endTime")
        self.patientIDLabel_2 = QtWidgets.QLabel(self.frame)
        self.patientIDLabel_2.setGeometry(QtCore.QRect(20, 10, 151, 41))
        self.patientIDLabel_2.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.patientIDLabel_2.setObjectName("patientIDLabel_2")
        self.billID = QtWidgets.QLabel(self.frame)
        self.billID.setGeometry(QtCore.QRect(170, 20, 301, 20))
        self.billID.setObjectName("billID")
        self.closeButton = QtWidgets.QPushButton(Form)
        self.closeButton.setGeometry(QtCore.QRect(380, 520, 111, 25))
        self.closeButton.setObjectName("closeButton")
        self.ambulanceLabel_6 = QtWidgets.QLabel(Form)
        self.ambulanceLabel_6.setGeometry(QtCore.QRect(30, 320, 121, 41))
        self.ambulanceLabel_6.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.ambulanceLabel_6.setObjectName("ambulanceLabel_6")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Ambulance Bill"))
        self.pickUpPlaceLabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">Pick Up Place : </span></p></body></html>"))
        self.destinationLabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">Destination : </span></p></body></html>"))
        self.patientIDLabel.setText(_translate("Form", "<html><head/><body><p>Patient ID :</p></body></html>"))
        self.patientID.setText(_translate("Form", "TextLabel"))
        self.destination.setText(_translate("Form", "TextLabel"))
        self.pickUpPlace.setText(_translate("Form", "TextLabel"))
        self.ambulanceLabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">Ambulance ID : </span></p></body></html>"))
        self.ambulanceID.setText(_translate("Form", "TextLabel"))
        self.ambulanceLabel_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">Start Time :</span></p></body></html>"))
        self.ambulanceLabel_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">End Time :</span></p></body></html>"))
        self.ambulanceLabel_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">Distance :</span></p></body></html>"))
        self.ambulanceLabel_5.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">Request ID : </span></p></body></html>"))
        self.requestID.setText(_translate("Form", "TextLabel"))
        self.esID.setText(_translate("Form", "TextLabel"))
        self.startTime.setText(_translate("Form", "TextLabel"))
        self.distance.setText(_translate("Form", "TextLabel"))
        self.endTime.setText(_translate("Form", "TextLabel"))
        self.patientIDLabel_2.setText(_translate("Form", "<html><head/><body><p>Bill ID :</p></body></html>"))
        self.billID.setText(_translate("Form", "TextLabel"))
        self.closeButton.setText(_translate("Form", "Close"))
        self.ambulanceLabel_6.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">ES ID :</span></p></body></html>"))

