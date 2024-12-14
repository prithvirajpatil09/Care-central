from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Data.States import *
from PyQt5.QtWidgets import *
from Dialogs.messageBox import *
from Dialogs.superadmin.Events.eventProfile import *
from Dialogs.superadmin.Events.new_eventProfile import *


class Widget1(QWidget):
    def __init__(self,parent = None):
        QWidget.__init__(self,parent=None)
        layout = QFrame(self)
        layout.setGeometry(0,0,1271,119)
        self.eventIdLabel = QLabel(layout)
        self.eventIdLabel.setGeometry(QRect(10,10,170,30))
        self.eventIdLabel.setText("Id : 123")
        self.eventNameLabel = QLabel(layout)
        self.eventIdLabel.setStyleSheet("text-align:left;font-size:12pt;font-weight:550;")
        self.eventNameLabel.setGeometry(QRect(180,10,1000,30))
        self.eventNameLabel.setText("Patidar Samaj event ")
        self.eventNameLabel.setStyleSheet("align:left;font-size:15pt;font-weight:600;")
        self.addresslabel = QLabel(layout)
        self.addresslabel.setGeometry(QRect(190,40,500,80))
        self.addresslabel.setStyleSheet("font-weight: 600; font-size : 9pt")
        self.addresslabel.setText("Aghhjhjjjjjjjjjjjjjjjjjj\nshahkhj\nsajhjdffffffffffffffkas\n")
        self.cityLabel = QLabel(layout)
        self.cityLabel.setGeometry(QRect(500,10,300,30))
        self.cityLabel.setText("City : Lokandwala")
        self.cityLabel.setStyleSheet("align:left;font-size:12pt;font-weight:600;")
        self.stateLabel = QLabel(layout)
        self.stateLabel.setGeometry(QRect(900,10,300,30))
        self.stateLabel.setText("State : Bihar")
        self.stateLabel.setStyleSheet("align:left;font-size:12pt;font-weight:550;")


