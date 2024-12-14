

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from Dialogs.Graphs.HospitalApointmentGraph import *
from Dialogs.Graphs.bedreportAnalysis import *

class hospitalStats(object):
    def setup(self, hospitalStats):
        hospitalStats.setObjectName("hospitalStats")
        hospitalStats.resize(355, 447)
        self.titleLabel = QtWidgets.QLabel(hospitalStats)
        self.titleLabel.setGeometry(QtCore.QRect(0, 10, 361, 41))
        self.titleLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.titleLabel.setObjectName("titleLabel")
        self.close = QtWidgets.QPushButton(hospitalStats)
        self.close.setGeometry(QtCore.QRect(130, 400, 89, 25))
        self.close.setObjectName("close")
        self.searchHospitalButton = QtWidgets.QPushButton(hospitalStats)
        self.searchHospitalButton.setGeometry(QtCore.QRect(10, 190, 161, 25))
        self.searchHospitalButton.setObjectName("searchHospitalButton")
        self.allBillsButton = QtWidgets.QPushButton(hospitalStats)
        self.allBillsButton.setGeometry(QtCore.QRect(180, 190, 161, 25))
        self.allBillsButton.setObjectName("allBillsButton")
        self.titleLabel_2 = QtWidgets.QLabel(hospitalStats)
        self.titleLabel_2.setGeometry(QtCore.QRect(-10, 80, 241, 41))
        self.titleLabel_2.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.titleLabel_2.setObjectName("titleLabel_2")
        self.titleLabel_3 = QtWidgets.QLabel(hospitalStats)
        self.titleLabel_3.setGeometry(QtCore.QRect(-20, 130, 241, 41))
        self.titleLabel_3.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.titleLabel_3.setObjectName("titleLabel_3")
        self.frame_2 = QtWidgets.QFrame(hospitalStats)
        self.frame_2.setGeometry(QtCore.QRect(10, 290, 341, 101))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.hid = QtWidgets.QLineEdit(self.frame_2)
        self.hid.setGeometry(QtCore.QRect(90, 10, 151, 25))
        self.hid.setObjectName("hid")
        self.goToProfile = QtWidgets.QPushButton(self.frame_2)
        self.goToProfile.setGeometry(QtCore.QRect(90, 60, 151, 25))
        self.goToProfile.setObjectName("goToProfile")
        self.billingstatsButton = QtWidgets.QPushButton(hospitalStats)
        self.billingstatsButton.setGeometry(QtCore.QRect(10, 250, 161, 25))
        self.billingstatsButton.setObjectName("billingstatsButton")
        self.locationstatsButton = QtWidgets.QPushButton(hospitalStats)
        self.locationstatsButton.setGeometry(QtCore.QRect(180, 250, 161, 25))
        self.locationstatsButton.setObjectName("locationstatsButton")
        self.hospitalRegistered = QtWidgets.QLabel(hospitalStats)
        self.hospitalRegistered.setGeometry(QtCore.QRect(250, 90, 67, 17))
        self.hospitalRegistered.setObjectName("hospitalRegistered")
        self.totalbills = QtWidgets.QLabel(hospitalStats)
        self.totalbills.setGeometry(QtCore.QRect(250, 140, 67, 17))
        self.totalbills.setObjectName("totalbills")

        self.retranslateUi(hospitalStats)
        QtCore.QMetaObject.connectSlotsByName(hospitalStats)

    def retranslateUi(self, hospitalStats):
        _translate = QtCore.QCoreApplication.translate
        hospitalStats.setWindowTitle(_translate("hospitalStats", "Stats"))
        self.titleLabel.setText(_translate("hospitalStats", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; text-decoration: underline;\">Hospital Stats</span></p><p align=\"center\"><br/></p></body></html>"))
        self.close.setText(_translate("hospitalStats", "close"))
        self.searchHospitalButton.setText(_translate("hospitalStats", "Search Hospitals"))
        self.allBillsButton.setText(_translate("hospitalStats", "All Hospital Bills"))
        self.titleLabel_2.setText(_translate("hospitalStats", "<html><head/><body><p align=\"center\">Hospital Registered :</p></body></html>"))
        self.titleLabel_3.setText(_translate("hospitalStats", "<html><head/><body><p align=\"center\">Total Hospital Bills:</p></body></html>"))
        self.hid.setPlaceholderText(_translate("hospitalStats", "Enter Hospital ID"))
        self.goToProfile.setText(_translate("hospitalStats", "Go To Profile"))
        self.billingstatsButton.setText(_translate("hospitalStats", "Appointment Stats"))
        self.locationstatsButton.setText(_translate("hospitalStats", "Bed Stats"))
        self.hospitalRegistered.setText(_translate("hospitalStats", "5"))
        self.totalbills.setText(_translate("hospitalStats", "TextLabel"))
        self.billingstatsButton.clicked.connect(lambda : self.clickOnbillingstats())
        self.locationstatsButton.clicked.connect(lambda : self.clickOnBedStats())

    def clickOnbillingstats(self):
        self.window = QDialog()
        self.dialog = hospitalAppointmentGraph()
        self.dialog.setup(self.window)
        self.window.setModal(True)
        self.window.show()
    def clickOnBedStats(self):
        self.window = QDialog()
        self.dialog = bedReportGraph()
        self.dialog.setup(self.window)
        self.window.setModal(True)
        self.window.show()

