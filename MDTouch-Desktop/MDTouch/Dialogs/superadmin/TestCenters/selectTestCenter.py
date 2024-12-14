from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Data.States import *
from Dialogs.superadmin.TestCenters.removeTestCenter import *

class selectTestCenter(object):
    def __init__(self):
        self.last_city = ''
        self.hospital_list = []
    def setup(self, selectTestCenter):
        selectTestCenter.setObjectName("selectTestCenter")
        selectTestCenter.resize(366, 323)
        self.frame = QtWidgets.QFrame(selectTestCenter)
        self.frame.setGeometry(QtCore.QRect(10, 60, 341, 211))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.cityComboBox = QtWidgets.QComboBox(self.frame)
        self.cityComboBox.setGeometry(QtCore.QRect(160, 120, 161, 27))
        self.cityComboBox.setObjectName("cityComboBox")
        self.testCenterComboBox = QtWidgets.QComboBox(self.frame)
        self.testCenterComboBox.setGeometry(QtCore.QRect(160, 170, 161, 27))
        self.testCenterComboBox.setObjectName("testCenterComboBox")
        self.stateComboBox = QtWidgets.QComboBox(self.frame)
        self.stateComboBox.setGeometry(QtCore.QRect(160, 70, 161, 27))
        self.stateComboBox.setObjectName("stateComboBox")
        self.cityLabel = QtWidgets.QLabel(self.frame)
        self.cityLabel.setGeometry(QtCore.QRect(40, 120, 111, 31))
        self.cityLabel.setObjectName("cityLabel")
        self.testCenterLabel = QtWidgets.QLabel(self.frame)
        self.testCenterLabel.setGeometry(QtCore.QRect(40, 170, 111, 31))
        self.testCenterLabel.setObjectName("testCenterLabel")
        self.stateLabel = QtWidgets.QLabel(self.frame)
        self.stateLabel.setGeometry(QtCore.QRect(40, 70, 111, 31))
        self.stateLabel.setObjectName("stateLabel")
        self.searchByID = QtWidgets.QLineEdit(self.frame)
        self.searchByID.setGeometry(QtCore.QRect(40, 10, 281, 27))
        self.searchByID.setObjectName("searchByID")
        self.ORLabel = QtWidgets.QLabel(self.frame)
        self.ORLabel.setGeometry(QtCore.QRect(120, 40, 111, 31))
        self.ORLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ORLabel.setObjectName("ORLabel")
        self.title = QtWidgets.QLabel(selectTestCenter)
        self.title.setGeometry(QtCore.QRect(10, 0, 341, 51))
        self.title.setObjectName("title")
        self.removeButton = QtWidgets.QPushButton(selectTestCenter)
        self.removeButton.setGeometry(QtCore.QRect(140, 280, 80, 28))
        self.removeButton.setObjectName("removeButton")

        self.retranslateUi(selectTestCenter)
        QtCore.QMetaObject.connectSlotsByName(selectTestCenter)

    def retranslateUi(self, selectTestCenter):
        _translate = QtCore.QCoreApplication.translate
        selectTestCenter.setWindowTitle(_translate("selectTestCenter", " "))
        self.cityLabel.setText(_translate("selectTestCenter", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">City : </span></p></body></html>"))
        self.testCenterLabel.setText(_translate("selectTestCenter", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Test Center :</span></p></body></html>"))
        self.stateLabel.setText(_translate("selectTestCenter", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">State : </span></p></body></html>"))
        self.searchByID.setPlaceholderText(_translate("selectTestCenter", "Search by Test Center ID"))
        self.ORLabel.setText(_translate("selectTestCenter", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">OR</span></p></body></html>"))
        self.title.setText(_translate("selectTestCenter", "<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; font-weight:600; text-decoration: underline;\">Select Test Center</span></p></body></html>"))
        self.removeButton.setText(_translate("selectTestCenter", "SELECT"))

        self.stateAddFunction(selectTestCenter)
        self.clickEvents(selectTestCenter)

    def clickEvents(self, parent):
        self.removeButton.clicked.connect(lambda: self.clickOnRemoveButton(parent))

    def clickOnRemoveButton(self, parent):
        if self.testCenterComboBox.count() == 0 and self.searchByID.text() == "":
            self.dialog = messageBox()
            self.dialog.warningBox("Select the Test Center or Enter the Id")
            return
        if self.searchByID.text() != "":
            id = self.searchByID.text()
            print(id)
            if id.isdigit():
                import requests
                url = "http://127.0.0.1:8000/api/testcentre/" + id
                r = requests.get(url= url)
                l = r.json()
                print(l)
                if l == {'detail': 'Not found.'}:
                    self.dialog = messageBox()
                    self.dialog.warningBox("No Id Match")
                    return
                else:
                    self.window = QDialog()
                    self.dialog = removeTestCenter()
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
        for i in self.testCenter_list:
            if i["name"] == self.testCenterComboBox.currentText():
                hdata = i
        parent.close()
        self.window = QDialog()
        self.dialog = removeTestCenter()
        self.dialog.setup(self.window,hdata)
        self.window.setModal(True)
        self.window.show()

    def stateAddFunction(self,parent):
        for i in states.values():
            self.stateComboBox.addItem(i)
        for i in cities["Andhra Pradesh"]:
            self.cityComboBox.addItem(i)
        self.stateComboBox.currentIndexChanged.connect(lambda : self.cityAddFunction(parent))
        self.stateComboBox.currentIndexChanged.connect(lambda :self.testCenterComboBoxAdd(parent))

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
            self.cityComboBox.currentIndexChanged.connect(lambda :self.testCenterComboBoxAdd(parent))

    def testCenterComboBoxAdd(self,parent):
        if self.last_city == self.cityComboBox.currentText() or self.cityComboBox.count() != len(cities[self.stateComboBox.currentText()]) or self.cityComboBox.itemText(self.cityComboBox.count()-1) != cities[self.stateComboBox.currentText()][-1]:
            return
        self.last_city = self.cityComboBox.currentText()
        # First Erase all testCenters
        i = self.testCenterComboBox.count()
        while i > 0:
            i -= 1
            self.testCenterComboBox.removeItem(0)

        import requests
        print(self.cityComboBox.currentText())
        URL = "http://127.0.0.1:8000/api/testcentre/"
        param ={
            "city": self.cityComboBox.currentText()
        }
        r = requests.get(url=URL,params=param)
        l = r.json()
        print(l)
        self.testCenter_list = l
        for i in l:
            self.testCenterComboBox.addItem(str(i["name"]))