class myEventList(object):
    def __init__(self):
        self.dataToFill = []
    def setup(self, EventListDialog,type = None,userdata = None):
        self.type = type
        self.userdata = userdata
        EventListDialog.setObjectName("EventListDialog")
        EventListDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        EventListDialog.resize(1291, 700)
        EventListDialog.setFixedSize(1291,700)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(EventListDialog.sizePolicy().hasHeightForWidth())
        EventListDialog.setSizePolicy(sizePolicy)
        self.tableWidget = QtWidgets.QTableWidget(EventListDialog)
        self.tableWidget.setGeometry(QtCore.QRect(10, 110, 1271, 520))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.eventListHeader = QtWidgets.QLabel(EventListDialog)
        self.eventListHeader.setGeometry(QtCore.QRect(10, 0, 1281, 61))
        self.eventListHeader.setStyleSheet("font: 68 27pt \"Ubuntu\";\n"
                                           "text-decoration : underline;\n"
                                           "")
        self.eventListHeader.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.eventListHeader.setObjectName("eventListHeader")
        self.searchEventInput = QtWidgets.QLineEdit(EventListDialog)
        self.searchEventInput.setGeometry(QtCore.QRect(10, 80, 460, 31))
        self.searchEventInput.setObjectName("searchEventInput")
        self.searchButton = QtWidgets.QPushButton(EventListDialog)
        self.searchButton.setGeometry(QtCore.QRect(1170, 80, 111, 31))
        self.searchButton.setObjectName("searchButton")
        self.comboBox = QtWidgets.QComboBox(EventListDialog)
        self.comboBox.setGeometry(QtCore.QRect(470,80,200,31))
        self.comboBox.setObjectName("comboBox")
        self.exitButton = QtWidgets.QPushButton(EventListDialog)
        self.exitButton.setGeometry(QtCore.QRect(580, 650, 121, 25))
        self.exitButton.setObjectName("exitButton")

        self.retranslateUi(EventListDialog)
        QtCore.QMetaObject.connectSlotsByName(EventListDialog)

    def retranslateUi(self, EventListDialog):
        _translate = QtCore.QCoreApplication.translate
        EventListDialog.setWindowTitle(_translate("eventListDialog", "Dialog"))
        self.eventListHeader.setText(_translate("EventListDialog", "My Events"))
        self.searchEventInput.setPlaceholderText(_translate("EventListDialog", "Enter event ID or Name"))
        self.searchButton.setText(_translate("EventListDialog", "Search"))
        self.exitButton.setText(_translate("EventListDialog", "Exit"))
        self.tableWidget.horizontalHeader().hide()
        self.searchEventInput.setPlaceholderText("Enter Id")
        self.tableWidget.verticalHeader().hide()
        self.comboBox.addItem("Search By Id")
        #############

        self.fillEventdata(EventListDialog)
        self.events(EventListDialog)


    # Fil rows and column in an data
    def events(self,EventListDialog):

        # Exit Button Functionality
        self.searchButton.clicked.connect(lambda : self.addRowDataFunction(EventListDialog))
        self.exitButton.clicked.connect(lambda : self.exitFunction(EventListDialog))

    def fillEventdata(self,EventListDialog):

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

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText("event ID")


    # Add data From Database

    def addRowDataFunction(self,EventListDialog):
        print("Hey baby")
        URL = "http://127.0.0.1:8000/MDTouch/api/event/"
        self.dataToFill = []
        import requests
        if self.searchEventInput.text()== "":
            params = {}
            if self.type =='H':
                params = {
                    "hospitalid" : self.userdata["id"]
                }
            elif self.type == "BB":
                params = {
                    "bloodbankid" : self.userdata["id"]
                }
            elif self.type == 'DS':
                params = {
                    "dispensaryid" : self.userdata["id"]
                }
            elif self.type == "T":
                params = {
                    "testcentreid": self.userdata["id"]
                }
            r = requests.get(url=URL,params = params)
            self.dataToFill = r.json()
        else:
            id = self.searchEventInput.text()
            if id.isdigit():
                import requests
                r= requests.get(url=URL + str(id))
                l = r.json()
                if self.type == 'H':
                    if l["hospitalid"] != self.userdata["id"]:
                        self.window = messageBox()
                        self.window.warningBox("No Id Found")
                        return
                if self.type == 'T':
                    if l["testcentreid"] != self.userdata["id"]:
                        self.window = messageBox()
                        self.window.warningBox("No Id Found")
                        return
                if self.type == 'BB':
                    if l["bloodbankid"] != self.userdata["id"]:
                        self.window = messageBox()
                        self.window.warningBox("No Id Found")
                        return
                if self.type == 'DS':
                    if l["dispensaryid"] != self.userdata["id"]:
                        self.window = messageBox()
                        self.window.warningBox("No Id Found")
                        return
                self.dataToFill.append(l)
            else:
                self.window = messageBox()
                self.window.warningBox("Id should be a integer")

        if len(self.dataToFill) == 0:
            self.tableWidget.setRowCount(0)
            self.dialog = messageBox()
            self.dialog.infoBox("No events Found")
            return
        i = 0
        print(self.dataToFill)
        self.tableWidget.setRowCount(len(self.dataToFill))
        for hdata in self.dataToFill:

            self.table = Widget1()
            self.table.eventNameLabel.setText(str(hdata["title"]))
            self.table.eventIdLabel.setText("Id : " + str(hdata["id"]))
            self.table.cityLabel.setText("City : " + str(hdata["city"]))
            self.table.stateLabel.setText("State : " + str(hdata["state"]))
            if hdata["hospitalid"]:
                self.table.addresslabel.setText("Host : Hospital Id : " +str(hdata["hospitalid"]))
            elif hdata["bloodbankid"]:
                self.table.addresslabel.setText("Host : BloodbankCentre Id : " + str(hdata["bloodbankid"]))
            elif hdata["dispensaryid"]:
                self.table.addresslabel.setText("Host : Dispensary Id : " + str(hdata["dispensaryid"]))
            elif hdata["testcentreid"]:
                self.table.addresslabel.setText("Host : Test Center Id : " + str(hdata["testcentreid"]))
            else :
                self.table.addresslabel.setText("Host : SuperAdmin")
            if(i%2):
                self.table.setStyleSheet("background:rgb(225,225,225);")
            else:
                self.table.setStyleSheet("background : rgb(255,255,255);")
            self.tableWidget.setCellWidget(i,0,self.table)
            self.tableWidget.setRowHeight(i,120)

            i += 1
        self.tableWidget.cellClicked.connect(self.cellClick)
        self.searchEventInput.setText("")







    def cellClick(self,row,col):
        print(self.dataToFill[row])
        self.window = QDialog()
        self.dialog = new_eventProfile()
        self.dialog.setup(self.window,self.dataToFill[row])
        self.window.setModal(True)
        self.window.show()




    # Exit Button FUnction

    def exitFunction(self,EventListDialog):
        EventListDialog.close()

