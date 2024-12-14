

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Dialogs.bloodBank.bloodwasteProfile import *
class Widget1(QWidget):
    def __init__(self,parent = None):
        QWidget.__init__(self,parent=None)
        layout = QFrame(self)
        layout.setGeometry(0,0,600,50)
        self.billIdLabel = QLabel(layout)
        self.billIdLabel.setGeometry(QRect(10,10,150,30))
        self.billIdLabel.setText("Id : 123")
        self.billNameLabel = QLabel(layout)
        self.billNameLabel.setGeometry(QRect(180,10,500,30))

class wasteRecordList(object):
    def __init__(self):
        self.wasterecord_list = []
    def setup(self, wasteRecordList,bloodbankdata):
        self.bloodbankdata = bloodbankdata
        wasteRecordList.setObjectName("wasteRecordList")
        wasteRecordList.resize(640, 480)
        self.frame = QtWidgets.QFrame(wasteRecordList)
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
        self.closebutton = QtWidgets.QPushButton(wasteRecordList)
        self.closebutton.setGeometry(QtCore.QRect(530, 440, 89, 25))
        self.closebutton.setObjectName("closebutton")

        self.retranslateUi(wasteRecordList)
        QtCore.QMetaObject.connectSlotsByName(wasteRecordList)

    def retranslateUi(self, wasteRecordList):
        _translate = QtCore.QCoreApplication.translate
        wasteRecordList.setWindowTitle(_translate("wasteRecordList", "Records"))
        self.wasteRecordLabel.setText(_translate("wasteRecordList", "Waste Records"))
        self.closebutton.setText(_translate("wasteRecordList", "close"))
        self.events(wasteRecordList)

    def events(self,parent):
        self.closebutton.clicked.connect(lambda : parent.close())
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
        import requests
        URL = "http://127.0.0.1:8000/MDTouch/api/bloodwaste/?ordering=-date"
        param = {
            "bbcid": int(self.bloodbankdata["id"])
        }
        r = requests.get(url=URL,params=param)
        self.wasterecord_list = r.json()
        ctr = 0
        if len(self.wasterecord_list) > 10:
            self.tableWidget.setRowCount(10)
        else:
            self.tableWidget.setRowCount(len(self.wasterecord_list))
        for i in self.wasterecord_list:


            self.item  = Widget1()
            self.item.billIdLabel.setText("ID : " + str(i["id"]))
            self.item.billNameLabel.setText("quantity : " + str(i["quantity"]) + str(i["bloodgrp"]))
            self.tableWidget.setCellWidget(ctr,0,self.item)
            self.tableWidget.setRowHeight(ctr,50)
            ctr += 1
        self.tableWidget.cellClicked.connect(self.cellClick)

    def cellClick(self,row,col):
        self.window = QDialog()
        self.dialog = bloodwasteReciept()
        self.dialog.setup(self.window,self.wasterecord_list[row])
        self.window.setModal(True)
        self.window.show()




