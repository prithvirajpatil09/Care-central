from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Data.States import *
from PyQt5.QtWidgets import *
from Dialogs.messageBox import *
from Dialogs.superadmin.BloodBanks.bloodBankProfile import *


class Widget1(QWidget):
    def __init__(self,parent = None):
        QWidget.__init__(self,parent=None)
        layout = QFrame(self)
        layout.setGeometry(0,0,1271,119)
        self.bloodBankCenterIdLabel = QLabel(layout)
        self.bloodBankCenterIdLabel.setGeometry(QRect(10,10,170,30))
        self.bloodBankCenterIdLabel.setText("Id : 123")
        self.bloodBankCenterNameLabel = QLabel(layout)
        self.bloodBankCenterIdLabel.setStyleSheet("text-align:left;font-size:12pt;font-weight:550;")
        self.bloodBankCenterNameLabel.setGeometry(QRect(180,10,1000,30))
        self.bloodBankCenterNameLabel.setText("Patidar Samaj bloodBankCenter ")
        self.bloodBankCenterNameLabel.setStyleSheet("align:left;font-size:15pt;font-weight:600;")
        self.addresslabel = QLabel(layout)
        self.addresslabel.setGeometry(QRect(190,40,500,80))
        self.addresslabel.setStyleSheet("font-weight: 500; font-size : 9pt")
        self.addresslabel.setText("Aghhjhjjjjjjjjjjjjjjjjjj\nshahkhj\nsajhjdffffffffffffffkas\n")
        self.cityLabel = QLabel(layout)
        self.cityLabel.setGeometry(QRect(500,80,300,30))
        self.cityLabel.setText("City : Lokandwala")
        self.cityLabel.setStyleSheet("align:left;font-size:12pt;font-weight:600;")
        self.stateLabel = QLabel(layout)
        self.stateLabel.setGeometry(QRect(900,80,300,30))
        self.stateLabel.setText("State : Bihar")
        self.stateLabel.setStyleSheet("align:left;font-size:12pt;font-weight:550;")


