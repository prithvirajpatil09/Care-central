from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from Dialogs.messageBox import *
from Dialogs.doctor.prescriptionList import *
from Dialogs.doctor.prescriptionProfile import *

class selectPrescription(object):
    def setup(self, selectPrescription,doctordata):
        self.doctordata = doctordata
        selectPrescription.setObjectName("selectPrescription")
        selectPrescription.resize(320, 295)
        selectPrescription.setWindowTitle("")
        self.title = QtWidgets.QLabel(selectPrescription)
        self.title.setGeometry(QtCore.QRect(0, 0, 321, 51))
        self.title.setObjectName("title")
        self.selectButton = QtWidgets.QPushButton(selectPrescription)
        self.selectButton.setGeometry(QtCore.QRect(100, 230, 80, 28))
        self.selectButton.setObjectName("selectButton")
        self.patientID = QtWidgets.QLineEdit(selectPrescription)
        self.patientID.setGeometry(QtCore.QRect(50, 70, 191, 27))
        self.patientID.setObjectName("patientID")
        self.prescriptionId = QtWidgets.QLineEdit(selectPrescription)
        self.prescriptionId.setGeometry(QtCore.QRect(50, 170, 191, 27))
        self.prescriptionId.setObjectName("prescriptionId")
        self.orLabel = QtWidgets.QLabel(selectPrescription)
        self.orLabel.setGeometry(QtCore.QRect(30, 110, 221, 41))
        self.orLabel.setObjectName("orLabel")

        self.retranslateUi(selectPrescription)
        QtCore.QMetaObject.connectSlotsByName(selectPrescription)

    def retranslateUi(self, selectPrescription):
        _translate = QtCore.QCoreApplication.translate
        self.title.setText(_translate("selectPrescription", "<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; font-weight:600; text-decoration: underline;\">Select Prescription</span></p></body></html>"))
        self.selectButton.setText(_translate("selectPrescription", "SELECT"))
        self.patientID.setPlaceholderText(_translate("selectPrescription", "Enter Patient ID"))
        self.prescriptionId.setPlaceholderText(_translate("selectPrescription", "Enter Prescription ID"))
        self.orLabel.setText(_translate("selectPrescription", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">OR</span></p></body></html>"))
        self.events(selectPrescription)

    def events(self,parent):
        self.selectButton.clicked.connect(lambda : self.clickOnSelectButton(parent))

    def clickOnSelectButton(self,parent):
        PatientID = self.patientID.text()
        prescriptionID = self.prescriptionId.text()
        if PatientID == "" and prescriptionID == "":
            self.window = messageBox()
            self.window.infoBox("Ivalid data")
            return
        if PatientID != "":
            if not(PatientID.isdigit()):
                self.window = messageBox()
                self.window.infoBox("Ivalid data")
                return
            params = {
                "patient" : int(PatientID),
                "doctor" : int(self.doctordata["id"])
            }
            import requests
            URL = "http://127.0.0.1:8000/api/prescription/"
            r = requests.get(url=URL,params=params)
            l = r.json()
            if len(l) == 0:
                self.window = messageBox()
                self.window.infoBox("No Prescription Found for This patient")
                return
            self.window = QDialog()
            self.dialog = prescriptionList()
            self.dialog.setup(self.window,l)
            self.window.setModal(True)
            self.window.show()
            parent.close()
        else:
            if prescriptionID.isdigit():
                import requests
                URL = "http://127.0.0.1:8000/api/prescription/" + str(prescriptionID)
                r= requests.get(url=URL)
                data = r.json()
                self.window = QDialog()
                self.dialog = prescriptionProfile()
                self.dialog.setup(self.window,data)
                self.window.setModal(True)
                self.window.show()
                parent.close()
            else:
                self.window = messageBox()
                self.window.infoBox("Ivalid Data")




