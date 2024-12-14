from PyQt5 import QtCore, QtGui, QtWidgets
from Dialogs.messageBox import *

class writePrescription(object):
    def setup(self, writePrescription,doctordata):
        self.doctordata = doctordata
        writePrescription.setObjectName("writePrescription")
        writePrescription.setWindowModality(QtCore.Qt.ApplicationModal)
        writePrescription.resize(320, 395)
        self.writePrescriptionLabel = QtWidgets.QLabel(writePrescription)
        self.writePrescriptionLabel.setGeometry(QtCore.QRect(10, 0, 281, 51))
        self.writePrescriptionLabel.setObjectName("writePrescriptionLabel")
        self.prescriptionBox = QtWidgets.QTextEdit(writePrescription)
        self.prescriptionBox.setGeometry(QtCore.QRect(10, 180, 301, 161))
        self.prescriptionBox.setObjectName("prescriptionBox")
        self.okButton = QtWidgets.QPushButton(writePrescription)
        self.okButton.setGeometry(QtCore.QRect(110, 350, 91, 21))
        self.okButton.setObjectName("okButton")
        self.patientID = QtWidgets.QLineEdit(writePrescription)
        self.patientID.setGeometry(QtCore.QRect(100, 70, 211, 21))
        self.patientID.setText("")
        self.patientID.setObjectName("patientID")
        self.patientIDLabel = QtWidgets.QLabel(writePrescription)
        self.patientIDLabel.setGeometry(QtCore.QRect(10, 70, 81, 21))
        self.patientIDLabel.setObjectName("patientIDLabel")
        self.title = QtWidgets.QLineEdit(writePrescription)
        self.title.setGeometry(QtCore.QRect(60, 100, 251, 21))
        self.title.setText("")
        self.title.setObjectName("title")
        self.titleLabel = QtWidgets.QLabel(writePrescription)
        self.titleLabel.setGeometry(QtCore.QRect(10, 100, 61, 21))
        self.titleLabel.setObjectName("titleLabel")
        self.disease = QtWidgets.QLineEdit(writePrescription)
        self.disease.setGeometry(QtCore.QRect(90, 140, 221, 21))
        self.disease.setText("")
        self.disease.setObjectName("disease")
        self.diseaseLabel = QtWidgets.QLabel(writePrescription)
        self.diseaseLabel.setGeometry(QtCore.QRect(10, 140, 71, 21))
        self.diseaseLabel.setObjectName("diseaseLabel")

        self.retranslateUi(writePrescription)
        QtCore.QMetaObject.connectSlotsByName(writePrescription)

    def retranslateUi(self, writePrescription):
        _translate = QtCore.QCoreApplication.translate
        writePrescription.setWindowTitle(_translate("writePrescription", "Form"))
        self.writePrescriptionLabel.setText(_translate("writePrescription", "<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; font-weight:600; text-decoration: underline;\">Write Prescription</span></p></body></html>"))
        self.prescriptionBox.setHtml(_translate("writePrescription", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.prescriptionBox.setPlaceholderText(_translate("writePrescription", "write prescription here"))
        self.okButton.setText(_translate("writePrescription", "OK"))
        self.patientIDLabel.setText(_translate("writePrescription", "<html><head/><body><p><span style=\" font-weight:600;\">Patient ID :</span></p></body></html>"))
        self.titleLabel.setText(_translate("writePrescription", "<html><head/><body><p><span style=\" font-weight:600;\">Title :</span></p></body></html>"))
        self.diseaseLabel.setText(_translate("writePrescription", "<html><head/><body><p><span style=\" font-weight:600;\">Disease : </span></p></body></html>"))

        self.events(writePrescription)

    def events(self,parent):
        self.okButton.clicked.connect(lambda : self.clickOnWrite(parent))

    def clickOnWrite(self,parent):
        patientId = self.patientID.text()
        data = {
            "patientid" : int(patientId),
            "doctorid" : int(self.doctordata["id"]),
        }
        URL = "http://127.0.0.1:8000/MDTouch/api/appointment/"
        import requests
        r = requests.get(url=URL,params=data)
        appointmentData = r.json()
        if len(appointmentData) == 0:
            self.window = messageBox()
            self.window.infoBox("This is not your Patient. Either you have not accepted his appointment")
            return
        title = self.title.text()
        disease = self.disease.text()
        prescription = self.prescriptionBox.toPlainText()
        data = {

            "name": title,
            "dosage": disease,
            "prescription": prescription,
            "patient": int(patientId),
            "doctor": int(self.doctordata["id"])
        }
        URL = "http://127.0.0.1:8000/MDTouch/api/prescription/"
        r = requests.post(url=URL,data=data)
        prescriptiondata = r.json()
        URL = "http://127.0.0.1:8000/MDTouch/api/appointment/" + str(appointmentData[0]["id"])
        r = requests.delete(url=URL)
        self.window = messageBox()
        self.window.infoBox("Prescription Generated with ID : ")
        parent.close()



