from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 480)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(10, 10, 621, 421))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.recordLabel = QtWidgets.QLabel(self.frame)
        self.recordLabel.setGeometry(QtCore.QRect(250, 0, 131, 41))
        self.recordLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.recordLabel.setObjectName("recordLabel")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(10, 41, 601, 371))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.okbutton = QtWidgets.QPushButton(Form)
        self.okbutton.setGeometry(QtCore.QRect(530, 440, 89, 25))
        self.okbutton.setObjectName("okbutton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.recordLabel.setText(_translate("Form", "Records "))
        self.okbutton.setText(_translate("Form", "close"))

