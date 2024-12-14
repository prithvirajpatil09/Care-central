from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import requests


class myPatientDoctorList(object):
    def setup(self, patientListDialog, doctor_data):
        self.doctor_data = doctor_data
        patientListDialog.setObjectName("patientListDialog")
        patientListDialog.resize(600, 235)
        self.patientListLabel = QtWidgets.QLabel(patientListDialog)
        self.patientListLabel.setGeometry(QtCore.QRect(20, 20, 550, 181))
        self.patientListLabel.setObjectName("patientListLabel")
        font = QtGui.QFont()
        font.setPointSize(11)
        self.patientListLabel.setFont(font)
        
        self.retranslateUi(patientListDialog)
        QtCore.QMetaObject.connectSlotsByName(patientListDialog)
        
        self.fetchPatientsWithAppointments()

    def retranslateUi(self, patientListDialog):
        _translate = QtCore.QCoreApplication.translate
        patientListDialog.setWindowTitle(_translate("patientListDialog", "Patient List"))

    def fetchPatientsWithAppointments(self):
        appointment_URL = "http://127.0.0.1:8000/MDTouch/api/appointment/"
        appointment_params = {
            "doctor": self.doctor_data["id"]
        }
        appointment_response = requests.get(url=appointment_URL, params=appointment_params)
        
        if appointment_response.status_code == 200:
            appointments = appointment_response.json()
            patient_ids = [appointment['patient'] for appointment in appointments]
            patients = self.fetchPatientsByID(patient_ids)
            
            if patients:
                patient_text = ""
                for patient in patients:
                    patient_text += f"Patient ID: {patient['id']},   Name: {patient['firstName']} {patient['lastName']},   Gender: {patient['gender']}\n"
                self.patientListLabel.setText(patient_text)
            else:
                self.patientListLabel.setText("No patients with appointments found.")
        else:
            self.patientListLabel.setText("Failed to fetch appointments.")

    def fetchPatientsByID(self, patient_ids):
        patient_URL = "http://127.0.0.1:8000/MDTouch/api/patient/"
        patient_response = requests.get(url=patient_URL)
        
        if patient_response.status_code == 200:
            patients = patient_response.json()
            return [patient for patient in patients if patient['id'] in patient_ids]
        else:
            return []

