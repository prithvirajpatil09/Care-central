from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Dialogs.doctor.prescriptionProfile import *

class Widget1(QWidget):
    def __init__(self,parent = None):
        QWidget.__init__(self,parent=None)
        layout = QFrame(self)
        layout.setGeometry(0,0,600,50)
        self.noticeIdLabel = QLabel(layout)
        self.noticeIdLabel.setGeometry(QRect(10,10,120,30))
        self.noticeIdLabel.setText("Id : 123")
        self.noticeNameLabel = QLabel(layout)
        self.noticeNameLabel.setGeometry(QRect(180,10,500,30))
        self.patientID = QLabel(layout)
        self.patientID.setGeometry(QRect(690,10,150,30))

class prescriptionList(object):
    def setup(self, prescriptionList,pList):
        self.pList = pList
        prescriptionList.setObjectName("prescriptionList")
        prescriptionList.resize(640, 480)
        self.frame = QtWidgets.QFrame(prescriptionList)
        self.frame.setGeometry(QtCore.QRect(10, 10, 621, 421))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.prescriptionListLabel = QtWidgets.QLabel(self.frame)
        self.prescriptionListLabel.setGeometry(QtCore.QRect(250, 0, 131, 41))
        self.prescriptionListLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.prescriptionListLabel.setObjectName("prescriptionListLabel")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(10, 41, 601, 371))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.okbutton = QtWidgets.QPushButton(prescriptionList)
        self.okbutton.setGeometry(QtCore.QRect(530, 440, 89, 25))
        self.okbutton.setObjectName("okbutton")

        self.retranslateUi(prescriptionList)
        QtCore.QMetaObject.connectSlotsByName(prescriptionList)

    def retranslateUi(self, prescriptionList):
        _translate = QtCore.QCoreApplication.translate
        prescriptionList.setWindowTitle(_translate("prescriptionList", "Notices"))
        self.prescriptionListLabel.setText(_translate("prescriptionList", "Prescriptions"))
        self.okbutton.setText(_translate("prescriptionList", "close"))
        self.events(prescriptionList)
        self.okbutton.clicked.connect(lambda : prescriptionList.close())

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
        self.tableWidget.setRowCount(len(self.pList))
        ctr = 0
        for i in self.pList:
            if ctr == 10:
                break

            self.item  = Widget1()
            self.item.noticeIdLabel.setText("ID : " + str(i["id"]))
            self.item.noticeNameLabel.setText(str(i["name"]))
            self.tableWidget.setCellWidget(ctr,0,self.item)
            self.tableWidget.setRowHeight(ctr,50)
            ctr += 1
        self.tableWidget.cellClicked.connect(self.cellClick)

    def cellClick(self,row,col):
        self.window = QDialog()
        self.dialog = prescriptionProfile()
        self.dialog.setup(self.window,self.pList[row])
        self.window.setModal(True)
        self.window.show()



