from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Dialogs.superadmin.Events.addEvent import *
from Dialogs.superadmin.Events.myEventList import *
from Dialogs.superadmin.Events.viewEvents import *
from Dialogs.superadmin.Events.selectEvent import *

class bloodCampDialog(object):
    def setup(self, bloodCampDialog, bloodbankdata = None):
        self.bloodbankdata = bloodbankdata
        bloodCampDialog.setObjectName("bloodCampDialog")
        bloodCampDialog.resize(553, 219)
        self.cancelBloodCampLabel = QtWidgets.QLabel(bloodCampDialog)
        self.cancelBloodCampLabel.setGeometry(QtCore.QRect(390, 130, 141, 71))
        self.cancelBloodCampLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.cancelBloodCampLabel.setObjectName("cancelBloodCampLabel")
        self.cancelBloodCamp = QtWidgets.QPushButton(bloodCampDialog)
        self.cancelBloodCamp.setGeometry(QtCore.QRect(410, 20, 100, 100))
        self.cancelBloodCamp.setMinimumSize(QtCore.QSize(100, 100))
        self.cancelBloodCamp.setMaximumSize(QtCore.QSize(100, 100))
        self.cancelBloodCamp.setStyleSheet("border:none;")
        self.cancelBloodCamp.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Images/remove_bloodBank.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancelBloodCamp.setIcon(icon)
        self.cancelBloodCamp.setIconSize(QtCore.QSize(100, 100))
        self.cancelBloodCamp.setObjectName("cancelBloodCamp")
        self.viewBloodCampsLabel = QtWidgets.QLabel(bloodCampDialog)
        self.viewBloodCampsLabel.setGeometry(QtCore.QRect(160, 130, 221, 71))
        self.viewBloodCampsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.viewBloodCampsLabel.setObjectName("viewBloodCampsLabel")
        self.addBloodCampLabel = QtWidgets.QLabel(bloodCampDialog)
        self.addBloodCampLabel.setGeometry(QtCore.QRect(0, 120, 181, 91))
        self.addBloodCampLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.addBloodCampLabel.setObjectName("addBloodCampLabel")
        self.addBloodCamp = QtWidgets.QPushButton(bloodCampDialog)
        self.addBloodCamp.setGeometry(QtCore.QRect(40, 20, 100, 100))
        self.addBloodCamp.setMinimumSize(QtCore.QSize(100, 100))
        self.addBloodCamp.setMaximumSize(QtCore.QSize(100, 100))
        self.addBloodCamp.setStyleSheet("border:none;")
        self.addBloodCamp.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../Images/blood_camp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addBloodCamp.setIcon(icon1)
        self.addBloodCamp.setIconSize(QtCore.QSize(100, 100))
        self.addBloodCamp.setObjectName("addBloodCamp")
        self.viewBloodCamps = QtWidgets.QPushButton(bloodCampDialog)
        self.viewBloodCamps.setGeometry(QtCore.QRect(230, 20, 100, 100))
        self.viewBloodCamps.setMinimumSize(QtCore.QSize(100, 100))
        self.viewBloodCamps.setMaximumSize(QtCore.QSize(100, 100))
        self.viewBloodCamps.setStyleSheet("border:none;")
        self.viewBloodCamps.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../Images/view_bloodBanks.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.viewBloodCamps.setIcon(icon2)
        self.viewBloodCamps.setIconSize(QtCore.QSize(100, 100))
        self.viewBloodCamps.setObjectName("viewBloodCamps")


        self.retranslateUi(bloodCampDialog)
        QtCore.QMetaObject.connectSlotsByName(bloodCampDialog)

    def retranslateUi(self, bloodCampDialog):
        _translate = QtCore.QCoreApplication.translate
        bloodCampDialog.setWindowTitle(_translate("bloodCampDialog", "Blood Camp"))
        self.cancelBloodCampLabel.setText(_translate("bloodCampDialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">Cancel<br>Blood Camp</span></p></body></html>"))
        self.viewBloodCampsLabel.setText(_translate("bloodCampDialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">View<br>Blood Camps</span></p></body></html>"))
        self.addBloodCampLabel.setText(_translate("bloodCampDialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">Add<br>Blood Camp</span></p></body></html>"))
        self.events(bloodCampDialog)

    def events(self,parent):
        self.addBloodCamp.clicked.connect(lambda : self.clickOnAddBloodCamp(parent))
        self.cancelBloodCamp.clicked.connect(lambda : self.clickOndeleteBloodCamp(parent))
        self.viewBloodCamps.clicked.connect(lambda : self.clickOnViewBloodCam(parent))

    def clickOnAddBloodCamp(self,parent):
        self.window = QDialog()
        self.dialog = addEvent()
        self.dialog.setup(self.window,'BB',self.bloodbankdata)
        self.window.setModal(True)
        self.window.show()
        parent.close()

    def clickOnViewBloodCam(self,parent):
        self.window = QDialog()
        self.dialog = viewEvent()
        self.dialog.setup(self.window,"BB",self.bloodbankdata)
        self.window.setModal(True)
        self.window.show()
        parent.close()

    def clickOndeleteBloodCamp(self,parent):
        self.window = QDialog()
        self.dialog = selectEvent()
        self.dialog.setup(self.window,'BB',self.bloodbankdata)
        self.window.setModal(True)
        self.window.show()
        parent.close()

