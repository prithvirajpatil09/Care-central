from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from Data.States import *
from Dialogs.superadmin.Hospitals.removeHospital import *
from Dialogs.messageBox import *

class selectHospital(object):
    def __init__(self):
        self.last_city = ''
        self.hospital_list = []

    def setup(self, selectHospital):
        selectHospital.setObjectName("selectHospital")
        selectHospital.resize(362, 331)
        self.title = QtWidgets.QLabel(selectHospital)
        self.title.setGeometry(QtCore.QRect(30, 0, 321, 51))
        self.title.setObjectName("title")
        self.frame = QtWidgets.QFrame(selectHospital)
        self.frame.setGeometry(QtCore.QRect(10, 60, 341, 211))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.cityComboBox = QtWidgets.QComboBox(self.frame)
        self.cityComboBox.setGeometry(QtCore.QRect(160, 120, 161, 27))
        self.cityComboBox.setObjectName("cityComboBox")
        self.hospitalComboBox = QtWidgets.QComboBox(self.frame)
        self.hospitalComboBox.setGeometry(QtCore.QRect(160, 170, 161, 27))
        self.hospitalComboBox.setObjectName("hospitalComboBox")
        self.stateComboBox = QtWidgets.QComboBox(self.frame)
        self.stateComboBox.setGeometry(QtCore.QRect(160, 70, 161, 27))
        self.stateComboBox.setObjectName("stateComboBox")
        self.cityLabel = QtWidgets.QLabel(self.frame)
        self.cityLabel.setGeometry(QtCore.QRect(40, 120, 111, 31))
        self.cityLabel.setObjectName("cityLabel")
        self.hospitalLabel = QtWidgets.QLabel(self.frame)
        self.hospitalLabel.setGeometry(QtCore.QRect(40, 170, 111, 31))
        self.hospitalLabel.setObjectName("hospitalLabel")
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
        self.removeButton = QtWidgets.QPushButton(selectHospital)
        self.removeButton.setGeometry(QtCore.QRect(140, 290, 80, 28))
        self.removeButton.setObjectName("removeButton")

        self.retranslateUi(selectHospital)
        QtCore.QMetaObject.connectSlotsByName(selectHospital)

    def retranslateUi(self, selectHospital):
        _translate = QtCore.QCoreApplication.translate
        selectHospital.setWindowTitle(_translate("selectHospital", " "))
        self.title.setText(_translate("selectHospital", "<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; font-weight:600; text-decoration: underline;\">Select Hospital</span></p></body></html>"))
        self.cityLabel.setText(_translate("selectHospital", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">City : </span></p></body></html>"))
        self.hospitalLabel.setText(_translate("selectHospital", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Hospital</span></p></body></html>"))
        self.stateLabel.setText(_translate("selectHospital", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">State : </span></p></body></html>"))
        self.searchByID.setPlaceholderText(_translate("selectHospital", "Search by Hospital ID"))
        self.ORLabel.setText(_translate("selectHospital", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">OR</span></p></body></html>"))
        self.removeButton.setText(_translate("selectHospital", "SELECT"))

        self.stateAddFunction(selectHospital)
        self.clickEvents(selectHospital)

    def clickEvents(self, parent):
        self.removeButton.clicked.connect(lambda: self.clickOnRemoveHospital(parent))

    def clickOnRemoveHospital(self, parent):
        if self.hospitalComboBox.count() == 0 and self.searchByID.text() == "":
            self.dialog = messageBox()
            self.dialog.warningBox("Select the Hospital or Enter the Id")
            return
        if self.searchByID.text() != "":
            id = self.searchByID.text()
            print(id)
            if id.isdigit():
                import requests
                url = "http://127.0.0.1:8000/MDTouch/api/hospital/" + id
                r = requests.get(url= url)
                l = r.json()
                print(l)
                if l == {'detail': 'Not found.'}:
                    self.dialog = messageBox()
                    self.dialog.warningBox("No Id Match")
                    return
                else:
                    self.window = QDialog()
                    self.dialog = removeHospital()
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
        for i in self.hospital_list:
            if i["name"] == self.hospitalComboBox.currentText():
                hdata = i
        parent.close()
        self.window = QDialog()
        self.dialog = removeHospital()
        self.dialog.setup(self.window,hdata)
        self.window.setModal(True)
        self.window.show()

    def stateAddFunction(self,parent):
        for i in states.values():
            self.stateComboBox.addItem(i)
        for i in cities["Andhra Pradesh"]:
            self.cityComboBox.addItem(i)
        self.stateComboBox.currentIndexChanged.connect(lambda : self.cityAddFunction(parent))
        self.stateComboBox.currentIndexChanged.connect(lambda :self.hospitalComboBoxAdd(parent))

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
            self.cityComboBox.currentIndexChanged.connect(lambda :self.hospitalComboBoxAdd(parent))

    def hospitalComboBoxAdd(self,parent):
        if self.last_city == self.cityComboBox.currentText() or self.cityComboBox.count() != len(cities[self.stateComboBox.currentText()]) or self.cityComboBox.itemText(self.cityComboBox.count()-1) != cities[self.stateComboBox.currentText()][-1]:
            return
        self.last_city = self.cityComboBox.currentText()
        # First Erase all Hospitals
        i = self.hospitalComboBox.count()
        while i > 0:
            i -= 1
            self.hospitalComboBox.removeItem(0)

        import requests
        print(self.cityComboBox.currentText())
        URL = "http://127.0.0.1:8000/api/hospital/"
        param ={
            "city": self.cityComboBox.currentText()
        }
        r = requests.get(url=URL,params=param)
        l = r.json()
        print(l)
        self.hospital_list = l
        for i in l:
            self.hospitalComboBox.addItem(str(i["name"]))
