from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Data.disease import *
from Data.States import *
from PyQt5 import QtCore, QtGui, QtWidgets

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

class DiseaseList(object):
    def setup(self, DiseaseList):
        DiseaseList.setObjectName("DiseaseList")
        DiseaseList.resize(640, 480)
        self.frame = QtWidgets.QFrame(DiseaseList)
        self.frame.setGeometry(QtCore.QRect(10, 10, 621, 421))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.diseaseLabel = QtWidgets.QLabel(self.frame)
        self.diseaseLabel.setGeometry(QtCore.QRect(250, 0, 131, 41))
        self.diseaseLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.diseaseLabel.setObjectName("diseaseLabel")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(10, 91, 601, 321))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.stateComboBox = QtWidgets.QComboBox(self.frame)
        self.stateComboBox.setGeometry(QtCore.QRect(10, 50, 221, 25))
        self.stateComboBox.setObjectName("stateComboBox")
        self.cityComboBox = QtWidgets.QComboBox(self.frame)
        self.cityComboBox.setGeometry(QtCore.QRect(240, 50, 221, 25))
        self.cityComboBox.setObjectName("cityComboBox")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(470, 50, 141, 25))
        self.pushButton.setObjectName("pushButton")
        self.okbutton = QtWidgets.QPushButton(DiseaseList)
        self.okbutton.setGeometry(QtCore.QRect(280, 440, 89, 25))
        self.okbutton.setObjectName("okbutton")

        self.retranslateUi(DiseaseList)
        QtCore.QMetaObject.connectSlotsByName(DiseaseList)
        self.okbutton.clicked.connect(lambda : DiseaseList.close())

    def retranslateUi(self, DiseaseList):
        _translate = QtCore.QCoreApplication.translate
        DiseaseList.setWindowTitle(_translate("DiseaseList", "Disease"))
        self.diseaseLabel.setText(_translate("DiseaseList", "Disease"))
        self.pushButton.setText(_translate("DiseaseList", "Search"))
        self.okbutton.setText(_translate("DiseaseList", "close"))
        self.stateAddFunction(DiseaseList)
        self.cityAddFunction(DiseaseList)
        self.pushButton.clicked.connect(lambda : self.events())

    def events(self):

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
        self.tableWidget.setRowCount(len(disease))
        ctr = 0
        for i in disease:

            self.item  = Widget1()
            self.item.noticeIdLabel.setText(i)
            import random
            self.item.noticeNameLabel.setText(str(random.randint(0,10)))
            self.tableWidget.setCellWidget(ctr,0,self.item)
            self.tableWidget.setRowHeight(ctr,50)
            ctr += 1


    def stateAddFunction(self,EventListDialog):
        for i in states.values():
            self.stateComboBox.addItem(i)

        self.stateComboBox.currentIndexChanged.connect(lambda : self.cityAddFunction(EventListDialog))

    def cityAddFunction(self,EventListDialog):
        state = self.stateComboBox.currentText()

        while self.cityComboBox.count() > 0:
            self.cityComboBox.removeItem(0)
        if state == "All States":
            return
        for i in cities[state]:
            self.cityComboBox.addItem(i)

