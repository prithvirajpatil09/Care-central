from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
import requests

class AppointmentDoctorDialog(object):
    def setup(self, appointmentDoctorDialog, doctordata):
        self.doctordata = doctordata
        appointmentDoctorDialog.setObjectName("appointmentDoctorDialog")
        appointmentDoctorDialog.resize(600, 235)
        self.appointmentListLabel = QtWidgets.QLabel(appointmentDoctorDialog)
        self.appointmentListLabel.setGeometry(QtCore.QRect(20, 20, 550, 181))
        self.appointmentListLabel.setObjectName("appointmentListLabel")
        font = QtGui.QFont()
        font.setPointSize(11)  
        self.appointmentListLabel.setFont(font)
        
        self.retranslateUi(appointmentDoctorDialog)
        QtCore.QMetaObject.connectSlotsByName(appointmentDoctorDialog)
        
        self.fetchAppointments()

    def retranslateUi(self, appointmentDoctorDialog):
        _translate = QtCore.QCoreApplication.translate
        appointmentDoctorDialog.setWindowTitle(_translate("appointmentDoctorDialog", "Appointments"))

    def fetchAppointments(self):
        URL = "http://127.0.0.1:8000/MDTouch/api/appointment/"
        params = {
            "doctor" : self.doctordata["id"],
            "status" : 0
         }
        r = requests.get(url=URL, params=params)
        if r.status_code == 200:
            appointments = r.json()
            appointment_text = ""
            for appointment in appointments:
                appointment_text += f"Patient ID: {appointment['patient']}, Time: {appointment['appttime']}, Phase: {appointment['phase']}, Date: {appointment['appointmentdate']}\n"
            self.appointmentListLabel.setText(appointment_text)
        else:
            self.appointmentListLabel.setText("Failed to fetch appointments.")
