from PyQt5 import QtCore, QtGui, QtWidgets
from Dialogs.messageBox import *
from Dialogs.bloodBank.bloodwasteProfile import *
from PyQt5.QtWidgets import *

class bloodwasteEntry(object):
    def setup(self, bloodwasteEntry,grandparent,bloodbankHome):
        bloodwasteEntry.setObjectName("bloodwasteEntry")
        bloodwasteEntry.setWindowModality(QtCore.Qt.ApplicationModal)
        bloodwasteEntry.resize(342, 402)
        self.frame = QtWidgets.QFrame(bloodwasteEntry)
        self.frame.setGeometry(QtCore.QRect(10, 10, 321, 351))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.bloodBillingLabel = QtWidgets.QLabel(self.frame)
        self.bloodBillingLabel.setGeometry(QtCore.QRect(20, 0, 291, 61))
        self.bloodBillingLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.bloodBillingLabel.setObjectName("bloodBillingLabel")
        self.bloodTypeLabel = QtWidgets.QLabel(self.frame)
        self.bloodTypeLabel.setGeometry(QtCore.QRect(20, 70, 151, 41))
        self.bloodTypeLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.bloodTypeLabel.setObjectName("bloodTypeLabel")
        self.quantityLabel = QtWidgets.QLabel(self.frame)
        self.quantityLabel.setGeometry(QtCore.QRect(20, 120, 151, 41))
        self.quantityLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.quantityLabel.setObjectName("quantityLabel")
        self.quantity = QtWidgets.QLineEdit(self.frame)
        self.quantity.setGeometry(QtCore.QRect(180, 130, 101, 25))
        self.quantity.setObjectName("quantity")
        self.bloodTypeComboBox = QtWidgets.QComboBox(self.frame)
        self.bloodTypeComboBox.setGeometry(QtCore.QRect(180, 80, 101, 25))
        self.bloodTypeComboBox.setObjectName("bloodTypeComboBox")
        self.bloodTypeComboBox.addItem("")
        self.bloodTypeComboBox.addItem("")
        self.bloodTypeComboBox.addItem("")
        self.bloodTypeComboBox.addItem("")
        self.bloodTypeComboBox.addItem("")
        self.bloodTypeComboBox.addItem("")
        self.bloodTypeComboBox.addItem("")
        self.bloodTypeComboBox.addItem("")
        self.reason = QtWidgets.QTextEdit(self.frame)
        self.reason.setGeometry(QtCore.QRect(20, 190, 301, 151))
        self.reason.setObjectName("reason")
        self.reasonLabel = QtWidgets.QLabel(self.frame)
        self.reasonLabel.setGeometry(QtCore.QRect(20, 160, 151, 41))
        self.reasonLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.reasonLabel.setObjectName("reasonLabel")
        self.addButton = QtWidgets.QPushButton(bloodwasteEntry)
        self.addButton.setGeometry(QtCore.QRect(120, 370, 89, 25))
        self.addButton.setObjectName("addButton")

        self.retranslateUi(bloodwasteEntry,grandparent,bloodbankHome)
        QtCore.QMetaObject.connectSlotsByName(bloodwasteEntry)

    def retranslateUi(self, bloodwasteEntry,grandparent,bloodbankHome):
        _translate = QtCore.QCoreApplication.translate
        bloodwasteEntry.setWindowTitle(_translate("bloodwasteEntry", "Blood Entry"))
        self.bloodBillingLabel.setText(_translate("bloodwasteEntry", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; text-decoration: underline;\">Blood Waste </span></p><p align=\"center\"><span style=\" font-size:12pt; text-decoration: underline;\">Entry</span></p></body></html>"))
        self.bloodTypeLabel.setText(_translate("bloodwasteEntry", "<html><head/><body><p>Blood Type :</p></body></html>"))
        self.quantityLabel.setText(_translate("bloodwasteEntry", "<html><head/><body><p>Quantity :</p></body></html>"))
        self.bloodTypeComboBox.setItemText(0, _translate("bloodwasteEntry", "A+"))
        self.bloodTypeComboBox.setItemText(1, _translate("bloodwasteEntry", "A-"))
        self.bloodTypeComboBox.setItemText(2, _translate("bloodwasteEntry", "B+"))
        self.bloodTypeComboBox.setItemText(3, _translate("bloodwasteEntry", "B-"))
        self.bloodTypeComboBox.setItemText(4, _translate("bloodwasteEntry", "AB+"))
        self.bloodTypeComboBox.setItemText(5, _translate("bloodwasteEntry", "AB_"))
        self.bloodTypeComboBox.setItemText(6, _translate("bloodwasteEntry", "O+"))
        self.bloodTypeComboBox.setItemText(7, _translate("bloodwasteEntry", "O-"))
        self.reasonLabel.setText(_translate("bloodwasteEntry", "<html><head/><body><p>Reason : </p></body></html>"))
        self.addButton.setText(_translate("bloodwasteEntry", "Add"))
        self.events(bloodwasteEntry,grandparent,bloodbankHome)

    def events(self,parent,grandparent,bloodbankHome):
        self.addButton.clicked.connect(lambda : self.clickOnAddButton(parent,grandparent,bloodbankHome))

    def clickOnAddButton(self,parent,grandparent,bloodbankHome):
        bbid = grandparent.bloodbankdata["id"]
        quantity = self.quantity.text()
        reason = self.reason.toPlainText()
        if not(quantity.isdigit()) or len(reason) < 11 :
            self.window = messageBox()
            self.window.infoBox("Invalid data")
            return
        import requests
        bloodtype = self.bloodTypeComboBox.currentText()
        if bloodtype == 'A+':
            if int(grandparent.bloodbankdata["quantityAp"]) < int(quantity):
                self.window = messageBox()
                self.window.infoBox("Does Not have blood of this type")
                return
            else:
                left = grandparent.bloodbankdata["quantityAp"] - int(quantity)
                grandparent.bloodbankdata["quantityAp"] = left
                data = {
                    "quantityAp" : int(left)
                }
                URL = "http://127.0.0.1:8000/MDTouch/api/bloodbankcenter/" + str(grandparent.bloodbankdata["id"])
                r = requests.put(url=URL,data = data)
        elif bloodtype == 'A-':
            if int(grandparent.bloodbankdata["quantityAm"]) < int(quantity):
                self.window = messageBox()
                self.window.infoBox("Does Not have blood of this type")
                return
            else:
                left = grandparent.bloodbankdata["quantityAm"] - int(quantity)
                grandparent.bloodbankdata["quantityAm"] = left
                data = {
                    "quantityAm" : int(left)
                }
                URL = "http://127.0.0.1:8000/MDTouch/api/bloodbankcenter/" + str(grandparent.bloodbankdata["id"])
                r = requests.put(url=URL,data = data)
        elif bloodtype == 'B+':
            if int(grandparent.bloodbankdata["quantityBp"]) < int(quantity):
                self.window = messageBox()
                self.window.infoBox("Does Not have blood of this type")
                return
            else:
                left = grandparent.bloodbankdata["quantityBp"] - int(quantity)
                grandparent.bloodbankdata["quantityBp"] = left
                data = {
                    "quantityBp" : int(left)
                }
                URL = "http://127.0.0.1:8000/MDTouch/api/bloodbankcenter/" + str(grandparent.bloodbankdata["id"])
                r = requests.put(url=URL,data = data)
        elif bloodtype == 'B-':
            if int(grandparent.bloodbankdata["quantityBm"]) < int(quantity):
                self.window = messageBox()
                self.window.infoBox("Does Not have blood of this type")
                return
            else:
                left = grandparent.bloodbankdata["quantityBm"] - int(quantity)
                grandparent.bloodbankdata["quantityBm"] = left
                data = {
                    "quantityBm" : int(left)
                }
                URL = "http://127.0.0.1:8000/MDTouch/api/bloodbankcenter/" + str(grandparent.bloodbankdata["id"])
                r = requests.put(url=URL,data = data)
        elif bloodtype == 'AB+':
            if int(grandparent.bloodbankdata["quantityABp"]) < int(quantity):
                self.window = messageBox()
                self.window.infoBox("Does Not have blood of this type")
                return
            else:
                left = grandparent.bloodbankdata["quantityABp"] - int(quantity)
                grandparent.bloodbankdata["quantityABp"] = left
                data = {
                    "quantityABp" : int(left)
                }
                URL = "http://127.0.0.1:8000/MDTouch/api/bloodbankcenter/" + str(grandparent.bloodbankdata["id"])
                r = requests.put(url=URL,data = data)
        elif bloodtype == 'AB-':
            if int(grandparent.bloodbankdata["quantityABm"]) < int(quantity):
                self.window = messageBox()
                self.window.infoBox("Does Not have blood of this type")
                return
            else:
                left = grandparent.bloodbankdata["quantityABm"] - int(quantity)
                grandparent.bloodbankdata["quantityABm"] = left
                data = {
                    "quantityABm" : int(left)
                }
                URL = "http://127.0.0.1:8000/MDTouch/api/bloodbankcenter/" + str(grandparent.bloodbankdata["id"])
                r = requests.put(url=URL,data = data)
        elif bloodtype == 'O+':
            if int(grandparent.bloodbankdata["quantityOp"]) < int(quantity):
                self.window = messageBox()
                self.window.infoBox("Does Not have blood of this type")
                return
            else:
                left = grandparent.bloodbankdata["quantityOp"] - int(quantity)
                grandparent.bloodbankdata["quantityOp"] = left
                data = {
                    "quantityOp" : int(left)
                }
                URL = "http://127.0.0.1:8000/MDTouch/api/bloodbankcenter/" + str(grandparent.bloodbankdata["id"])
                r = requests.put(url=URL,data = data)
        else:
            if int(grandparent.bloodbankdata["quantityOm"]) < int(quantity):
                self.window = messageBox()
                self.window.infoBox("Does Not have blood of this type")
                return
            else:
                left = grandparent.bloodbankdata["quantityOm"] - int(quantity)
                grandparent.bloodbankdata["quantityOm"] = left
                data = {
                    "quantityOm" : int(left)
                }
                URL = "http://127.0.0.1:8000/MDTouch/api/bloodbankcenter/" + str(grandparent.bloodbankdata["id"])
                r = requests.put(url=URL,data = data)

        import datetime
        data = {
            "date" : datetime.date.today(),
            "quantity": int(quantity),
            "bloodgrp": self.bloodTypeComboBox.currentText(),
            "reason": reason,
            "bbcid": int(bbid)
        }
        URL = "http://127.0.0.1:8000/MDTouch/api/bloodwaste/"
        r = requests.post(url=URL,data=data)
        l = r.json()
        parent.close()
        self.window = QDialog()
        self.dialog = bloodwasteReciept()
        self.dialog.setup(self.window,l)
        self.window.setModal(True)
        self.window.show()
        grandparent.setup(bloodbankHome,grandparent.logindata)




