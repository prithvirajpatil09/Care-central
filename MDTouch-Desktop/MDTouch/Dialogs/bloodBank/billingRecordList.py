from PyQt5 import QtCore, QtGui, QtWidgets

class billingList(object):
    def setup(self, billingList, userdata):
        self.userdata = userdata
        billingList.setObjectName("billingList")
        billingList.resize(640, 480)
        self.frame = QtWidgets.QFrame(billingList)
        self.frame.setGeometry(QtCore.QRect(10, 10, 621, 421))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.wasteRecordLabel = QtWidgets.QLabel(self.frame)
        self.wasteRecordLabel.setGeometry(QtCore.QRect(220, 0, 221, 41))
        self.wasteRecordLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.wasteRecordLabel.setObjectName("wasteRecordLabel")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(10, 41, 601, 371))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.closebutton = QtWidgets.QPushButton(billingList)
        self.closebutton.setGeometry(QtCore.QRect(530, 440, 89, 25))
        self.closebutton.setObjectName("closebutton")

        self.retranslateUi(billingList)
        QtCore.QMetaObject.connectSlotsByName(billingList)

    def retranslateUi(self, billingList):
        _translate = QtCore.QCoreApplication.translate
        billingList.setWindowTitle(_translate("billingList", "Records"))
        self.wasteRecordLabel.setText(_translate("billingList", "Blood Billing List"))
        self.closebutton.setText(_translate("billingList", "close"))

