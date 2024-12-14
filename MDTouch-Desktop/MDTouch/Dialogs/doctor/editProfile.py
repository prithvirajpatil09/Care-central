from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Dialogs.messageBox import *
from Dialogs.doctor.addQualification import *
from Dialogs.doctor.addSpecialization import *

class editProfile(object):
    def setup(self, editProfile,doctordata,hospitaldata,grandparent):
        self.doctordata = doctordata
        self.hospitaldata = hospitaldata
        editProfile.setObjectName("editProfile")
        editProfile.resize(792, 467)
        editProfile.setStyleSheet("")
        self.exitButton = QtWidgets.QPushButton(editProfile)
        self.exitButton.setGeometry(QtCore.QRect(670, 420, 80, 28))
        self.exitButton.setStyleSheet("")
        self.exitButton.setObjectName("exitButton")
        self.saveButton = QtWidgets.QPushButton(editProfile)
        self.saveButton.setGeometry(QtCore.QRect(560, 420, 80, 28))
        self.saveButton.setStyleSheet("")
        self.saveButton.setObjectName("saveButton")
        self.frame = QtWidgets.QFrame(editProfile)
        self.frame.setGeometry(QtCore.QRect(20, 60, 751, 341))
        self.frame.setStyleSheet("background:white;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(30, 70, 221, 201))
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet("image: url(:../MDTouch/doctor_icon.png);\n"
"border-style:solid;\n"
"border-width:1px;\n"
"border-color: rgb(0, 0, 0);")
        self.widget.setObjectName("widget")
        self.doctorIDLabel = QtWidgets.QLabel(self.frame)
        self.doctorIDLabel.setGeometry(QtCore.QRect(30, 10, 101, 41))
        self.doctorIDLabel.setObjectName("doctorIDLabel")
        self.doctorID = QtWidgets.QLabel(self.frame)
        self.doctorID.setGeometry(QtCore.QRect(140, 10, 211, 41))
        self.doctorID.setStyleSheet("font-size:12pt;\n"
"font-weight:bold;")
        self.doctorID.setObjectName("doctorID")
        self.uploadImage = QtWidgets.QPushButton(self.frame)
        self.uploadImage.setGeometry(QtCore.QRect(80, 290, 111, 28))
        self.uploadImage.setObjectName("uploadImage")
        self.tabWidget = QtWidgets.QTabWidget(self.frame)
        self.tabWidget.setGeometry(QtCore.QRect(270, 20, 451, 301))
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.personal = QtWidgets.QWidget()
        self.personal.setObjectName("personal")
        self.address = QtWidgets.QTextBrowser(self.personal)
        self.address.setGeometry(QtCore.QRect(140, 20, 291, 101))
        self.address.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard | QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextBrowserInteraction | QtCore.Qt.TextEditable | QtCore.Qt.TextSelectableByMouse)
        self.address.setStyleSheet("")
        self.address.setObjectName("address")
        self.addressLabel = QtWidgets.QLabel(self.personal)
        self.addressLabel.setGeometry(QtCore.QRect(30, 60, 111, 31))
        self.addressLabel.setObjectName("addressLabel")
        self.city = QtWidgets.QLabel(self.personal)
        self.city.setGeometry(QtCore.QRect(140, 150, 181, 31))
        self.city.setStyleSheet("font-size:12pt;")
        self.city.setObjectName("city")
        self.stateLabel = QtWidgets.QLabel(self.personal)
        self.stateLabel.setGeometry(QtCore.QRect(30, 200, 111, 31))
        self.stateLabel.setObjectName("stateLabel")
        self.state = QtWidgets.QLabel(self.personal)
        self.state.setGeometry(QtCore.QRect(140, 200, 181, 31))
        self.state.setStyleSheet("font-size:12pt;")
        self.state.setObjectName("state")
        self.cityLabel = QtWidgets.QLabel(self.personal)
        self.cityLabel.setGeometry(QtCore.QRect(30, 150, 111, 31))
        self.cityLabel.setObjectName("cityLabel")
        self.tabWidget.addTab(self.personal, "")
        self.professional = QtWidgets.QWidget()
        self.professional.setObjectName("professional")
        self.hospital = QtWidgets.QLabel(self.professional)
        self.hospital.setGeometry(QtCore.QRect(205, 190, 201, 31))
        self.hospital.setStyleSheet("font-size:12pt;")
        self.hospital.setObjectName("hospital")
        self.specializationLabel = QtWidgets.QLabel(self.professional)
        self.specializationLabel.setGeometry(QtCore.QRect(30, 110, 171, 31))
        self.specializationLabel.setObjectName("specializationLabel")
        self.qualificationLabel = QtWidgets.QLabel(self.professional)
        self.qualificationLabel.setGeometry(QtCore.QRect(30, 30, 171, 31))
        self.qualificationLabel.setObjectName("qualificationLabel")
        self.hospitalLabel = QtWidgets.QLabel(self.professional)
        self.hospitalLabel.setGeometry(QtCore.QRect(30, 190, 111, 31))
        self.hospitalLabel.setObjectName("hospitalLabel")
        self.qualificationComboBox = QtWidgets.QComboBox(self.professional)
        self.qualificationComboBox.setGeometry(QtCore.QRect(200, 30, 171, 27))
        self.qualificationComboBox.setObjectName("qualificationComboBox")
        self.newQualificationButton = QPushButton(self.professional)
        self.newQualificationButton.setText("+")
        self.newQualificationButton.setGeometry(QRect(375,30,20,27))
        self.newSpecializationButton = QPushButton(self.professional)
        self.newSpecializationButton.setText("+")
        self.newSpecializationButton.setGeometry(QRect(375,110,20,27))
        self.specializationComboBox = QtWidgets.QComboBox(self.professional)
        self.specializationComboBox.setGeometry(QtCore.QRect(200, 110, 171, 27))
        self.specializationComboBox.setObjectName("specializationComboBox")
        self.tabWidget.addTab(self.professional, "")
        self.name = QtWidgets.QLabel(editProfile)
        self.name.setGeometry(QtCore.QRect(40, 10, 371, 41))
        self.name.setStyleSheet("font-weight:bold;\n"
"font-size:13pt;")
        self.name.setObjectName("name")

        self.retranslateUi(editProfile,grandparent)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(editProfile)

    def retranslateUi(self, editProfile,grandparent):
        _translate = QtCore.QCoreApplication.translate
        editProfile.setWindowTitle(_translate("editProfile", "Profile"))
        self.exitButton.setText(_translate("editProfile", "EXIT"))
        self.saveButton.setText(_translate("editProfile", "SAVE"))
        self.doctorIDLabel.setText(_translate("editProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Doctor ID :</span></p></body></html>"))
        self.doctorID.setText(_translate("editProfile", "Doctor ID"))
        self.uploadImage.setText(_translate("editProfile", "Upload Image"))
        self.address.setPlaceholderText(_translate("editProfile", "Update your address"))
        self.addressLabel.setText(_translate("editProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Address :</span></p></body></html>"))
        self.city.setText(_translate("editProfile", "city_name"))
        self.stateLabel.setText(_translate("editProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">State : </span></p></body></html>"))
        self.state.setText(_translate("editProfile", "state_name"))
        self.cityLabel.setText(_translate("editProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">City : </span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.personal), _translate("editProfile", "Personal"))
        self.hospital.setText(_translate("editProfile", "hospital_name"))
        self.specializationLabel.setText(_translate("editProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Specialization :</span></p></body></html>"))
        self.qualificationLabel.setText(_translate("editProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Qualification :</span></p></body></html>"))
        self.hospitalLabel.setText(_translate("editProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Hospital : </span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.professional), _translate("editProfile", "Professional"))
        self.name.setText(_translate("editProfile", "first_name last_name"))


        self.clickEvents(editProfile,grandparent)

    def clickEvents(self, parent,grandparent):
        self.name.setText("Dr. " + self.doctordata["firstName"] + self.doctordata["lastName"])
        self.doctorID.setText(str(self.doctordata["id"]))
        self.address.setText(self.doctordata["address"])
        self.hospital.setText(str(self.hospitaldata["name"]))
        self.city.setText(self.doctordata["city"])
        self.state.setText(self.doctordata["state"])
        if self.doctordata["qualification"]:
            import requests
            URL = "http://127.0.0.1:8000/api/qualification/" + str(self.doctordata["qualification"])
            r = requests.get(url=URL)
            qualification = r.json()
            self.qualificationComboBox.addItem(qualification["degree"])
        if self.doctordata["specialization"]:
            URL = "http://127.0.0.1:8000/api/specialization/" + str(self.doctordata["specialization"])
            r = requests.get(url=URL)
            specialization = r.json()
            self.specializationComboBox.addItem(str(specialization["skill"]))
        self.saveButton.clicked.connect(lambda: self.clickOnSaveButton(parent,grandparent))
        self.exitButton.clicked.connect(lambda : parent.close())
        self.newQualificationButton.clicked.connect(lambda : self.addQualificationevent(parent))
        self.newSpecializationButton.clicked.connect(lambda : self.addSpecilizationevent(parent))

    def addQualificationevent(self,parent):
        print("Start")
        self.window = QDialog()
        self.dialog = addQualification()
        if self.doctordata["qualification"]:
            self.dialog.setup(self.window,self.doctordata["qualification"],self)
        else :
            self.dialog.setup(self.window,0,self)
        self.window.setModal(True)
        self.window.show()
        print("End")

    def addSpecilizationevent(self,parent):
        self.window = QDialog()
        self.dialog = addSpecialization()
        if self.doctordata["specialization"]:
            self.dialog.setup(self.window,self.doctordata["specialization"],self)
        else:
            self.dialog.setup(self.window,0,self)
        self.window.setModal(True)
        self.window.show()

    def clickOnSaveButton(self,parent,grandparent):

        address =  self.address.toPlainText()

        import requests
        URL = "http://127.0.0.1:8000/api/doctor/" + str(self.doctordata["id"])
        data = {
            "address" : address,
            "qualification" : int(self.doctordata["qualification"]),
            "specialization" : int(self.doctordata["specialization"])
        }
        r = requests.put(url=URL,data= data)
        print(r.json())
        self.doctordata = r.json()
        grandparent.doctordata = self.doctordata
        print(self.doctordata)
        self.window = messageBox()
        self.window.infoBox("Changes are saved")
        parent.close()



