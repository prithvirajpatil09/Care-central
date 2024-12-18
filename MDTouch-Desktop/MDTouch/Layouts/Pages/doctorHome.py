# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'doctorHome.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_doctorHome(object):
    def setupUi(self, doctorHome):
        doctorHome.setObjectName("doctorHome")
        doctorHome.resize(1366, 779)
        self.centralwidget = QtWidgets.QWidget(doctorHome)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(550, 20, 281, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        self.title.setMinimumSize(QtCore.QSize(0, 50))
        self.title.setMaximumSize(QtCore.QSize(400, 70))
        self.title.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.title.setObjectName("title")
        self.logout = QtWidgets.QPushButton(self.centralwidget)
        self.logout.setGeometry(QtCore.QRect(1250, 10, 100, 90))
        self.logout.setMinimumSize(QtCore.QSize(100, 90))
        self.logout.setMaximumSize(QtCore.QSize(100, 90))
        self.logout.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-style:solid;\n"
"border-width:2px;")
        self.logout.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Images/LogoutIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logout.setIcon(icon)
        self.logout.setIconSize(QtCore.QSize(80, 80))
        self.logout.setObjectName("logout")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 300, 1331, 111))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.writePrescription = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.writePrescription.setMinimumSize(QtCore.QSize(100, 100))
        self.writePrescription.setMaximumSize(QtCore.QSize(100, 100))
        self.writePrescription.setStyleSheet("border:none;")
        self.writePrescription.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../Images/prescription.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.writePrescription.setIcon(icon1)
        self.writePrescription.setIconSize(QtCore.QSize(100, 100))
        self.writePrescription.setObjectName("writePrescription")
        self.horizontalLayout_2.addWidget(self.writePrescription)
        self.searchPrescriptions = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.searchPrescriptions.setMinimumSize(QtCore.QSize(100, 100))
        self.searchPrescriptions.setMaximumSize(QtCore.QSize(100, 100))
        self.searchPrescriptions.setStyleSheet("border:none;")
        self.searchPrescriptions.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../Images/search_prescription.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchPrescriptions.setIcon(icon2)
        self.searchPrescriptions.setIconSize(QtCore.QSize(100, 100))
        self.searchPrescriptions.setObjectName("searchPrescriptions")
        self.horizontalLayout_2.addWidget(self.searchPrescriptions)
        self.patients = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.patients.setMinimumSize(QtCore.QSize(100, 100))
        self.patients.setMaximumSize(QtCore.QSize(100, 100))
        self.patients.setStyleSheet("border:none;")
        self.patients.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../Images/patients.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.patients.setIcon(icon3)
        self.patients.setIconSize(QtCore.QSize(100, 100))
        self.patients.setObjectName("patients")
        self.horizontalLayout_2.addWidget(self.patients)
        self.appointments = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.appointments.setMinimumSize(QtCore.QSize(100, 100))
        self.appointments.setMaximumSize(QtCore.QSize(100, 100))
        self.appointments.setStyleSheet("border:none;")
        self.appointments.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../../Images/appointments.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.appointments.setIcon(icon4)
        self.appointments.setIconSize(QtCore.QSize(100, 100))
        self.appointments.setObjectName("appointments")
        self.horizontalLayout_2.addWidget(self.appointments)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 490, 1331, 111))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.searchHospitals = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.searchHospitals.setMinimumSize(QtCore.QSize(100, 100))
        self.searchHospitals.setMaximumSize(QtCore.QSize(100, 100))
        self.searchHospitals.setStyleSheet("border:none;")
        self.searchHospitals.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../../Images/search_hospitals.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchHospitals.setIcon(icon5)
        self.searchHospitals.setIconSize(QtCore.QSize(100, 100))
        self.searchHospitals.setObjectName("searchHospitals")
        self.horizontalLayout_3.addWidget(self.searchHospitals)
        self.searchBloodBankCenters = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.searchBloodBankCenters.setMinimumSize(QtCore.QSize(100, 100))
        self.searchBloodBankCenters.setMaximumSize(QtCore.QSize(100, 100))
        self.searchBloodBankCenters.setStyleSheet("border:none;")
        self.searchBloodBankCenters.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../../Images/view_bloodBanks.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchBloodBankCenters.setIcon(icon6)
        self.searchBloodBankCenters.setIconSize(QtCore.QSize(100, 100))
        self.searchBloodBankCenters.setObjectName("searchBloodBankCenters")
        self.horizontalLayout_3.addWidget(self.searchBloodBankCenters)
        self.searchTestCenters = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.searchTestCenters.setMinimumSize(QtCore.QSize(100, 100))
        self.searchTestCenters.setMaximumSize(QtCore.QSize(100, 100))
        self.searchTestCenters.setStyleSheet("border:none;")
        self.searchTestCenters.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../../Images/search_testCenters.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchTestCenters.setIcon(icon7)
        self.searchTestCenters.setIconSize(QtCore.QSize(100, 100))
        self.searchTestCenters.setObjectName("searchTestCenters")
        self.horizontalLayout_3.addWidget(self.searchTestCenters)
        self.searchDispensaries = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.searchDispensaries.setMinimumSize(QtCore.QSize(100, 100))
        self.searchDispensaries.setMaximumSize(QtCore.QSize(100, 100))
        self.searchDispensaries.setStyleSheet("border:none;")
        self.searchDispensaries.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("../../Images/search_medicines.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchDispensaries.setIcon(icon8)
        self.searchDispensaries.setIconSize(QtCore.QSize(100, 100))
        self.searchDispensaries.setObjectName("searchDispensaries")
        self.horizontalLayout_3.addWidget(self.searchDispensaries)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 120, 1331, 109))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.editProfile = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.editProfile.setMinimumSize(QtCore.QSize(100, 100))
        self.editProfile.setMaximumSize(QtCore.QSize(100, 100))
        self.editProfile.setStyleSheet("border:none;")
        self.editProfile.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("../../Images/edit_profile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.editProfile.setIcon(icon9)
        self.editProfile.setIconSize(QtCore.QSize(100, 100))
        self.editProfile.setObjectName("editProfile")
        self.horizontalLayout.addWidget(self.editProfile)
        self.myHospital = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.myHospital.setMinimumSize(QtCore.QSize(100, 100))
        self.myHospital.setMaximumSize(QtCore.QSize(100, 100))
        self.myHospital.setStyleSheet("border:none;")
        self.myHospital.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("../../Images/my_hospital.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.myHospital.setIcon(icon10)
        self.myHospital.setIconSize(QtCore.QSize(100, 100))
        self.myHospital.setObjectName("myHospital")
        self.horizontalLayout.addWidget(self.myHospital)
        self.notices = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.notices.setMinimumSize(QtCore.QSize(100, 100))
        self.notices.setMaximumSize(QtCore.QSize(100, 100))
        self.notices.setStyleSheet("border:none;")
        self.notices.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("../../Images/notices.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.notices.setIcon(icon11)
        self.notices.setIconSize(QtCore.QSize(100, 100))
        self.notices.setObjectName("notices")
        self.horizontalLayout.addWidget(self.notices)
        self.changePassword = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.changePassword.setMinimumSize(QtCore.QSize(100, 100))
        self.changePassword.setMaximumSize(QtCore.QSize(100, 100))
        self.changePassword.setStyleSheet("border:none;")
        self.changePassword.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("../../Images/change_password.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.changePassword.setIcon(icon12)
        self.changePassword.setIconSize(QtCore.QSize(100, 100))
        self.changePassword.setObjectName("changePassword")
        self.horizontalLayout.addWidget(self.changePassword)
        self.editProfileLabel = QtWidgets.QLabel(self.centralwidget)
        self.editProfileLabel.setGeometry(QtCore.QRect(180, 230, 150, 40))
        self.editProfileLabel.setMinimumSize(QtCore.QSize(150, 40))
        self.editProfileLabel.setMaximumSize(QtCore.QSize(150, 40))
        self.editProfileLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.editProfileLabel.setObjectName("editProfileLabel")
        self.appointmentsLabel = QtWidgets.QLabel(self.centralwidget)
        self.appointmentsLabel.setGeometry(QtCore.QRect(1020, 410, 180, 40))
        self.appointmentsLabel.setMinimumSize(QtCore.QSize(180, 40))
        self.appointmentsLabel.setMaximumSize(QtCore.QSize(180, 40))
        self.appointmentsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.appointmentsLabel.setObjectName("appointmentsLabel")
        self.patientsLabel = QtWidgets.QLabel(self.centralwidget)
        self.patientsLabel.setGeometry(QtCore.QRect(750, 410, 150, 40))
        self.patientsLabel.setMinimumSize(QtCore.QSize(150, 40))
        self.patientsLabel.setMaximumSize(QtCore.QSize(150, 40))
        self.patientsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.patientsLabel.setObjectName("patientsLabel")
        self.noticesLabel = QtWidgets.QLabel(self.centralwidget)
        self.noticesLabel.setGeometry(QtCore.QRect(745, 230, 150, 40))
        self.noticesLabel.setMinimumSize(QtCore.QSize(150, 40))
        self.noticesLabel.setMaximumSize(QtCore.QSize(150, 40))
        self.noticesLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.noticesLabel.setObjectName("noticesLabel")
        self.writePrescriptionLabel = QtWidgets.QLabel(self.centralwidget)
        self.writePrescriptionLabel.setGeometry(QtCore.QRect(130, 410, 240, 40))
        self.writePrescriptionLabel.setMinimumSize(QtCore.QSize(240, 40))
        self.writePrescriptionLabel.setMaximumSize(QtCore.QSize(240, 40))
        self.writePrescriptionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.writePrescriptionLabel.setObjectName("writePrescriptionLabel")
        self.searchPrescriptionsLabel = QtWidgets.QLabel(self.centralwidget)
        self.searchPrescriptionsLabel.setGeometry(QtCore.QRect(400, 410, 240, 40))
        self.searchPrescriptionsLabel.setMinimumSize(QtCore.QSize(240, 40))
        self.searchPrescriptionsLabel.setMaximumSize(QtCore.QSize(240, 40))
        self.searchPrescriptionsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.searchPrescriptionsLabel.setObjectName("searchPrescriptionsLabel")
        self.consultsLabel = QtWidgets.QLabel(self.centralwidget)
        self.consultsLabel.setGeometry(QtCore.QRect(460, 230, 150, 40))
        self.consultsLabel.setMinimumSize(QtCore.QSize(150, 40))
        self.consultsLabel.setMaximumSize(QtCore.QSize(150, 40))
        self.consultsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.consultsLabel.setObjectName("consultsLabel")
        self.changePasswordLabel = QtWidgets.QLabel(self.centralwidget)
        self.changePasswordLabel.setGeometry(QtCore.QRect(1000, 230, 240, 40))
        self.changePasswordLabel.setMinimumSize(QtCore.QSize(240, 40))
        self.changePasswordLabel.setMaximumSize(QtCore.QSize(240, 40))
        self.changePasswordLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.changePasswordLabel.setObjectName("changePasswordLabel")
        self.searchHospitalsLabel = QtWidgets.QLabel(self.centralwidget)
        self.searchHospitalsLabel.setGeometry(QtCore.QRect(120, 600, 240, 40))
        self.searchHospitalsLabel.setMinimumSize(QtCore.QSize(240, 40))
        self.searchHospitalsLabel.setMaximumSize(QtCore.QSize(240, 40))
        self.searchHospitalsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.searchHospitalsLabel.setObjectName("searchHospitalsLabel")
        self.searchBloodBanksLabel = QtWidgets.QLabel(self.centralwidget)
        self.searchBloodBanksLabel.setGeometry(QtCore.QRect(400, 600, 240, 71))
        self.searchBloodBanksLabel.setMinimumSize(QtCore.QSize(240, 40))
        self.searchBloodBanksLabel.setMaximumSize(QtCore.QSize(240, 80))
        self.searchBloodBanksLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.searchBloodBanksLabel.setObjectName("searchBloodBanksLabel")
        self.searchTestCentersLabel = QtWidgets.QLabel(self.centralwidget)
        self.searchTestCentersLabel.setGeometry(QtCore.QRect(700, 600, 240, 71))
        self.searchTestCentersLabel.setMinimumSize(QtCore.QSize(240, 40))
        self.searchTestCentersLabel.setMaximumSize(QtCore.QSize(240, 80))
        self.searchTestCentersLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.searchTestCentersLabel.setObjectName("searchTestCentersLabel")
        self.searchDispensariesLabel = QtWidgets.QLabel(self.centralwidget)
        self.searchDispensariesLabel.setGeometry(QtCore.QRect(990, 600, 240, 40))
        self.searchDispensariesLabel.setMinimumSize(QtCore.QSize(240, 40))
        self.searchDispensariesLabel.setMaximumSize(QtCore.QSize(240, 40))
        self.searchDispensariesLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.searchDispensariesLabel.setObjectName("searchDispensariesLabel")
        self.myHospitalLabel = QtWidgets.QPushButton(self.centralwidget)
        self.myHospitalLabel.setGeometry(QtCore.QRect(1120, 10, 100, 90))
        self.myHospitalLabel.setMinimumSize(QtCore.QSize(100, 90))
        self.myHospitalLabel.setMaximumSize(QtCore.QSize(100, 90))
        self.myHospitalLabel.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-style:solid;\n"
"border-width:2px;")
        self.myHospitalLabel.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("../../Images/doctor_consultant.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.myHospitalLabel.setIcon(icon13)
        self.myHospitalLabel.setIconSize(QtCore.QSize(80, 80))
        self.myHospitalLabel.setObjectName("myHospitalLabel")
        doctorHome.setCentralWidget(self.centralwidget)

        self.retranslateUi(doctorHome)
        QtCore.QMetaObject.connectSlotsByName(doctorHome)

    def retranslateUi(self, doctorHome):
        _translate = QtCore.QCoreApplication.translate
        doctorHome.setWindowTitle(_translate("doctorHome", "MainWindow"))
        self.title.setText(_translate("doctorHome", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:25pt; font-weight:600; text-decoration: underline;\">MDTouch</span></p></body></html>"))
        self.editProfileLabel.setText(_translate("doctorHome", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">Edit Profile</span></p></body></html>"))
        self.appointmentsLabel.setText(_translate("doctorHome", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">Appointments</span></p></body></html>"))
        self.patientsLabel.setText(_translate("doctorHome", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">My Patients</span></p></body></html>"))
        self.noticesLabel.setText(_translate("doctorHome", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">Notices</span></p></body></html>"))
        self.writePrescriptionLabel.setText(_translate("doctorHome", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">Write Prescription</span></p></body></html>"))
        self.searchPrescriptionsLabel.setText(_translate("doctorHome", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">Search Prescriptions</span></p></body></html>"))
        self.consultsLabel.setText(_translate("doctorHome", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">My Hospital</span></p></body></html>"))
        self.changePasswordLabel.setText(_translate("doctorHome", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">Change Password</span></p></body></html>"))
        self.searchHospitalsLabel.setText(_translate("doctorHome", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">Search Hospitals</span></p></body></html>"))
        self.searchBloodBanksLabel.setText(_translate("doctorHome", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">Search </span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">Blood Banks</span></p></body></html>"))
        self.searchTestCentersLabel.setText(_translate("doctorHome", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">Search </span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">Test Centers</span></p></body></html>"))
        self.searchDispensariesLabel.setText(_translate("doctorHome", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">Search Dispensaries</span></p></body></html>"))

