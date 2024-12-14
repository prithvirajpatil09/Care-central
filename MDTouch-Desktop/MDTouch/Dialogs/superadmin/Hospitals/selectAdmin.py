from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Dialogs.superadmin.Hospitals.deleteAdmin import *
from Data.States import *
from Dialogs.messageBox import *

class selectAdmin(object):
    def __init__(self):
        self.last_city = ''
        self.hospital_list = []
        self.admin_list = []
        self.last_hospital = ''
    def setup(self, selectAdmin):
        selectAdmin.setObjectName("selectAdmin")
        selectAdmin.resize(333, 408)
        selectAdmin.setWindowTitle("")
        self.title = QtWidgets.QLabel(selectAdmin)
        self.title.setGeometry(QtCore.QRect(40, 0, 261, 51))
        self.title.setObjectName("title")
        self.frame = QtWidgets.QFrame(selectAdmin)
        self.frame.setGeometry(QtCore.QRect(10, 60, 311, 291))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.cityComboBox = QtWidgets.QComboBox(self.frame)
        self.cityComboBox.setGeometry(QtCore.QRect(120, 140, 161, 27))
        self.cityComboBox.setObjectName("cityComboBox")
        self.hospitalComboBox = QtWidgets.QComboBox(self.frame)
        self.hospitalComboBox.setGeometry(QtCore.QRect(120, 190, 161, 27))
        self.hospitalComboBox.setObjectName("hospitalComboBox")
        self.stateComboBox = QtWidgets.QComboBox(self.frame)
        self.stateComboBox.setGeometry(QtCore.QRect(120, 90, 161, 27))
        self.stateComboBox.setObjectName("stateComboBox")
        self.cityLabel = QtWidgets.QLabel(self.frame)
        self.cityLabel.setGeometry(QtCore.QRect(30, 140, 111, 31))
        self.cityLabel.setObjectName("cityLabel")
        self.hospitalLabel = QtWidgets.QLabel(self.frame)
        self.hospitalLabel.setGeometry(QtCore.QRect(30, 190, 111, 31))
        self.hospitalLabel.setObjectName("hospitalLabel")
        self.stateLabel = QtWidgets.QLabel(self.frame)
        self.stateLabel.setGeometry(QtCore.QRect(30, 90, 111, 31))
        self.stateLabel.setObjectName("stateLabel")
        self.adminLabel = QtWidgets.QLabel(self.frame)
        self.adminLabel.setGeometry(QtCore.QRect(30, 240, 111, 31))
        self.adminLabel.setObjectName("adminLabel")
        self.adminComboBox = QtWidgets.QComboBox(self.frame)
        self.adminComboBox.setGeometry(QtCore.QRect(120, 240, 161, 27))
        self.adminComboBox.setObjectName("adminComboBox")
        self.ORLabel = QtWidgets.QLabel(self.frame)
        self.ORLabel.setGeometry(QtCore.QRect(110, 50, 111, 31))
        self.ORLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ORLabel.setObjectName("ORLabel")
        self.searchByID = QtWidgets.QLineEdit(self.frame)
        self.searchByID.setGeometry(QtCore.QRect(20, 20, 261, 27))
        self.searchByID.setObjectName("searchByID")
        self.deleteButton = QtWidgets.QPushButton(selectAdmin)
        self.deleteButton.setGeometry(QtCore.QRect(140, 360, 80, 28))
        self.deleteButton.setObjectName("deleteButton")

        self.retranslateUi(selectAdmin)
        QtCore.QMetaObject.connectSlotsByName(selectAdmin)

    def retranslateUi(self, selectAdmin):
        _translate = QtCore.QCoreApplication.translate
        selectAdmin.setWindowTitle(_translate("selectAdmin", " "))
        self.title.setText(_translate("selectAdmin", "<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; font-weight:600; text-decoration: underline;\">Select Admin</span></p></body></html>"))
        self.cityLabel.setText(_translate("selectAdmin", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">City : </span></p></body></html>"))
        self.hospitalLabel.setText(_translate("selectAdmin", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Hospital : </span></p></body></html>"))
        self.stateLabel.setText(_translate("selectAdmin", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">State : </span></p></body></html>"))
        self.adminLabel.setText(_translate("selectAdmin", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Admin :</span></p></body></html>"))
        self.ORLabel.setText(_translate("selectAdmin", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">OR</span></p></body></html>"))
        self.searchByID.setPlaceholderText(_translate("selectAdmin", "Search by Admin Id"))
        self.deleteButton.setText(_translate("selectAdmin", "SELECT"))

        self.stateAddFunction(selectAdmin)
        self.clickEvents(selectAdmin)

    def clickEvents(self, parent):
        self.deleteButton.clicked.connect(lambda : self.clickOnDeleteAdmin(parent))

    def clickOnDeleteAdmin(self, parent):
        id = self.searchByID.text()
        if id != "":
            if id.isdigit():
                import requests
                URL = "http://127.0.0.1:8000/api/administrator/" + str(id)
                r = requests.get(url= URL)
                data = r.json()
                if data == {"detail": "Not found."}:
                    self.window = messageBox()
                    self.window.infoBox("Id Does Not Exists")
                    self.searchByID.setText("")
                    return
                else:
                    URL = "http://127.0.0.1:8000/api/hospital/" + str(data["workplace"])
                    r = requests.get(url=URL)
                    hdata = r.json()
                    parent.close()
                    self.window = QDialog()
                    self.dialog = deleteAdmin()
                    self.dialog.setup(self.window,data,hdata)
                    self.window.setModal(True)
                    self.window.show()
                    return

            else:
                self.window = messageBox()
                self.window.infoBox("Id is a Integer")
                self.searchByID.setText("")
            return

        if self.adminComboBox.count() == 0:
            self.window = messageBox()
            self.window.infoBox("Select the hospital first")
            return
        admin_name = self.adminComboBox.currentText()
        adminData = {}
        hdata = {}
        for i in self.admin_list:
            if admin_name == i["firstName"] + " " + i["lastName"]:
                adminData = i
                break
        for i in self.hospital_list:
            if i["name"] == self.hospitalComboBox.currentText():
                hdata = i
                break
        parent.close()
        self.window = QDialog()
        self.dialog = deleteAdmin()
        self.dialog.setup(self.window,adminData,hdata)
        self.window.setModal(True)
        self.window.show()


    def stateAddFunction(self,parent):
        for i in states.values():
            self.stateComboBox.addItem(i)
        for i in cities["Andhra Pradesh"]:
            self.cityComboBox.addItem(i)
        self.stateComboBox.currentIndexChanged.connect(lambda : self.cityAddFunction(parent))
        self.stateComboBox.currentIndexChanged.connect(lambda :self.hospitalComboBoxAdd(parent))
        #self.stateComboBox.currentIndexChanged.connect(lambda : self.adminComboBoxAdd(parent))

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
        self.hospitalComboBox.currentIndexChanged.connect(lambda : self.adminComboBoxAdd(parent))

    def adminComboBoxAdd(self,parent):
        i = self.adminComboBox.count()
        while i > 0:
            i -= 1
            self.adminComboBox.removeItem(0)
        workplace_id = 0
        print(self.hospital_list)
        for i in self.hospital_list:
            if i["name"] == self.hospitalComboBox.currentText():
                workplace_id = i["id"]
                break
        if workplace_id == 0:
            return

        print(workplace_id)
        import requests
        URL = "http://127.0.0.1:8000/api/administrator/"
        param = {
            "workplace" : int(workplace_id)
        }
        r = requests.get(url=URL,params=param)
        self.admin_list = r.json()
        print(self.admin_list)
        for i in self.admin_list:
            self.adminComboBox.addItem(str(i["firstName"]) + " " + i["lastName"])
