from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Dialogs.Notice.noticeProfile import *

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


class noticeList(object):
    def __init__(self):
        self.notice_list = []
    def setup(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 480)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(10, 10, 621, 421))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.noticeListLabel = QtWidgets.QLabel(self.frame)
        self.noticeListLabel.setGeometry(QtCore.QRect(250, 0, 131, 41))
        self.noticeListLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.noticeListLabel.setObjectName("noticeListLabel")
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
        Form.setWindowTitle(_translate("Form", "Notices"))
        self.noticeListLabel.setText(_translate("Form", "Notices"))
        self.okbutton.setText(_translate("Form", "close"))
        self.events(Form)

    def events(self,parent):
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
        self.okbutton.clicked.connect(lambda : parent.close())
        import requests
        URL = "http://127.0.0.1:8000/MDTouch/api/notice/?ordering=-date"
        r = requests.get(url=URL)
        self.notice_list = r.json()
        ctr = 0
        if len(self.notice_list) > 10:
            self.tableWidget.setRowCount(10)
        else:
            self.tableWidget.setRowCount(len(self.notice_list))
        for i in self.notice_list:
            if ctr == 10:
                break

            self.item  = Widget1()
            self.item.noticeIdLabel.setText("ID : " + str(i["id"]))
            self.item.noticeNameLabel.setText(str(i["title"]))
            self.tableWidget.setCellWidget(ctr,0,self.item)
            self.tableWidget.setRowHeight(ctr,50)
            ctr += 1
        self.tableWidget.cellClicked.connect(self.cellClick)

    def cellClick(self,row,col):
        self.window = QDialog()
        self.dialog = noticeProfile()
        self.dialog.setup(self.window,self.notice_list[row])
        self.window.setModal(True)
        self.window.show()
