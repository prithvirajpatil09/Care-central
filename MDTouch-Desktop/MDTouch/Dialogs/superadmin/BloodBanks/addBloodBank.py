from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Data.States import *
from Dialogs.superadmin.BloodBanks.bloodBankProfile import *
from Dialogs.messageBox import *
from Dialogs.superadmin.BloodBanks.selectBloodBank import *
from Dialogs.accountCreated import *
class addBloodBank(object):
    def setup(self, addBloodBank):
        addBloodBank.setObjectName("addBloodBank")
        addBloodBank.resize(750, 480)
        addBloodBank.setMinimumSize(QtCore.QSize(750, 480))
        addBloodBank.setMaximumSize(QtCore.QSize(750, 480))
        self.title = QtWidgets.QLabel(addBloodBank)
        self.title.setGeometry(QtCore.QRect(260, 0, 261, 51))
        self.title.setObjectName("title")
        self.frame = QtWidgets.QFrame(addBloodBank)
        self.frame.setGeometry(QtCore.QRect(10, 60, 730, 340))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.nameLabel = QtWidgets.QLabel(self.frame)
        self.nameLabel.setGeometry(QtCore.QRect(25, 20, 71, 41))
        self.nameLabel.setObjectName("nameLabel")
        self.name = QtWidgets.QLineEdit(self.frame)
        self.name.setGeometry(QtCore.QRect(150, 20, 561, 41))
        self.name.setObjectName("name")
        self.addressLabel = QtWidgets.QLabel(self.frame)
        self.addressLabel.setGeometry(QtCore.QRect(25, 70, 91, 41))
        self.addressLabel.setObjectName("addressLabel")
        self.contactLabel = QtWidgets.QLabel(self.frame)
        self.contactLabel.setGeometry(QtCore.QRect(25, 280, 131, 41))
        self.contactLabel.setObjectName("contactLabel")
        self.stateLabel = QtWidgets.QLabel(self.frame)
        self.stateLabel.setGeometry(QtCore.QRect(25, 190, 61, 41))
        self.stateLabel.setObjectName("stateLabel")
        self.pinCodeLabel = QtWidgets.QLabel(self.frame)
        self.pinCodeLabel.setGeometry(QtCore.QRect(25, 150, 91, 41))
        self.pinCodeLabel.setObjectName("pinCodeLabel")
        self.cityLabel = QtWidgets.QLabel(self.frame)
        self.cityLabel.setGeometry(QtCore.QRect(25, 240, 61, 41))
        self.cityLabel.setObjectName("cityLabel")
        self.address = QtWidgets.QTextEdit(self.frame)
        self.address.setGeometry(QtCore.QRect(150, 70, 561, 75))
        self.address.setObjectName("address")
        self.pinCode = QtWidgets.QLineEdit(self.frame)
        self.pinCode.setGeometry(QtCore.QRect(150, 160, 181, 27))
        self.pinCode.setObjectName("pinCode")
        self.contact = QtWidgets.QLineEdit(self.frame)
        self.contact.setGeometry(QtCore.QRect(150, 290, 181, 27))
        self.contact.setInputMethodHints(QtCore.Qt.ImhNone)
        self.contact.setObjectName("contact")
        self.state = QtWidgets.QComboBox(self.frame)
        self.state.setGeometry(QtCore.QRect(150, 200, 181, 27))
        self.state.setObjectName("state")
        self.city = QtWidgets.QComboBox(self.frame)
        self.city.setGeometry(QtCore.QRect(150, 250, 181, 27))
        self.city.setObjectName("city")
        self.addButton = QtWidgets.QPushButton(addBloodBank)
        self.addButton.setGeometry(QtCore.QRect(330, 420, 131, 41))
        self.addButton.setObjectName("addButton")

        self.retranslateUi(addBloodBank)
        QtCore.QMetaObject.connectSlotsByName(addBloodBank)

    def retranslateUi(self, addBloodBank):
        _translate = QtCore.QCoreApplication.translate
        addBloodBank.setWindowTitle(_translate("addBloodBank", " "))
        self.title.setText(_translate("addBloodBank", "<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; font-weight:600; text-decoration: underline;\">Add Blood Bank</span></p></body></html>"))
        self.nameLabel.setText(_translate("addBloodBank", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Name :</span></p></body></html>"))
        self.addressLabel.setText(_translate("addBloodBank", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Address :</span></p></body></html>"))
        self.contactLabel.setText(_translate("addBloodBank", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Contact No. :</span></p></body></html>"))
        self.stateLabel.setText(_translate("addBloodBank", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">State :</span></p></body></html>"))
        self.pinCodeLabel.setText(_translate("addBloodBank", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Pin Code :</span></p></body></html>"))
        self.cityLabel.setText(_translate("addBloodBank", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">City :</span></p></body></html>"))
        self.addButton.setText(_translate("addBloodBank", "ADD"))

        self.stateAddFunction(addBloodBank)
        self.clickEvents(addBloodBank)

    def clickEvents(self,parent):
        self.addButton.clicked.connect(lambda : self.addBloodBankCenterFunction(parent))

    def addBloodBankCenterFunction(self,parent):
        name  = self.name.text()
        address = self.address.toPlainText()
        city = self.city.currentText()
        state = self.state.currentText()
        pin = self.pinCode.text()
        contact = self.contact.text()

        import requests
        from random import randint
        username = name.replace(" ","") +  str(randint(0,100))
        URL = "http://127.0.0.1:8000/api/login/"
        params = {
            "username" : username
        }
        while True:
            params = {
                "username" : username
            }
            r = requests.get(url=URL,params=params)
            if len(r.json()) > 0:
                username = name.replace(" ","") +  str(randint(0,100))
            else:
                break
        URL = "http://127.0.0.1:8000/api/login/"
        data = {
            "username": username,
            "password": "12345",
            "dept": "BB",
            "email": username+"@email.com"
        }
        r = requests.post(url=URL,data=data)
        loginData = r.json()
        print(loginData)
        id = loginData["id"]


        data1 = {
            "name": name,
            "address": address,
            "city": city,
            "pin": pin,
            "state": state,
            "contact": contact,
            "email": username+"@email.com",
            "username": id
        }

        URL1 = "http://127.0.0.1:8000/api/bloodbankcenter/"
        r = requests.post(url=URL1,data=data1)
        l = r.json()
        print(l)
        parent.close()
        self.window = QDialog()
        self.dialog = accountCreated()
        self.dialog.setup(self.window,"BloodBank",l,loginData)
        self.window.setModal(True)
        self.window.show()


    def stateAddFunction(self,parent):
        for i in states.values():
            self.state.addItem(i)
        for i in cities["Andhra Pradesh"]:
            self.city.addItem(i)
        self.state.currentIndexChanged.connect(lambda : self.cityAddFunction(parent))

    def cityAddFunction(self,parent):
        state = self.state.currentText()

        while self.city.count() > 0:
            self.city.removeItem(0)

        for i in cities[state]:
            self.city.addItem(i)


