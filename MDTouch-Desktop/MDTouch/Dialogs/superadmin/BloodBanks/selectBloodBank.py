from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Dialogs.superadmin.BloodBanks.removeBloodBank import *
from Data.States import *
from Dialogs.messageBox import *

class selectBloodBank(object):
    def __init__(self):
        self.last_city = ''
        self.bloodBank_list = []
    def setup(self, selectBloodBank):
        selectBloodBank.setObjectName("selectBloodBank")
        selectBloodBank.resize(380, 350)
        selectBloodBank.setMinimumSize(QtCore.QSize(380, 350))
        selectBloodBank.setMaximumSize(QtCore.QSize(380, 350))
        self.frame = QtWidgets.QFrame(selectBloodBank)
        self.frame.setGeometry(QtCore.QRect(10, 60, 351, 221))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.cityComboBox = QtWidgets.QComboBox(self.frame)
        self.cityComboBox.setGeometry(QtCore.QRect(160, 130, 161, 27))
        self.cityComboBox.setObjectName("cityComboBox")
        self.bloodBankComboBox = QtWidgets.QComboBox(self.frame)
        self.bloodBankComboBox.setGeometry(QtCore.QRect(160, 180, 161, 27))
        self.bloodBankComboBox.setObjectName("bloodBankComboBox")
        self.stateComboBox = QtWidgets.QComboBox(self.frame)
        self.stateComboBox.setGeometry(QtCore.QRect(160, 80, 161, 27))
        self.stateComboBox.setObjectName("stateComboBox")
        self.cityLabel = QtWidgets.QLabel(self.frame)
        self.cityLabel.setGeometry(QtCore.QRect(40, 130, 111, 31))
        self.cityLabel.setObjectName("cityLabel")
        self.bloodBankLabel = QtWidgets.QLabel(self.frame)
        self.bloodBankLabel.setGeometry(QtCore.QRect(40, 180, 111, 31))
        self.bloodBankLabel.setObjectName("bloodBankLabel")
        self.stateLabel = QtWidgets.QLabel(self.frame)
        self.stateLabel.setGeometry(QtCore.QRect(40, 80, 111, 31))
        self.stateLabel.setObjectName("stateLabel")
        self.ORLabel = QtWidgets.QLabel(self.frame)
        self.ORLabel.setGeometry(QtCore.QRect(130, 50, 111, 31))
        self.ORLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ORLabel.setObjectName("ORLabel")
        self.searchByID = QtWidgets.QLineEdit(self.frame)
        self.searchByID.setGeometry(QtCore.QRect(40, 20, 281, 27))
        self.searchByID.setObjectName("searchByID")
        self.removeButton = QtWidgets.QPushButton(selectBloodBank)
        self.removeButton.setGeometry(QtCore.QRect(130, 310, 131, 28))
        self.removeButton.setObjectName("removeButton")
        self.title = QtWidgets.QLabel(selectBloodBank)
        self.title.setGeometry(QtCore.QRect(20, 0, 331, 51))
        self.title.setObjectName("title")

        self.retranslateUi(selectBloodBank)
        QtCore.QMetaObject.connectSlotsByName(selectBloodBank)

    def retranslateUi(self, selectBloodBank):
        _translate = QtCore.QCoreApplication.translate
        selectBloodBank.setWindowTitle(_translate("selectBloodBank", " "))
        self.cityLabel.setText(_translate("selectBloodBank", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">City : </span></p></body></html>"))
        self.bloodBankLabel.setText(_translate("selectBloodBank", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Blood Bank :</span></p></body></html>"))
        self.stateLabel.setText(_translate("selectBloodBank", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">State : </span></p></body></html>"))
        self.ORLabel.setText(_translate("selectBloodBank", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">OR</span></p></body></html>"))
        self.searchByID.setPlaceholderText(_translate("selectBloodBank", "Search by Blood Bank Id"))
        self.removeButton.setText(_translate("selectBloodBank", "SELECT"))
        self.title.setText(_translate("selectBloodBank", "<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; font-weight:600; text-decoration: underline;\">Select Blood Bank</span></p></body></html>"))

        self.stateAddFunction(selectBloodBank)
        self.clickEvents(selectBloodBank)

    def clickEvents(self, parent):
        self.removeButton.clicked.connect(lambda: self.clickOnRemoveBloodBank(parent))

    def clickOnRemoveBloodBank(self, parent):
        if self.bloodBankComboBox.count() == 0 and self.searchByID.text() == "":
            self.dialog = messageBox()
            self.dialog.warningBox("Select the Blood Bank or Enter the Id")
            return
        if self.searchByID.text() != "":
            id = self.searchByID.text()
            print(id)
            if id.isdigit():
                import requests
                url = "http://127.0.0.1:8000/api/bloodbankcenter/" + id
                r = requests.get(url= url)
                l = r.json()
                print(l)
                if l == {'detail': 'Not found.'}:
                    self.dialog = messageBox()
                    self.dialog.warningBox("No Id Match")
                    return
                else:
                    self.window = QDialog()
                    self.dialog = removeBloodBank()
                    self.dialog.setup(self.window,l)
                    self.window.setModal(True)
                    self.window.show()
                    parent.close()
                    return
            else:
                self.dialog = messageBox()
                self.dialog.warningBox("Id must be integer")
            return
        hdata = {}
        for i in self.bloodBank_list:
            if i["name"] == self.bloodBankComboBox.currentText():
                hdata = i
        parent.close()
        self.window = QDialog()
        self.dialog = removeBloodBank()
        self.dialog.setup(self.window,hdata)
        self.window.setModal(True)
        self.window.show()

    def stateAddFunction(self,parent):
        for i in states.values():
            self.stateComboBox.addItem(i)
        for i in cities["Andhra Pradesh"]:
            self.cityComboBox.addItem(i)
        self.stateComboBox.currentIndexChanged.connect(lambda : self.cityAddFunction(parent))
        self.stateComboBox.currentIndexChanged.connect(lambda :self.bloodBankComboBoxAdd(parent))

    def cityAddFunction(self,parent):
        state = self.stateComboBox.currentText()
        i = self.cityComboBox.count()
        flag = True
        while i > 0:
            flag = False
            self.cityComboBox.removeItem(0)
            i-=1
        flag = True
        for i in cities[state]:
            flag = False
            self.cityComboBox.addItem(i)
        flag = True
        if flag :
            self.cityComboBox.currentIndexChanged.connect(lambda :self.bloodBankComboBoxAdd(parent))

    def bloodBankComboBoxAdd(self,parent):
        if self.last_city == self.cityComboBox.currentText() or self.cityComboBox.count() != len(cities[self.stateComboBox.currentText()]) or self.cityComboBox.itemText(self.cityComboBox.count()-1) != cities[self.stateComboBox.currentText()][-1]:
            return
        self.last_city = self.cityComboBox.currentText()
        # First Erase all bloodBanks
        i = self.bloodBankComboBox.count()
        while i > 0:
            i -= 1
            self.bloodBankComboBox.removeItem(0)

        import requests
        print(self.cityComboBox.currentText())
        URL = "http://127.0.0.1:8000/api/bloodbankcenter/"
        param ={
            "city": self.cityComboBox.currentText()
        }
        r = requests.get(url=URL,params=param)
        l = r.json()
        print(l)
        self.bloodBank_list = l
        for i in l:
            self.bloodBankComboBox.addItem(str(i["name"]))
