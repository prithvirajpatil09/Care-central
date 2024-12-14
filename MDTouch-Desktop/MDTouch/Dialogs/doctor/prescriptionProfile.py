from PyQt5 import QtCore, QtGui, QtWidgets

class prescriptionProfile(object):
    def setup(self, writePrescription,data):
        self.data = data
        writePrescription.setObjectName("writePrescription")
        writePrescription.setWindowModality(QtCore.Qt.ApplicationModal)
        writePrescription.resize(320, 402)
        self.prescriptionLabel = QtWidgets.QLabel(writePrescription)
        self.prescriptionLabel.setGeometry(QtCore.QRect(40, 0, 261, 51))
        self.prescriptionLabel.setObjectName("prescriptionLabel")
        self.okButton = QtWidgets.QPushButton(writePrescription)
        self.okButton.setGeometry(QtCore.QRect(100, 370, 91, 21))
        self.okButton.setObjectName("okButton")
        self.patientIDLabel = QtWidgets.QLabel(writePrescription)
        self.patientIDLabel.setGeometry(QtCore.QRect(10, 90, 81, 21))
        self.patientIDLabel.setObjectName("patientIDLabel")
        self.titleLabel = QtWidgets.QLabel(writePrescription)
        self.titleLabel.setGeometry(QtCore.QRect(10, 120, 61, 21))
        self.titleLabel.setObjectName("titleLabel")
        self.prescription = QtWidgets.QTextBrowser(writePrescription)
        self.prescription.setGeometry(QtCore.QRect(10, 200, 301, 161))
        self.prescription.setObjectName("prescription")
        self.prescriptionLabel1 = QtWidgets.QLabel(writePrescription)
        self.prescriptionLabel1.setGeometry(QtCore.QRect(10, 180, 111, 21))
        self.prescriptionLabel1.setObjectName("prescriptionLabel1")
        self.prescriptionIdLabel = QtWidgets.QLabel(writePrescription)
        self.prescriptionIdLabel.setGeometry(QtCore.QRect(10, 60, 121, 21))
        self.prescriptionIdLabel.setObjectName("prescriptionIdLabel")
        self.prescriptionID = QtWidgets.QLabel(writePrescription)
        self.prescriptionID.setGeometry(QtCore.QRect(140, 60, 171, 17))
        self.prescriptionID.setObjectName("prescriptionID")
        self.patientId = QtWidgets.QLabel(writePrescription)
        self.patientId.setGeometry(QtCore.QRect(100, 90, 201, 20))
        self.patientId.setObjectName("patientId")
        self.title = QtWidgets.QLabel(writePrescription)
        self.title.setGeometry(QtCore.QRect(70, 120, 241, 20))
        self.title.setObjectName("title")
        self.diseaseLabel = QtWidgets.QLabel(writePrescription)
        self.diseaseLabel.setGeometry(QtCore.QRect(10, 150, 71, 21))
        self.diseaseLabel.setObjectName("diseaseLabel")
        self.disease = QtWidgets.QLabel(writePrescription)
        self.disease.setGeometry(QtCore.QRect(80, 150, 241, 20))
        self.disease.setObjectName("disease")

        self.retranslateUi(writePrescription)
        QtCore.QMetaObject.connectSlotsByName(writePrescription)

    def retranslateUi(self, writePrescription):
        _translate = QtCore.QCoreApplication.translate
        writePrescription.setWindowTitle(_translate("writePrescription", "Form"))
        self.prescriptionLabel.setText(_translate("writePrescription", "<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; font-weight:600; text-decoration: underline;\">Prescription</span></p></body></html>"))
        self.okButton.setText(_translate("writePrescription", "OK"))
        self.patientIDLabel.setText(_translate("writePrescription", "<html><head/><body><p><span style=\" font-weight:600;\">Patient ID :</span></p></body></html>"))
        self.titleLabel.setText(_translate("writePrescription", "<html><head/><body><p><span style=\" font-weight:600;\">Title :</span></p></body></html>"))
        self.prescription.setHtml(_translate("writePrescription", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.prescriptionLabel1.setText(_translate("writePrescription", "<html><head/><body><p><span style=\" font-weight:600;\">Prescription :</span></p></body></html>"))
        self.prescriptionIdLabel.setText(_translate("writePrescription", "<html><head/><body><p><span style=\" font-weight:600;\">Prescription ID :</span></p></body></html>"))
        self.prescriptionID.setText(_translate("writePrescription", "Prescription ID"))
        self.patientId.setText(_translate("writePrescription", "Patient_id"))
        self.title.setText(_translate("writePrescription", "title"))
        self.diseaseLabel.setText(_translate("writePrescription", "<html><head/><body><p><span style=\" font-weight:600;\">Disease : </span></p></body></html>"))
        self.disease.setText(_translate("writePrescription", "disease"))

        self.disease.setText(self.data["dosage"])
        self.title.setText(self.data["name"])
        self.prescription.setText(self.data["prescription"])
        self.patientId.setText(str(self.data["patient"]))
        self.okButton.clicked.connect(lambda : writePrescription.close())
