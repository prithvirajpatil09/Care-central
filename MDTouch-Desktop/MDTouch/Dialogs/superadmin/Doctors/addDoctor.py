from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Data.States import *
from Dialogs.superadmin.Doctors.doctorProfile import *
from Dialogs.accountCreated import *

class addDoctor(object):
    def __init__(self):
        self.last_city = ''
        self.hospital_list = []

    def setup(self, addDoctor):
        addDoctor.setObjectName("addDoctor")
        addDoctor.resize(750, 481)
        addDoctor.setWindowTitle("")
        self.title = QtWidgets.QLabel(addDoctor)
        self.title.setGeometry(QtCore.QRect(250, 0, 261, 51))
        self.title.setObjectName("title")
        self.addButton = QtWidgets.QPushButton(addDoctor)
        self.addButton.setGeometry(QtCore.QRect(300, 420, 131, 41))
        self.addButton.setObjectName("addButton")
        self.frame = QtWidgets.QFrame(addDoctor)
        self.frame.setGeometry(QtCore.QRect(10, 60, 731, 341))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.firstNameLabel = QtWidgets.QLabel(self.frame)
        self.firstNameLabel.setGeometry(QtCore.QRect(10, 20, 121, 41))
        self.firstNameLabel.setObjectName("firstNameLabel")
        self.firstName = QtWidgets.QLineEdit(self.frame)
        self.firstName.setGeometry(QtCore.QRect(120, 20, 211, 41))
        self.firstName.setObjectName("firstName")
        self.uploadImage = QtWidgets.QPushButton(self.frame)
        self.uploadImage.setGeometry(QtCore.QRect(90, 280, 131, 41))
        self.uploadImage.setObjectName("uploadImage")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(50, 70, 221, 201))
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet("image: url(:/doctor_icon.png);\n"
"border-style:solid;\n"
"border-width:1px;\n"
"border-color: rgb(0, 0, 0);")
        self.widget.setObjectName("widget")
        self.lastNameLabel = QtWidgets.QLabel(self.frame)
        self.lastNameLabel.setGeometry(QtCore.QRect(350, 20, 111, 41))
        self.lastNameLabel.setObjectName("lastNameLabel")
        self.lastName = QtWidgets.QLineEdit(self.frame)
        self.lastName.setGeometry(QtCore.QRect(460, 20, 211, 41))
        self.lastName.setObjectName("lastName")
        self.stateLabel = QtWidgets.QLabel(self.frame)
        self.stateLabel.setGeometry(QtCore.QRect(350, 90, 111, 31))
        self.stateLabel.setObjectName("stateLabel")
        self.cityLabel = QtWidgets.QLabel(self.frame)
        self.cityLabel.setGeometry(QtCore.QRect(350, 160, 111, 31))
        self.cityLabel.setObjectName("cityLabel")
        self.hospitalLabel = QtWidgets.QLabel(self.frame)
        self.hospitalLabel.setGeometry(QtCore.QRect(350, 240, 111, 31))
        self.hospitalLabel.setObjectName("hospitalLabel")
        self.stateComboBox = QtWidgets.QComboBox(self.frame)
        self.stateComboBox.setGeometry(QtCore.QRect(460, 90, 161, 27))
        self.stateComboBox.setObjectName("stateComboBox")
        self.cityComboBox = QtWidgets.QComboBox(self.frame)
        self.cityComboBox.setGeometry(QtCore.QRect(460, 160, 161, 27))
        self.cityComboBox.setObjectName("cityComboBox")
        self.hospitalComboBox = QtWidgets.QComboBox(self.frame)
        self.hospitalComboBox.setGeometry(QtCore.QRect(460, 240, 161, 27))
        self.hospitalComboBox.setObjectName("hospitalComboBox")

        self.retranslateUi(addDoctor)
        QtCore.QMetaObject.connectSlotsByName(addDoctor)

    def retranslateUi(self, addDoctor):
        _translate = QtCore.QCoreApplication.translate
        self.title.setText(_translate("addDoctor", "<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; font-weight:600; text-decoration: underline;\">Add Doctor</span></p></body></html>"))
        self.addButton.setText(_translate("addDoctor", "ADD"))
        self.firstNameLabel.setText(_translate("addDoctor", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">First Name : </span></p></body></html>"))
        self.uploadImage.setText(_translate("addDoctor", "Upload Image"))
        self.lastNameLabel.setText(_translate("addDoctor", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Last Name : </span></p></body></html>"))
        self.stateLabel.setText(_translate("addDoctor", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">State : </span></p></body></html>"))
        self.cityLabel.setText(_translate("addDoctor", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">City : </span></p></body></html>"))
        self.hospitalLabel.setText(_translate("addDoctor", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Hospital : </span></p></body></html>"))

        self.clickEvents(addDoctor)

    def clickEvents(self, parent):
        self.stateAddFunction(parent)
        self.addButton.clicked.connect(lambda : self.addDoctorFunction(parent))

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


    def addDoctorFunction(self,parent):
        fname = self.firstName.text()
        lname = self.lastName.text()
        state = self.stateComboBox.currentText()
        city = self.cityComboBox.currentText()
        hospital = self.hospitalComboBox.currentText()
        import requests
        from random import randint
        username = fname.replace(" ","") +  str(randint(0,100))
        '''
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
        '''
        hdata = {}
        for i in self.hospital_list:
            if i["name"] == hospital and i["city"] == city and state ==i["state"]:
                hdata = i
                break
        '''
        URLH = "http://127.0.0.1:8000/api/hospital/"
        r = requests.get(url=URLH,params={
            "name" : hospital,
            "city" : city,
            "state" : state
        })
        '''
        hospital_id = hdata["id"]
        URL = "http://127.0.0.1:8000/api/login/"
        data = {
            "username":username,
            "password": "12345",
            "dept": "H",
            "email": username + "@email.com"
        }
        r = requests.post(url=URL,data=data)
        loginData = r.json()
        print(loginData)
        id = loginData["id"]
        sdata = {
            "skill" : "Brain"
        }
        qdata = {
            "degree" : "MBBS"
        }
        r = requests.post(url="http://127.0.0.1:8000/api/qualification/",data=qdata)
        qualification = r.json()
        print(qualification)
        r =requests.post(url="http://127.0.0.1:8000/api/specialization/",data=sdata)
        specialization = r.json()
        print(specialization)
        URLD = "http://127.0.0.1:8000/api/doctor/"
        data1 = {
            "firstName":fname,
            "lastName": lname,
            "username": id,
            "workplace": hospital_id,
            "qualification": int(qualification["id"]),
            "specialization" : int(specialization["id"])
        }
        r = requests.post(url=URLD,data=data1)
        l = r.json()

        parent.close()
        self.window = QDialog()
        self.dialog = accountCreated()
        self.dialog.setup(self.window,"Doctor",l,loginData,hdata)
        self.window.setModal(True)
        self.window.show()

