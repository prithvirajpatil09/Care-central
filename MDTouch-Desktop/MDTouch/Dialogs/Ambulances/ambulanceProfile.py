from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(575, 450)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(10, 10, 551, 381))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.vechicleNumberLabel = QtWidgets.QLabel(self.frame)
        self.vechicleNumberLabel.setGeometry(QtCore.QRect(20, 120, 151, 41))
        self.vechicleNumberLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.vechicleNumberLabel.setObjectName("vechicleNumberLabel")
        self.driverNameLabel = QtWidgets.QLabel(self.frame)
        self.driverNameLabel.setGeometry(QtCore.QRect(20, 170, 151, 41))
        self.driverNameLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.driverNameLabel.setObjectName("driverNameLabel")
        self.capacityLabel = QtWidgets.QLabel(self.frame)
        self.capacityLabel.setGeometry(QtCore.QRect(20, 270, 91, 41))
        self.capacityLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.capacityLabel.setObjectName("capacityLabel")
        self.mobileNumberLabel = QtWidgets.QLabel(self.frame)
        self.mobileNumberLabel.setGeometry(QtCore.QRect(20, 220, 151, 41))
        self.mobileNumberLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.mobileNumberLabel.setObjectName("mobileNumberLabel")
        self.typeLabel = QtWidgets.QLabel(self.frame)
        self.typeLabel.setGeometry(QtCore.QRect(20, 320, 71, 41))
        self.typeLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.typeLabel.setObjectName("typeLabel")
        self.ambulanceIDLabel = QtWidgets.QLabel(self.frame)
        self.ambulanceIDLabel.setGeometry(QtCore.QRect(20, 20, 151, 41))
        self.ambulanceIDLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.ambulanceIDLabel.setObjectName("ambulanceIDLabel")
        self.esIDLabel = QtWidgets.QLabel(self.frame)
        self.esIDLabel.setGeometry(QtCore.QRect(20, 70, 151, 41))
        self.esIDLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.esIDLabel.setObjectName("esIDLabel")
        self.ambulanceID = QtWidgets.QLabel(self.frame)
        self.ambulanceID.setGeometry(QtCore.QRect(170, 30, 281, 20))
        self.ambulanceID.setObjectName("ambulanceID")
        self.esID = QtWidgets.QLabel(self.frame)
        self.esID.setGeometry(QtCore.QRect(170, 80, 281, 20))
        self.esID.setObjectName("esID")
        self.vechicleLabel = QtWidgets.QLabel(self.frame)
        self.vechicleLabel.setGeometry(QtCore.QRect(170, 130, 281, 20))
        self.vechicleLabel.setObjectName("vechicleLabel")
        self.capacity = QtWidgets.QLabel(self.frame)
        self.capacity.setGeometry(QtCore.QRect(170, 280, 281, 20))
        self.capacity.setObjectName("capacity")
        self.mobileNumber = QtWidgets.QLabel(self.frame)
        self.mobileNumber.setGeometry(QtCore.QRect(170, 230, 281, 20))
        self.mobileNumber.setObjectName("mobileNumber")
        self.driverName = QtWidgets.QLabel(self.frame)
        self.driverName.setGeometry(QtCore.QRect(170, 180, 281, 20))
        self.driverName.setObjectName("driverName")
        self.type = QtWidgets.QLabel(self.frame)
        self.type.setGeometry(QtCore.QRect(170, 330, 281, 20))
        self.type.setObjectName("type")
        self.closeButton = QtWidgets.QPushButton(Form)
        self.closeButton.setGeometry(QtCore.QRect(470, 410, 89, 25))
        self.closeButton.setObjectName("closeButton")
        self.seeRecordsButton = QtWidgets.QPushButton(Form)
        self.seeRecordsButton.setGeometry(QtCore.QRect(320, 410, 131, 25))
        self.seeRecordsButton.setObjectName("seeRecordsButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Ambulance Profile"))
        self.vechicleNumberLabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">Vechicle Number :</span></p></body></html>"))
        self.driverNameLabel.setText(_translate("Form", "<html><head/><body><p>Driver Name : </p></body></html>"))
        self.capacityLabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">Capacity :</span></p></body></html>"))
        self.mobileNumberLabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">Mobile Number :</span></p></body></html>"))
        self.typeLabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">Type : </span></p></body></html>"))
        self.ambulanceIDLabel.setText(_translate("Form", "<html><head/><body><p>Ambulance ID :</p></body></html>"))
        self.esIDLabel.setText(_translate("Form", "<html><head/><body><p>ES ID :</p></body></html>"))
        self.ambulanceID.setText(_translate("Form", "TextLabel"))
        self.esID.setText(_translate("Form", "TextLabel"))
        self.vechicleLabel.setText(_translate("Form", "TextLabel"))
        self.capacity.setText(_translate("Form", "TextLabel"))
        self.mobileNumber.setText(_translate("Form", "TextLabel"))
        self.driverName.setText(_translate("Form", "TextLabel"))
        self.type.setText(_translate("Form", "TextLabel"))
        self.closeButton.setText(_translate("Form", "Close"))
        self.seeRecordsButton.setText(_translate("Form", "See Records"))

