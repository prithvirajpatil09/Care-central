from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Data.States import *
from Dialogs.superadmin.Events.deleteEvent import *
from Dialogs.messageBox import *

class selectEvent(object):
    def setup(self, selectEvent,type= None,userdata = None):
        self.type = type
        self.userdata = userdata
        selectEvent.setObjectName("selectEvent")
        selectEvent.resize(323, 315)
        self.frame = QtWidgets.QFrame(selectEvent)
        self.frame.setGeometry(QtCore.QRect(10, 60, 301, 211))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.searchByID = QtWidgets.QLineEdit(self.frame)
        self.searchByID.setGeometry(QtCore.QRect(20, 10, 251, 27))
        self.searchByID.setObjectName("searchByID")
        self.title = QtWidgets.QLabel(selectEvent)
        self.title.setGeometry(QtCore.QRect(10, 0, 291, 51))
        self.title.setObjectName("title")
        self.removeButton = QtWidgets.QPushButton(selectEvent)
        self.removeButton.setGeometry(QtCore.QRect(120, 280, 80, 28))
        self.removeButton.setObjectName("removeButton")

        self.retranslateUi(selectEvent)
        QtCore.QMetaObject.connectSlotsByName(selectEvent)

    def retranslateUi(self, selectEvent):
        _translate = QtCore.QCoreApplication.translate
        selectEvent.setWindowTitle(_translate("selectEvent", " "))
        self.searchByID.setPlaceholderText(_translate("selectEvent", "Search by Event ID"))
        self.title.setText(_translate("selectEvent", "<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; font-weight:600; text-decoration: underline;\">Select Event</span></p></body></html>"))
        self.removeButton.setText(_translate("selectEvent", "SELECT"))

        self.clickEvents(selectEvent)

    def clickEvents(self, parent):
        self.removeButton.clicked.connect(lambda: self.clickOnRemoveButton(parent))

    def clickOnRemoveButton(self, parent):
        id = self.searchByID.text()
        if self.searchByID.text() == "" or (not(self.searchByID.text().isdigit())):
            self.dialog = messageBox()
            self.dialog.warningBox("Enter Valid ID")
            return
        import requests
        URL = "http://127.0.0.1:8000/api/event/" + id
        r = requests.get(url=URL)
        l = r.json()
        print(l)
        if l == {'detail' : 'Not found.'}:
            self.window = messageBox()
            self.window.warningBox("Id Does not Exists")
            return
        if self.type == 'H':
            if l["hospitalid"] != self.userdata["id"]:
                self.dialog = messageBox()
                self.dialog.warningBox("Enter Valid ID")
                return
        elif self.type == "BB":
            if l["bloodbankid"] != self.userdata["id"]:
                self.dialog = messageBox()
                self.dialog.warningBox("Enter Valid ID")
                return
        elif self.type == "DS":
            if l["dispensaryid"] != self.userdata["id"]:
                self.dialog = messageBox()
                self.dialog.warningBox("Enter Valid ID")
                return
        elif self.type == "T":
            if l["testcenterid"] != self.userdata["id"]:
                self.dialog = messageBox()
                self.dialog.warningBox("Enter Valid ID")
                return

        parent.close()
        self.window = QDialog()
        self.dialog = deleteEvent()
        self.dialog.setup(self.window,l)
        self.window.setModal(True)
        self.window.show()
