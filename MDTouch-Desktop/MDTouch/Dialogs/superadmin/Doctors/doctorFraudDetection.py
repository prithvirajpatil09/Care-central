from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from PyQt5 import QtCore, QtGui, QtWidgets
from Dialogs.Graphs.doctorAppointmentGraph import *

class DoctorFraud(object):
    def setup(self, DoctorFraud):
        DoctorFraud.setObjectName("DoctorFraud")
        DoctorFraud.resize(648, 512)
        self.frame = QtWidgets.QFrame(DoctorFraud)
        self.frame.setGeometry(QtCore.QRect(10, 50, 621, 421))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(10, 41, 311, 371))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
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
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 2, item)
        self.startingDate = QtWidgets.QDateEdit(self.frame)
        self.startingDate.setGeometry(QtCore.QRect(140, 10, 111, 26))
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
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(360, 170, 241, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(358, 220, 241, 25))
        self.pushButton.setObjectName("pushButton")
        self.okbutton = QtWidgets.QPushButton(DoctorFraud)
        self.okbutton.setGeometry(QtCore.QRect(260, 480, 89, 25))
        self.okbutton.setObjectName("okbutton")
        self.titleLabel = QtWidgets.QLabel(DoctorFraud)
        self.titleLabel.setGeometry(QtCore.QRect(50, 0, 561, 41))
        self.titleLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.titleLabel.setObjectName("titleLabel")

        self.retranslateUi(DoctorFraud)
        QtCore.QMetaObject.connectSlotsByName(DoctorFraud)

    def retranslateUi(self, DoctorFraud):
        _translate = QtCore.QCoreApplication.translate
        DoctorFraud.setWindowTitle(_translate("DoctorFraud", "bloodFraud"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("DoctorFraud", "Doctor ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("DoctorFraud", "Hospital ID"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("DoctorFraud", "Fraud T/F"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("DoctorFraud", "5"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("DoctorFraud", "1"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("DoctorFraud", "T"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("DoctorFraud", "1"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("DoctorFraud", "1"))
        item = self.tableWidget.item(1, 2)
        item.setText(_translate("DoctorFraud", "T"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("DoctorFraud", "2"))
        item = self.tableWidget.item(2, 1)
        item.setText(_translate("DoctorFraud", "2"))
        item = self.tableWidget.item(2, 2)
        item.setText(_translate("DoctorFraud", "F"))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("DoctorFraud", "3"))
        item = self.tableWidget.item(3, 1)
        item.setText(_translate("DoctorFraud", "1"))
        item = self.tableWidget.item(3, 2)
        item.setText(_translate("DoctorFraud", "F"))
        item = self.tableWidget.item(4, 0)
        item.setText(_translate("DoctorFraud", "6"))
        item = self.tableWidget.item(4, 1)
        item.setText(_translate("DoctorFraud", "2"))
        item = self.tableWidget.item(4, 2)
        item.setText(_translate("DoctorFraud", "F"))
        item = self.tableWidget.item(5, 0)
        item.setText(_translate("DoctorFraud", "4"))
        item = self.tableWidget.item(5, 1)
        item.setText(_translate("DoctorFraud", "3"))
        item = self.tableWidget.item(5, 2)
        item.setText(_translate("DoctorFraud", "F"))
        item = self.tableWidget.item(6, 0)
        item.setText(_translate("DoctorFraud", "7"))
        item = self.tableWidget.item(6, 1)
        item.setText(_translate("DoctorFraud", "3"))
        item = self.tableWidget.item(6, 2)
        item.setText(_translate("DoctorFraud", "F"))
        item = self.tableWidget.item(7, 0)
        item.setText(_translate("DoctorFraud", "8"))
        item = self.tableWidget.item(7, 1)
        item.setText(_translate("DoctorFraud", "2"))
        item = self.tableWidget.item(7, 2)
        item.setText(_translate("DoctorFraud", "F"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.titleLabel_2.setText(_translate("DoctorFraud", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Starting Date :</span></p></body></html>"))
        self.titleLabel_3.setText(_translate("DoctorFraud", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Ending Date :</span></p></body></html>"))
        self.findButton.setText(_translate("DoctorFraud", "Find"))
        self.lineEdit.setPlaceholderText(_translate("DoctorFraud", "Enter Doctor ID"))
        self.pushButton.setText(_translate("DoctorFraud", "See Appointment Stats"))
        self.okbutton.setText(_translate("DoctorFraud", "close"))
        self.titleLabel.setText(_translate("DoctorFraud", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; text-decoration: underline;\">Doctor Fraud Detection</span></p></body></html>"))
        self.okbutton.clicked.connect(lambda : DoctorFraud.close())
        self.pushButton.clicked.connect(lambda : self.clickOnDoctorGraph())

    def clickOnDoctorGraph(self):
        self.window = QDialog()
        self.dialog = doctorAppointmentGraph()
        self.dialog.setup(self.window)
        self.window.setModal(True)
        self.window.show()