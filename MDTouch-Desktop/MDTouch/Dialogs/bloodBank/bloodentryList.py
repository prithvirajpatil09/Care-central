
from PyQt5 import QtCore, QtGui, QtWidgets

class bloodentryList(object):
    def setup(self, bloodentryList,data):
        self.userdata = data
        bloodentryList.setObjectName("bloodentryList")
        bloodentryList.resize(640, 480)
        self.frame = QtWidgets.QFrame(bloodentryList)
        self.frame.setGeometry(QtCore.QRect(10, 10, 621, 421))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.billingLabel = QtWidgets.QLabel(self.frame)
        self.billingLabel.setGeometry(QtCore.QRect(220, 0, 221, 41))
        self.billingLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.billingLabel.setObjectName("billingLabel")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(10, 41, 601, 371))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.closebutton = QtWidgets.QPushButton(bloodentryList)
        self.closebutton.setGeometry(QtCore.QRect(530, 440, 89, 25))
        self.closebutton.setObjectName("closebutton")

        self.retranslateUi(bloodentryList)
        QtCore.QMetaObject.connectSlotsByName(bloodentryList)

    def retranslateUi(self, bloodentryList):
        _translate = QtCore.QCoreApplication.translate
        bloodentryList.setWindowTitle(_translate("bloodentryList", "Records"))
        self.billingLabel.setText(_translate("bloodentryList", "Blood Entry Records"))
        self.closebutton.setText(_translate("bloodentryList", "close"))

