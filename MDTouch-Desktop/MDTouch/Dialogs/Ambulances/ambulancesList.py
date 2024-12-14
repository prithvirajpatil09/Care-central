from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
class ambulanceList(object):
    def setup(self, Form,esid):
        self.esid = esid
        Form.setObjectName("Form")
        Form.resize(640, 480)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(10, 10, 621, 421))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.ambulanceListLabel = QtWidgets.QLabel(self.frame)
        self.ambulanceListLabel.setGeometry(QtCore.QRect(210, 0, 191, 41))
        self.ambulanceListLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.ambulanceListLabel.setObjectName("ambulanceListLabel")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(10, 41, 601, 371))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(0)
        self.okButton = QtWidgets.QPushButton(Form)
        self.okButton.setGeometry(QtCore.QRect(530, 440, 89, 25))
        self.okButton.setObjectName("okButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Ambulances List"))
        self.ambulanceListLabel.setText(_translate("Form", "Ambulances List"))
        self.okButton.setText(_translate("Form", "close"))