class viewBloodBankCenter(object):
    def __init__(self):
        self.dataToFill = []
    def setup(self, bloodBankCenterListDialog):
        bloodBankCenterListDialog.setObjectName("bloodBankCenterListDialog")
        bloodBankCenterListDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        bloodBankCenterListDialog.resize(1291, 700)
        bloodBankCenterListDialog.setFixedSize(1291,700)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(bloodBankCenterListDialog.sizePolicy().hasHeightForWidth())
        bloodBankCenterListDialog.setSizePolicy(sizePolicy)
        self.tableWidget = QtWidgets.QTableWidget(bloodBankCenterListDialog)
        self.tableWidget.setGeometry(QtCore.QRect(10, 110, 1271, 520))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.bloodBankCenterListHeader = QtWidgets.QLabel(bloodBankCenterListDialog)
        self.bloodBankCenterListHeader.setGeometry(QtCore.QRect(10, 0, 1281, 61))
        self.bloodBankCenterListHeader.setStyleSheet("font: 68 27pt \"Ubuntu\";\n"
                                                     "text-decoration : underline;\n"
                                                     "")
        self.bloodBankCenterListHeader.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.bloodBankCenterListHeader.setObjectName("bloodBankCenterListHeader")
        self.searchbloodBankCenterInput = QtWidgets.QLineEdit(bloodBankCenterListDialog)
        self.searchbloodBankCenterInput.setGeometry(QtCore.QRect(10, 80, 460, 31))
        self.searchbloodBankCenterInput.setObjectName("searchbloodBankCenterInput")
        self.searchButton = QtWidgets.QPushButton(bloodBankCenterListDialog)
        self.searchButton.setGeometry(QtCore.QRect(1170, 80, 111, 31))
        self.searchButton.setObjectName("searchButton")
        self.comboBox = QtWidgets.QComboBox(bloodBankCenterListDialog)
        self.comboBox.setGeometry(QtCore.QRect(470,80,200,31))
        self.comboBox.setObjectName("comboBox")
        self.stateComboBox = QtWidgets.QComboBox(bloodBankCenterListDialog)
        self.stateComboBox.setGeometry(QtCore.QRect(670,80,200,31))
        self.exitButton = QtWidgets.QPushButton(bloodBankCenterListDialog)
        self.exitButton.setGeometry(QtCore.QRect(580, 650, 121, 25))
        self.cityComboBox = QtWidgets.QComboBox(bloodBankCenterListDialog)
        self.cityComboBox.setGeometry(QtCore.QRect(870,80,300,31))
        self.cityComboBox.addItem("All Cities")
        self.stateComboBox.addItem("All States")

        self.exitButton.setObjectName("exitButton")

        self.retranslateUi(bloodBankCenterListDialog)
        self.stateAddFunction(bloodBankCenterListDialog)
        QtCore.QMetaObject.connectSlotsByName(bloodBankCenterListDialog)

    def stateAddFunction(self,bloodBankCenterListDialog):
        for i in states.values():
            self.stateComboBox.addItem(i)

        self.stateComboBox.currentIndexChanged.connect(lambda : self.cityAddFunction(bloodBankCenterListDialog))

    def cityAddFunction(self,bloodBankCenterListDialog):
        state = self.stateComboBox.currentText()

        while self.cityComboBox.count() > 1:
            self.cityComboBox.removeItem(1)
        if state == "All States":
            return
        for i in cities[state]:
            self.cityComboBox.addItem(i)


    def retranslateUi(self, bloodBankCenterListDialog):
        _translate = QtCore.QCoreApplication.translate
        bloodBankCenterListDialog.setWindowTitle(_translate("bloodBankCenterListDialog", "Dialog"))
        self.bloodBankCenterListHeader.setText(_translate("bloodBankCenterListDialog", "Blood Bank Center"))
        self.searchbloodBankCenterInput.setPlaceholderText(_translate("bloodBankCenterListDialog", "Enter bloodBankCenter ID or Name"))
        self.searchButton.setText(_translate("bloodBankCenterListDialog", "Search"))
        self.exitButton.setText(_translate("bloodBankCenterListDialog", "Exit"))
        self.tableWidget.horizontalHeader().hide()
        self.searchbloodBankCenterInput.setPlaceholderText("Enter Id")
        self.tableWidget.verticalHeader().hide()
        self.comboBox.addItem("Search By Id")
        self.comboBox.addItem("Search By Name")
        self.comboBox.currentIndexChanged.connect(lambda : self.placeholder(bloodBankCenterListDialog))

        #############

        self.fillbloodBankCenterdata(bloodBankCenterListDialog)
        self.bloodBankCenters(bloodBankCenterListDialog)


    # Fil rows and column in an data
    def bloodBankCenters(self,bloodBankCenterListDialog):

        # Exit Button Functionality
        self.searchButton.clicked.connect(lambda : self.addRowDataFunction(bloodBankCenterListDialog))
        self.exitButton.clicked.connect(lambda : self.exitFunction(bloodBankCenterListDialog))

    def placeholder(self,bloodBankCenterListDialog):
        a = self.comboBox.currentText()
        if "Id" in a:
            self.searchbloodBankCenterInput.setPlaceholderText("Enter bloodBankCenter  Id")
        else:
            self.searchbloodBankCenterInput.setPlaceholderText("Enter bloodBankCenter Name")


    def fillbloodBankCenterdata(self,bloodBankCenterListDialog):

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
        item.setText("bloodBankCenter ID")


    # Add data From Database

    def addRowDataFunction(self,bloodBankCenterListDialog):
        print("Hey baby")
        URL = "http://127.0.0.1:8000/MDTouch/api/bloodbankcenter/"
        self.dataToFill = []
        if self.searchbloodBankCenterInput.text()== "":
            print("Yes")
            if self.stateComboBox.currentText() == "All States":
                print("All States")
                import requests
                r = requests.get(url = URL)
                l = r.json()
                self.dataToFill = l
                print(self.dataToFill)
            else:
                if self.cityComboBox.currentText() == "All Cities":
                    params = {
                        "state": self.stateComboBox.currentText()
                    }
                    import requests
                    r = requests.get(url = URL,params=params)
                    l = r.json()
                    self.dataToFill = l
                else:
                    params = {
                        "state": self.stateComboBox.currentText(),
                        "city": self.cityComboBox.currentText()
                    }
                    import requests
                    r = requests.get(url = URL,params=params)
                    l = r.json()
                    self.dataToFill = l
            print(self.dataToFill)
        elif self.comboBox.currentText() == "Search By Id":
            id =  self.searchbloodBankCenterInput.text()
            if id.isdigit():
                import requests
                url = URL + id
                r = requests.get(url= url)
                m = r.json()
                print(m)
                if m == {'detail': 'Not found.'}:
                    self.dialog = messageBox()
                    self.dialog.infoBox("No Id Match")
                    self.tableWidget.setRowCount(0)
                    return
                else:
                    self.dataToFill.append(m)
            else:
                self.window = messageBox()
                self.window.infoBox("Id should be a integer")
                self.tableWidget.setRowCount(0)
                return
        else:
            name = self.searchbloodBankCenterInput.text()
            print(name)
            if self.stateComboBox.currentText() == "All States":
                import requests
                r = requests.get(url= URL)
                l = r.json()
                from difflib import SequenceMatcher
                for i in l:
                    if SequenceMatcher(None,i["name"].lower(),name.lower()).ratio() >= 0.5 or name.lower() in i["name"].lower():
                        self.dataToFill.append(i)
            else:
                if self.cityComboBox.currentText() == "All Cities":
                    params = {
                        "state": self.stateComboBox.currentText()
                    }
                    import requests
                    r = requests.get(url = URL,params=params)
                    l = r.json()
                    from difflib import SequenceMatcher
                    for i in l:
                        if SequenceMatcher(None,i["name"].lower(),name.lower()).ratio() >= 0.5 or name.lower() in i["name"].lower():
                            self.dataToFill.append(i)
                else:
                    params = {
                        "state": self.stateComboBox.currentText(),
                        "city": self.cityComboBox.currentText()
                    }
                    import requests
                    r = requests.get(url = URL,params=params)
                    l = r.json()
                    from difflib import SequenceMatcher
                    for i in l:
                        if SequenceMatcher(None,i["name"].lower(),name.lower()).ratio() >= 0.5 or name.lower() in i["name"].lower() :
                            self.dataToFill.append(i)
        print("Hello")
        if len(self.dataToFill) == 0:
            self.tableWidget.setRowCount(0)
            self.dialog = messageBox()
            self.dialog.infoBox("No bloodBankCenters Found")
            return
        i = 0
        print(self.dataToFill)
        self.tableWidget.setRowCount(len(self.dataToFill))
        for hdata in self.dataToFill:

            self.table = Widget1()
            self.table.bloodBankCenterNameLabel.setText(str(hdata["name"]))
            self.table.bloodBankCenterIdLabel.setText("Id : " + str(hdata["id"]))
            self.table.cityLabel.setText("City : " + str(hdata["city"]))
            self.table.stateLabel.setText("State : " + str(hdata["state"]))
            self.table.addresslabel.setText(hdata["address"])
            if(i%2):
                self.table.setStyleSheet("background:rgb(225,225,225);")
            else:
                self.table.setStyleSheet("background : rgb(255,255,255);")
            self.tableWidget.setCellWidget(i,0,self.table)
            self.tableWidget.setRowHeight(i,120)

            i += 1
        self.tableWidget.cellClicked.connect(self.cellClick)
        self.searchbloodBankCenterInput.setText("")







    def cellClick(self,row,col):
        self.window = QDialog()
        self.dialog = bloodBankProfile()
        self.dialog.setup(self.window,self.dataToFill[row])
        self.window.setModal(True)
        self.window.show()
        print(row,col)


    # Exit Button FUnction

    def exitFunction(self,bloodBankCenterListDialog):
        bloodBankCenterListDialog.close()

