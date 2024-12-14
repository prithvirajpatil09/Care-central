from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Data.States import *
from Dialogs.superadmin.EmergencyServices.removeEmergencyService import *
from Dialogs.messageBox import *

class selectEmergencyService(object):
    def __init__(self):
        self.last_city = ''
        self.emergencyService_list = []
    def setup(self, selectEmergencyService):
        selectEmergencyService.setObjectName("selectEmergencyService")
        selectEmergencyService.resize(415, 313)
        selectEmergencyService.setMinimumSize(QtCore.QSize(415, 313))
        selectEmergencyService.setMaximumSize(QtCore.QSize(415, 313))
        self.title = QtWidgets.QLabel(selectEmergencyService)
        self.title.setGeometry(QtCore.QRect(10, 0, 391, 51))
        self.title.setObjectName("title")
        self.frame = QtWidgets.QFrame(selectEmergencyService)
        self.frame.setGeometry(QtCore.QRect(10, 60, 391, 211))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.cityComboBox = QtWidgets.QComboBox(self.frame)
        self.cityComboBox.setGeometry(QtCore.QRect(200, 120, 161, 27))
        self.cityComboBox.setObjectName("cityComboBox")
        self.emergencyServiceComboBox = QtWidgets.QComboBox(self.frame)
        self.emergencyServiceComboBox.setGeometry(QtCore.QRect(200, 160, 161, 27))
        self.emergencyServiceComboBox.setObjectName("emergencyServiceComboBox")
        self.stateComboBox = QtWidgets.QComboBox(self.frame)
        self.stateComboBox.setGeometry(QtCore.QRect(200, 80, 161, 27))
        self.stateComboBox.setObjectName("stateComboBox")
        self.cityLabel = QtWidgets.QLabel(self.frame)
        self.cityLabel.setGeometry(QtCore.QRect(20, 120, 111, 31))
        self.cityLabel.setObjectName("cityLabel")
        self.emergencyServiceLabel = QtWidgets.QLabel(self.frame)
        self.emergencyServiceLabel.setGeometry(QtCore.QRect(20, 160, 161, 31))
        self.emergencyServiceLabel.setObjectName("emergencyServiceLabel")
        self.stateLabel = QtWidgets.QLabel(self.frame)
        self.stateLabel.setGeometry(QtCore.QRect(20, 80, 111, 31))
        self.stateLabel.setObjectName("stateLabel")
        self.ORLabel = QtWidgets.QLabel(self.frame)
        self.ORLabel.setGeometry(QtCore.QRect(140, 40, 111, 31))
        self.ORLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ORLabel.setObjectName("ORLabel")
        self.searchByID = QtWidgets.QLineEdit(self.frame)
        self.searchByID.setGeometry(QtCore.QRect(20, 10, 341, 27))
        self.searchByID.setObjectName("searchByID")
        self.removeButton = QtWidgets.QPushButton(selectEmergencyService)
        self.removeButton.setGeometry(QtCore.QRect(170, 280, 80, 28))
        self.removeButton.setObjectName("removeButton")

        self.retranslateUi(selectEmergencyService)
        QtCore.QMetaObject.connectSlotsByName(selectEmergencyService)

    def retranslateUi(self, selectEmergencyService):
        _translate = QtCore.QCoreApplication.translate
        selectEmergencyService.setWindowTitle(_translate("selectEmergencyService", " "))
        self.title.setText(_translate("selectEmergencyService", "<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; font-weight:600; text-decoration: underline;\">Select Emergency Service</span></p></body></html>"))
        self.cityLabel.setText(_translate("selectEmergencyService", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">City : </span></p></body></html>"))
        self.emergencyServiceLabel.setText(_translate("selectEmergencyService", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">E. Service :</span></p></body></html>"))
        self.stateLabel.setText(_translate("selectEmergencyService", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">State : </span></p></body></html>"))
        self.ORLabel.setText(_translate("selectEmergencyService", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">OR</span></p></body></html>"))
        self.searchByID.setPlaceholderText(_translate("selectEmergencyService", "Search by Emergency Service ID"))
        self.removeButton.setText(_translate("selectEmergencyService", "SELECT"))

        self.stateAddFunction(selectEmergencyService)
        self.clickEvents(selectEmergencyService)

    def clickEvents(self, parent):
        self.removeButton.clicked.connect(lambda: self.clickOnRemoveButton(parent))

    def clickOnRemoveButton(self, parent):
        if self.emergencyServiceComboBox.count() == 0 and self.searchByID.text() == "":
            self.dialog = messageBox()
            self.dialog.warningBox("Select the emergencyService or Enter the Id")
            return
        if self.searchByID.text() != "":
            id = self.searchByID.text()
            print(id)
            if id.isdigit():
                import requests
                url = "http://127.0.0.1:8000/api/emergencyservice/" + id
                r = requests.get(url= url)
                l = r.json()
                print(l)
                if l == {'detail': 'Not found.'}:
                    self.dialog = messageBox()
                    self.dialog.warningBox("No Id Match")
                    return
                else:
                    self.window = QDialog()
                    self.dialog = removeEmergencyService()
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
        for i in self.emergencyService_list:
            if i["name"] == self.emergencyServiceComboBox.currentText():
                hdata = i
        parent.close()
        self.window = QDialog()
        self.dialog = removeEmergencyService()
        self.dialog.setup(self.window,hdata)
        self.window.setModal(True)
        self.window.show()

    def stateAddFunction(self,parent):
        for i in states.values():
            self.stateComboBox.addItem(i)
        for i in cities["Andhra Pradesh"]:
            self.cityComboBox.addItem(i)
        self.stateComboBox.currentIndexChanged.connect(lambda : self.cityAddFunction(parent))
        self.stateComboBox.currentIndexChanged.connect(lambda :self.emergencyServiceComboBoxAdd(parent))

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
            self.cityComboBox.currentIndexChanged.connect(lambda :self.emergencyServiceComboBoxAdd(parent))

    def emergencyServiceComboBoxAdd(self,parent):
        if self.last_city == self.cityComboBox.currentText() or self.cityComboBox.count() != len(cities[self.stateComboBox.currentText()]) or self.cityComboBox.itemText(self.cityComboBox.count()-1) != cities[self.stateComboBox.currentText()][-1]:
            return
        self.last_city = self.cityComboBox.currentText()
        # First Erase all emergencyServices
        i = self.emergencyServiceComboBox.count()
        while i > 0:
            i -= 1
            self.emergencyServiceComboBox.removeItem(0)

        import requests
        print(self.cityComboBox.currentText())
        URL = "http://127.0.0.1:8000/api/emergencyservice/"
        param ={
            "city": self.cityComboBox.currentText()
        }
        r = requests.get(url=URL,params=param)
        l = r.json()
        print(l)
        self.emergencyService_list = l
        for i in l:
            self.emergencyServiceComboBox.addItem(str(i["name"]))
