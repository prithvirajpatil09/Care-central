# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eventStats.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_eventStats(object):
    def setupUi(self, eventStats):
        eventStats.setObjectName("eventStats")
        eventStats.resize(915, 504)
        self.titleLabel = QtWidgets.QLabel(eventStats)
        self.titleLabel.setGeometry(QtCore.QRect(250, 10, 361, 41))
        self.titleLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.titleLabel.setObjectName("titleLabel")
        self.titleLabel_2 = QtWidgets.QLabel(eventStats)
        self.titleLabel_2.setGeometry(QtCore.QRect(30, 80, 201, 41))
        self.titleLabel_2.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.titleLabel_2.setObjectName("titleLabel_2")
        self.titleLabel_3 = QtWidgets.QLabel(eventStats)
        self.titleLabel_3.setGeometry(QtCore.QRect(40, 130, 201, 41))
        self.titleLabel_3.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.titleLabel_3.setObjectName("titleLabel_3")
        self.totalevents = QtWidgets.QLabel(eventStats)
        self.totalevents.setGeometry(QtCore.QRect(260, 90, 67, 17))
        self.totalevents.setObjectName("totalevents")
        self.totalRegistration = QtWidgets.QLabel(eventStats)
        self.totalRegistration.setGeometry(QtCore.QRect(260, 140, 67, 17))
        self.totalRegistration.setObjectName("totalRegistration")
        self.frame = QtWidgets.QFrame(eventStats)
        self.frame.setGeometry(QtCore.QRect(10, 230, 221, 231))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.titleLabel_4 = QtWidgets.QLabel(self.frame)
        self.titleLabel_4.setGeometry(QtCore.QRect(10, 10, 201, 41))
        self.titleLabel_4.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.titleLabel_4.setObjectName("titleLabel_4")
        self.SeeHospitalEvents = QtWidgets.QPushButton(self.frame)
        self.SeeHospitalEvents.setGeometry(QtCore.QRect(20, 50, 171, 25))
        self.SeeHospitalEvents.setObjectName("SeeHospitalEvents")
        self.hid = QtWidgets.QLineEdit(self.frame)
        self.hid.setGeometry(QtCore.QRect(20, 130, 181, 25))
        self.hid.setObjectName("hid")
        self.hidbutton = QtWidgets.QPushButton(self.frame)
        self.hidbutton.setGeometry(QtCore.QRect(20, 190, 171, 25))
        self.hidbutton.setObjectName("hidbutton")
        self.frame_2 = QtWidgets.QFrame(eventStats)
        self.frame_2.setGeometry(QtCore.QRect(240, 230, 221, 231))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.titleLabel_5 = QtWidgets.QLabel(self.frame_2)
        self.titleLabel_5.setGeometry(QtCore.QRect(10, 0, 201, 41))
        self.titleLabel_5.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.titleLabel_5.setObjectName("titleLabel_5")
        self.seeBloodCamp = QtWidgets.QPushButton(self.frame_2)
        self.seeBloodCamp.setGeometry(QtCore.QRect(30, 50, 171, 25))
        self.seeBloodCamp.setObjectName("seeBloodCamp")
        self.bbcidbutton = QtWidgets.QPushButton(self.frame_2)
        self.bbcidbutton.setGeometry(QtCore.QRect(20, 190, 171, 25))
        self.bbcidbutton.setObjectName("bbcidbutton")
        self.bbcid = QtWidgets.QLineEdit(self.frame_2)
        self.bbcid.setGeometry(QtCore.QRect(20, 130, 181, 25))
        self.bbcid.setObjectName("bbcid")
        self.frame_3 = QtWidgets.QFrame(eventStats)
        self.frame_3.setGeometry(QtCore.QRect(470, 230, 221, 231))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.titleLabel_6 = QtWidgets.QLabel(self.frame_3)
        self.titleLabel_6.setGeometry(QtCore.QRect(10, 0, 201, 41))
        self.titleLabel_6.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.titleLabel_6.setObjectName("titleLabel_6")
        self.seeFirstAid = QtWidgets.QPushButton(self.frame_3)
        self.seeFirstAid.setGeometry(QtCore.QRect(20, 50, 171, 25))
        self.seeFirstAid.setObjectName("seeFirstAid")
        self.did = QtWidgets.QLineEdit(self.frame_3)
        self.did.setGeometry(QtCore.QRect(20, 130, 181, 25))
        self.did.setObjectName("did")
        self.didbutton = QtWidgets.QPushButton(self.frame_3)
        self.didbutton.setGeometry(QtCore.QRect(20, 190, 171, 25))
        self.didbutton.setObjectName("didbutton")
        self.frame_4 = QtWidgets.QFrame(eventStats)
        self.frame_4.setGeometry(QtCore.QRect(700, 230, 221, 231))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.titleLabel_7 = QtWidgets.QLabel(self.frame_4)
        self.titleLabel_7.setGeometry(QtCore.QRect(10, 10, 201, 41))
        self.titleLabel_7.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.titleLabel_7.setObjectName("titleLabel_7")
        self.seeTestCenter = QtWidgets.QPushButton(self.frame_4)
        self.seeTestCenter.setGeometry(QtCore.QRect(20, 50, 171, 25))
        self.seeTestCenter.setObjectName("seeTestCenter")
        self.tcid = QtWidgets.QLineEdit(self.frame_4)
        self.tcid.setGeometry(QtCore.QRect(20, 130, 181, 25))
        self.tcid.setObjectName("tcid")
        self.tcidbutton = QtWidgets.QPushButton(self.frame_4)
        self.tcidbutton.setGeometry(QtCore.QRect(20, 190, 171, 25))
        self.tcidbutton.setObjectName("tcidbutton")
        self.searchEventsButton = QtWidgets.QPushButton(eventStats)
        self.searchEventsButton.setGeometry(QtCore.QRect(50, 190, 171, 25))
        self.searchEventsButton.setObjectName("searchEventsButton")
        self.frame_5 = QtWidgets.QFrame(eventStats)
        self.frame_5.setGeometry(QtCore.QRect(689, 90, 221, 131))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.eventID = QtWidgets.QLineEdit(self.frame_5)
        self.eventID.setGeometry(QtCore.QRect(20, 20, 181, 25))
        self.eventID.setObjectName("eventID")
        self.eventIDButton = QtWidgets.QPushButton(self.frame_5)
        self.eventIDButton.setGeometry(QtCore.QRect(20, 70, 181, 25))
        self.eventIDButton.setObjectName("eventIDButton")
        self.superadminEventButton = QtWidgets.QPushButton(eventStats)
        self.superadminEventButton.setGeometry(QtCore.QRect(490, 190, 171, 25))
        self.superadminEventButton.setObjectName("superadminEventButton")
        self.pushButton = QtWidgets.QPushButton(eventStats)
        self.pushButton.setGeometry(QtCore.QRect(410, 470, 89, 25))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(eventStats)
        QtCore.QMetaObject.connectSlotsByName(eventStats)

    def retranslateUi(self, eventStats):
        _translate = QtCore.QCoreApplication.translate
        eventStats.setWindowTitle(_translate("eventStats", "Stats"))
        self.titleLabel.setText(_translate("eventStats", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; text-decoration: underline;\">Event Stats</span></p></body></html>"))
        self.titleLabel_2.setText(_translate("eventStats", "<html><head/><body><p align=\"center\"><span style=\" text-decoration: underline;\">Total Event Held :</span></p></body></html>"))
        self.titleLabel_3.setText(_translate("eventStats", "<html><head/><body><p align=\"center\"><span style=\" text-decoration: underline;\">Total Registrations:</span></p></body></html>"))
        self.totalevents.setText(_translate("eventStats", "TextLabel"))
        self.totalRegistration.setText(_translate("eventStats", "TextLabel"))
        self.titleLabel_4.setText(_translate("eventStats", "<html><head/><body><p align=\"center\"><span style=\" text-decoration: underline;\">Hospital Events</span></p><p align=\"center\"><span style=\" text-decoration: underline;\"><br/></span></p></body></html>"))
        self.SeeHospitalEvents.setText(_translate("eventStats", "See All "))
        self.hid.setPlaceholderText(_translate("eventStats", "Enter Hospital Id"))
        self.hidbutton.setText(_translate("eventStats", "Go To Events"))
        self.titleLabel_5.setText(_translate("eventStats", "<html><head/><body><p align=\"center\"><span style=\" text-decoration: underline;\">Blood Camps</span></p></body></html>"))
        self.seeBloodCamp.setText(_translate("eventStats", "See All "))
        self.bbcidbutton.setText(_translate("eventStats", "Go To Events"))
        self.bbcid.setPlaceholderText(_translate("eventStats", "Enter BloodBankCener Id"))
        self.titleLabel_6.setText(_translate("eventStats", "<html><head/><body><p align=\"center\"><span style=\" text-decoration: underline;\">First Aid Distribution</span></p></body></html>"))
        self.seeFirstAid.setText(_translate("eventStats", "See All "))
        self.did.setPlaceholderText(_translate("eventStats", "Enter Dispensary Id"))
        self.didbutton.setText(_translate("eventStats", "Go To Events"))
        self.titleLabel_7.setText(_translate("eventStats", "<html><head/><body><p align=\"center\"><span style=\" text-decoration: underline;\">Test Center Events</span></p><p align=\"center\"><span style=\" text-decoration: underline;\"><br/></span></p></body></html>"))
        self.seeTestCenter.setText(_translate("eventStats", "See All "))
        self.tcid.setPlaceholderText(_translate("eventStats", "Enter Test Centre Id"))
        self.tcidbutton.setText(_translate("eventStats", "Go To Events"))
        self.searchEventsButton.setText(_translate("eventStats", "Search Events"))
        self.eventID.setPlaceholderText(_translate("eventStats", "Enter Event Id"))
        self.eventIDButton.setText(_translate("eventStats", "Go To Event"))
        self.superadminEventButton.setText(_translate("eventStats", "See SuperAdmin Events"))
        self.pushButton.setText(_translate("eventStats", "close"))
