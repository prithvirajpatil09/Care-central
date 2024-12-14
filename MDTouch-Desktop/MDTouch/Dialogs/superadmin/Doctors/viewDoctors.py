from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Data.States import *
from PyQt5.QtWidgets import *
from Dialogs.messageBox import *


class Widget1(QWidget):
    def __init__(self,parent = None):
        QWidget.__init__(self,parent=None)
        layout = QFrame(self)
        layout.setGeometry(0,0,1271,119)
        self.doctorIdLabel = QLabel(layout)
        self.doctorIdLabel.setGeometry(QRect(10,10,170,30))
        self.doctorIdLabel.setText("Id : 123")
        self.doctorNameLabel = QLabel(layout)
        self.doctorIdLabel.setStyleSheet("text-align:left;font-size:12pt;font-weight:550;")
        self.doctorNameLabel.setGeometry(QRect(180,10,1000,30))
        self.doctorNameLabel.setText("Patidar Samaj doctor ")
        self.doctorNameLabel.setStyleSheet("align:left;font-size:15pt;font-weight:600;")
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


class viewDoctor(object):
    def __init__(self):
        self.dataToFill = []
    def setup(self, doctorListDialog):
        doctorListDialog.setObjectName("doctorListDialog")
        doctorListDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        doctorListDialog.resize(1291, 700)
        doctorListDialog.setFixedSize(1291,700)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(doctorListDialog.sizePolicy().hasHeightForWidth())
        doctorListDialog.setSizePolicy(sizePolicy)
        self.tableWidget = QtWidgets.QTableWidget(doctorListDialog)
        self.tableWidget.setGeometry(QtCore.QRect(10, 110, 1271, 520))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.doctorListHeader = QtWidgets.QLabel(doctorListDialog)
        self.doctorListHeader.setGeometry(QtCore.QRect(10, 0, 1281, 61))
        self.doctorListHeader.setStyleSheet("font: 68 27pt \"Ubuntu\";\n"
                                                "text-decoration : underline;\n"
                                                "")
        self.doctorListHeader.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.doctorListHeader.setObjectName("doctorListHeader")
        self.searchdoctorInput = QtWidgets.QLineEdit(doctorListDialog)
        self.searchdoctorInput.setGeometry(QtCore.QRect(10, 80, 460, 31))
        self.searchdoctorInput.setObjectName("searchdoctorInput")
        self.searchButton = QtWidgets.QPushButton(doctorListDialog)
        self.searchButton.setGeometry(QtCore.QRect(1170, 80, 111, 31))
        self.searchButton.setObjectName("searchButton")
        self.comboBox = QtWidgets.QComboBox(doctorListDialog)
        self.comboBox.setGeometry(QtCore.QRect(470,80,200,31))
        self.comboBox.setObjectName("comboBox")
        self.stateComboBox = QtWidgets.QComboBox(doctorListDialog)
        self.stateComboBox.setGeometry(QtCore.QRect(670,80,200,31))
        self.exitButton = QtWidgets.QPushButton(doctorListDialog)
        self.exitButton.setGeometry(QtCore.QRect(580, 650, 121, 25))
        self.cityComboBox = QtWidgets.QComboBox(doctorListDialog)
        self.cityComboBox.setGeometry(QtCore.QRect(870,80,300,31))
        self.cityComboBox.addItem("All Cities")
        self.stateComboBox.addItem("All States")

        self.exitButton.setObjectName("exitButton")

        self.retranslateUi(doctorListDialog)
        self.stateAddFunction(doctorListDialog)
        QtCore.QMetaObject.connectSlotsByName(doctorListDialog)

    def stateAddFunction(self,doctorListDialog):
        for i in states.values():
            self.stateComboBox.addItem(i)

        self.stateComboBox.currentIndexChanged.connect(lambda : self.cityAddFunction(doctorListDialog))

    def cityAddFunction(self,doctorListDialog):
        state = self.stateComboBox.currentText()

        while self.cityComboBox.count() > 1:
            self.cityComboBox.removeItem(1)
        if state == "All States":
            return
        for i in cities[state]:
            self.cityComboBox.addItem(i)


    def retranslateUi(self, doctorListDialog):
        _translate = QtCore.QCoreApplication.translate
        doctorListDialog.setWindowTitle(_translate("doctorListDialog", "Dialog"))
        self.doctorListHeader.setText(_translate("doctorListDialog", "Doctors"))
        self.searchdoctorInput.setPlaceholderText(_translate("doctorListDialog", "Enter doctor ID or Name"))
        self.searchButton.setText(_translate("doctorListDialog", "Search"))
        self.exitButton.setText(_translate("doctorListDialog", "Exit"))
        self.tableWidget.horizontalHeader().hide()
        self.searchdoctorInput.setPlaceholderText("Enter Id")
        self.tableWidget.verticalHeader().hide()
        self.comboBox.addItem("Search By Id")
        self.comboBox.addItem("Search By Name")
        self.comboBox.currentIndexChanged.connect(lambda : self.placeholder(doctorListDialog))

        #############

        self.filldoctordata(doctorListDialog)
        self.doctors(doctorListDialog)


    # Fil rows and column in an data
    def doctors(self,doctorListDialog):

        # Exit Button Functionality
        self.searchButton.clicked.connect(lambda : self.addRowDataFunction(doctorListDialog))
        self.exitButton.clicked.connect(lambda : self.exitFunction(doctorListDialog))

    def placeholder(self,doctorListDialog):
        a = self.comboBox.currentText()
        if "Id" in a:
            self.searchdoctorInput.setPlaceholderText("Enter doctor  Id")
        else:
            self.searchdoctorInput.setPlaceholderText("Enter doctor Name")


    def filldoctordata(self,doctorListDialog):

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
        item.setText("doctor ID")


    # Add data From Database

    def addRowDataFunction(self,doctorListDialog):
        URL = "http://127.0.0.1:8000/MDTouch/api/doctor/"
        self.dataToFill = []
        if self.searchdoctorInput.text()== "":
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
            id =  self.searchdoctorInput.text()
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
            name = self.searchdoctorInput.text()
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
            self.dialog.infoBox("No doctors Found")
            return
        i = 0
        print(self.dataToFill)
        self.tableWidget.setRowCount(len(self.dataToFill))
        for hdata in self.dataToFill:

            self.table = Widget1()
            self.table.doctorNameLabel.setText(str(hdata["firstName"]) + " " + str(hdata["lastName"]))
            self.table.doctorIdLabel.setText("Id : " + str(hdata["id"]))
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
        self.searchdoctorInput.setText("")







    def cellClick(self,row,col):
        print(self.dataToFill[row])
        print(row,col)


    # Exit Button FUnction

    def exitFunction(self,doctorListDialog):
        doctorListDialog.close()

