

from PyQt5 import QtCore, QtGui, QtWidgets

class bloodFraud(object):
    def setup(self, bloodFraud):
        bloodFraud.setObjectName("bloodFraud")
        bloodFraud.resize(648, 512)
        self.frame = QtWidgets.QFrame(bloodFraud)
        self.frame.setGeometry(QtCore.QRect(10, 50, 621, 421))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(10, 41, 601, 371))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(8)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 5, item)
        self.startingDate = QtWidgets.QDateEdit(self.frame)
        self.startingDate.setGeometry(QtCore.QRect(150, 10, 111, 26))
        self.startingDate.setObjectName("startingDate")
        self.titleLabel_2 = QtWidgets.QLabel(self.frame)
        self.titleLabel_2.setGeometry(QtCore.QRect(10, 10, 131, 31))
        self.titleLabel_2.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.titleLabel_2.setObjectName("titleLabel_2")
        self.titleLabel_3 = QtWidgets.QLabel(self.frame)
        self.titleLabel_3.setGeometry(QtCore.QRect(260, 10, 131, 31))
        self.titleLabel_3.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.titleLabel_3.setObjectName("titleLabel_3")
        self.EndingDate = QtWidgets.QDateEdit(self.frame)
        self.EndingDate.setGeometry(QtCore.QRect(390, 10, 111, 26))
        self.EndingDate.setObjectName("EndingDate")
        self.findButton = QtWidgets.QPushButton(self.frame)
        self.findButton.setGeometry(QtCore.QRect(520, 10, 89, 25))
        self.findButton.setObjectName("findButton")
        self.okbutton = QtWidgets.QPushButton(bloodFraud)
        self.okbutton.setGeometry(QtCore.QRect(260, 480, 89, 25))
        self.okbutton.setObjectName("okbutton")
        self.titleLabel = QtWidgets.QLabel(bloodFraud)
        self.titleLabel.setGeometry(QtCore.QRect(110, 0, 411, 41))
        self.titleLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.titleLabel.setObjectName("titleLabel")

        self.retranslateUi(bloodFraud)
        QtCore.QMetaObject.connectSlotsByName(bloodFraud)

    def retranslateUi(self, bloodFraud):
        _translate = QtCore.QCoreApplication.translate
        bloodFraud.setWindowTitle(_translate("bloodFraud", "bloodFraud"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("bloodFraud", "Blood Bank Id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("bloodFraud", "Total Records"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("bloodFraud", "Total Wasted"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("bloodFraud", "Total Recieved"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("bloodFraud", "Total Send"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("bloodFraud", "Fraud T/F"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("bloodFraud", "5"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("bloodFraud", "16"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("bloodFraud", "46"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("bloodFraud", "124"))
        item = self.tableWidget.item(0, 4)
        item.setText(_translate("bloodFraud", "16"))
        item = self.tableWidget.item(0, 5)
        item.setText(_translate("bloodFraud", "T"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("bloodFraud", "1"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("bloodFraud", "17"))
        item = self.tableWidget.item(1, 2)
        item.setText(_translate("bloodFraud", "33"))
        item = self.tableWidget.item(1, 3)
        item.setText(_translate("bloodFraud", "123"))
        item = self.tableWidget.item(1, 4)
        item.setText(_translate("bloodFraud", "18"))
        item = self.tableWidget.item(1, 5)
        item.setText(_translate("bloodFraud", "T"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("bloodFraud", "2"))
        item = self.tableWidget.item(2, 1)
        item.setText(_translate("bloodFraud", "24"))
        item = self.tableWidget.item(2, 2)
        item.setText(_translate("bloodFraud", "37"))
        item = self.tableWidget.item(2, 3)
        item.setText(_translate("bloodFraud", "67"))
        item = self.tableWidget.item(2, 4)
        item.setText(_translate("bloodFraud", "25"))
        item = self.tableWidget.item(2, 5)
        item.setText(_translate("bloodFraud", "F"))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("bloodFraud", "3"))
        item = self.tableWidget.item(3, 1)
        item.setText(_translate("bloodFraud", "16"))
        item = self.tableWidget.item(3, 2)
        item.setText(_translate("bloodFraud", "1"))
        item = self.tableWidget.item(3, 3)
        item.setText(_translate("bloodFraud", "12"))
        item = self.tableWidget.item(3, 4)
        item.setText(_translate("bloodFraud", "15"))
        item = self.tableWidget.item(3, 5)
        item.setText(_translate("bloodFraud", "F"))
        item = self.tableWidget.item(4, 0)
        item.setText(_translate("bloodFraud", "6"))
        item = self.tableWidget.item(4, 1)
        item.setText(_translate("bloodFraud", "7"))
        item = self.tableWidget.item(4, 2)
        item.setText(_translate("bloodFraud", "0"))
        item = self.tableWidget.item(4, 3)
        item.setText(_translate("bloodFraud", "1"))
        item = self.tableWidget.item(4, 4)
        item.setText(_translate("bloodFraud", "2"))
        item = self.tableWidget.item(4, 5)
        item.setText(_translate("bloodFraud", "F"))
        item = self.tableWidget.item(5, 0)
        item.setText(_translate("bloodFraud", "4"))
        item = self.tableWidget.item(5, 1)
        item.setText(_translate("bloodFraud", "20"))
        item = self.tableWidget.item(5, 2)
        item.setText(_translate("bloodFraud", "0"))
        item = self.tableWidget.item(5, 3)
        item.setText(_translate("bloodFraud", "1"))
        item = self.tableWidget.item(5, 4)
        item.setText(_translate("bloodFraud", "3"))
        item = self.tableWidget.item(5, 5)
        item.setText(_translate("bloodFraud", "F"))
        item = self.tableWidget.item(6, 0)
        item.setText(_translate("bloodFraud", "7"))
        item = self.tableWidget.item(6, 1)
        item.setText(_translate("bloodFraud", "11"))
        item = self.tableWidget.item(6, 2)
        item.setText(_translate("bloodFraud", "1"))
        item = self.tableWidget.item(6, 3)
        item.setText(_translate("bloodFraud", "0"))
        item = self.tableWidget.item(6, 4)
        item.setText(_translate("bloodFraud", "1"))
        item = self.tableWidget.item(6, 5)
        item.setText(_translate("bloodFraud", "F"))
        item = self.tableWidget.item(7, 0)
        item.setText(_translate("bloodFraud", "8"))
        item = self.tableWidget.item(7, 1)
        item.setText(_translate("bloodFraud", "2"))
        item = self.tableWidget.item(7, 2)
        item.setText(_translate("bloodFraud", "0"))
        item = self.tableWidget.item(7, 3)
        item.setText(_translate("bloodFraud", "0"))
        item = self.tableWidget.item(7, 4)
        item.setText(_translate("bloodFraud", "2"))
        item = self.tableWidget.item(7, 5)
        item.setText(_translate("bloodFraud", "F"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.titleLabel_2.setText(_translate("bloodFraud", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Starting Date :</span></p></body></html>"))
        self.titleLabel_3.setText(_translate("bloodFraud", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Ending Date :</span></p></body></html>"))
        self.findButton.setText(_translate("bloodFraud", "Find"))
        self.okbutton.setText(_translate("bloodFraud", "close"))
        self.titleLabel.setText(_translate("bloodFraud", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; text-decoration: underline;\">Blood Fraud Detection</span></p></body></html>"))

