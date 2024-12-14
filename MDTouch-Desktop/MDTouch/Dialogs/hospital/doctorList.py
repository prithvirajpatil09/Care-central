from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Dialogs.messageBox import *
from Dialogs.superadmin.Doctors.doctorProfile import *

class Widget1(QWidget):
    def __init__(self,parent = None):
        QWidget.__init__(self,parent=None)
        layout = QFrame(self)
        layout.setGeometry(0,0,600,50)
        self.noticeIdLabel = QLabel(layout)
        self.noticeIdLabel.setGeometry(QRect(10,10,150,30))
        self.noticeIdLabel.setText("Id : 123")
        self.noticeNameLabel = QLabel(layout)
        self.noticeNameLabel.setGeometry(QRect(180,10,500,30))


class doctorList(object):
    def setup(self, doctorList,hospitaldata):
        self.doctorList = []
        self.hospitaldata = hospitaldata
        doctorList.setObjectName("doctorList")
        doctorList.resize(640, 539)
        self.frame = QtWidgets.QFrame(doctorList)
        self.frame.setGeometry(QtCore.QRect(10, 50, 621, 421))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(10, 41, 601, 371))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.okbutton = QtWidgets.QPushButton(doctorList)
        self.okbutton.setGeometry(QtCore.QRect(260, 480, 89, 25))
        self.okbutton.setObjectName("okbutton")
        self.titleLabel = QtWidgets.QLabel(doctorList)
        self.titleLabel.setGeometry(QtCore.QRect(160, 0, 301, 41))
        self.titleLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.titleLabel.setObjectName("titleLabel")

        self.retranslateUi(doctorList)
        QtCore.QMetaObject.connectSlotsByName(doctorList)

    def retranslateUi(self, doctorList):
        _translate = QtCore.QCoreApplication.translate
        doctorList.setWindowTitle(_translate("doctorList", "Doctors"))
        self.okbutton.setText(_translate("doctorList", "close"))
        self.titleLabel.setText(_translate("doctorList", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; text-decoration: underline;\">Doctor List</span></p></body></html>"))
        self.events(doctorList)

    def events(self,parent):
        self.okbutton.clicked.connect(lambda : parent.close())
        import requests
        URL = "http://127.0.0.1:8000/MDTouch/api/doctor/"
        params = {
            "workplace" : int(self.hospitaldata["id"])
        }
        r = requests.get(url=URL,params=params)
        l = r.json()
        self.doctorList = l
        if len(l) == 0:
            self.window = messageBox()
            self.window.infoBox("No Admin Found")
            parent.close()
            return
        self.tableWidget.verticalHeader().hide()
        self.tableWidget.horizontalHeader().hide()
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableWidget.setAutoScrollMargin(100)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setRowHeight(0,120)
        self.tableWidget.setStyleSheet("background : rgb(255,255,255);")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setObjectName("tablewidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(len(l))
        ctr = 0
        for i in l:
            if ctr == 10:
                break

            self.item  = Widget1()
            self.item.noticeIdLabel.setText("ID : " + str(i["id"]))
            self.item.noticeNameLabel.setText(str(i["firstName"] + " " + i["lastName"]))
            self.tableWidget.setCellWidget(ctr,0,self.item)
            self.tableWidget.setRowHeight(ctr,50)
            ctr += 1
        self.tableWidget.cellClicked.connect(self.cellClick)

    def cellClick(self,row,col):
        self.window = QDialog()
        self.dialog = doctorProfile()
        self.dialog.setup(self.window,self.doctorList[row],self.hospitaldata)
        self.window.setModal(True)
        self.window.show()

