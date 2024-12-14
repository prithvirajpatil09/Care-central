from PyQt5 import QtCore, QtGui, QtWidgets
from Dialogs.Message.broadcastList import *
from Dialogs.doctor.doctorMessageList import *
from PyQt5.QtWidgets import *

class messageDoctorDialog(object):
    def setup(self, messageDoctorDialog,data,hospitaldata):
        self.logindata = data
        self.hospitaldata = hospitaldata
        messageDoctorDialog.setObjectName("messageDoctorDialog")
        messageDoctorDialog.resize(348, 228)
        self.doctorMessage = QtWidgets.QPushButton(messageDoctorDialog)
        self.doctorMessage.setGeometry(QtCore.QRect(40, 10, 120, 120))
        self.doctorMessage.setMaximumSize(QtCore.QSize(120, 120))
        self.doctorMessage.setStyleSheet("border:none;")
        self.doctorMessage.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../Images/write_bill.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.doctorMessage.setIcon(icon)
        self.doctorMessage.setIconSize(QtCore.QSize(100, 100))
        self.doctorMessage.setObjectName("doctorMessage")
        self.broadcastMessage = QtWidgets.QPushButton(messageDoctorDialog)
        self.broadcastMessage.setGeometry(QtCore.QRect(190, 20, 120, 120))
        self.broadcastMessage.setMaximumSize(QtCore.QSize(120, 120))
        self.broadcastMessage.setStyleSheet("border:none;")
        self.broadcastMessage.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../Images/search_prescription.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.broadcastMessage.setIcon(icon1)
        self.broadcastMessage.setIconSize(QtCore.QSize(100, 100))
        self.broadcastMessage.setObjectName("broadcastMessage")
        self.doctorMessageLabel = QtWidgets.QLabel(messageDoctorDialog)
        self.doctorMessageLabel.setGeometry(QtCore.QRect(0, 130, 180, 80))
        self.doctorMessageLabel.setMinimumSize(QtCore.QSize(180, 80))
        self.doctorMessageLabel.setMaximumSize(QtCore.QSize(180, 40))
        self.doctorMessageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.doctorMessageLabel.setObjectName("doctorMessageLabel")
        self.broadcastMessageLabel = QtWidgets.QLabel(messageDoctorDialog)
        self.broadcastMessageLabel.setGeometry(QtCore.QRect(160, 130, 180, 80))
        self.broadcastMessageLabel.setMinimumSize(QtCore.QSize(180, 80))
        self.broadcastMessageLabel.setMaximumSize(QtCore.QSize(180, 40))
        self.broadcastMessageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.broadcastMessageLabel.setObjectName("broadcastMessageLabel")

        self.retranslateUi(messageDoctorDialog)
        QtCore.QMetaObject.connectSlotsByName(messageDoctorDialog)

    def retranslateUi(self, messageDoctorDialog):
        _translate = QtCore.QCoreApplication.translate
        messageDoctorDialog.setWindowTitle(_translate("messageDoctorDialog", "Messages"))
        self.doctorMessageLabel.setText(_translate("messageDoctorDialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">Doctors</span></p><p><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">Message</span></p></body></html>"))
        self.broadcastMessageLabel.setText(_translate("messageDoctorDialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">Broadcast</span></p><p><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">Messages</span></p></body></html>"))

        self.clickevents(messageDoctorDialog)

    def clickevents(self,parent):
        self.broadcastMessage.clicked.connect(lambda : self.clickOnBroadcastMEssage(parent))
        self.doctorMessage.clicked.connect(lambda : self.clickOnDoctorMessage(parent))

    def clickOnBroadcastMEssage(self,parent):
        self.window = QDialog()
        self.dialog = broadcastList()
        self.dialog.setup(self.window)
        self.window.setModal(True)
        self.window.show()

    def clickOnDoctorMessage(self,parent):
        self.window = QDialog()
        self.dialog = messageDoctorDialog()
        self.dialog.setup(self.window,self.logindata, self.hospitaldata)
        self.window.setModal(True)
        self.window.show()
