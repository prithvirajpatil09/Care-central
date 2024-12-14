

from PyQt5 import QtCore, QtGui, QtWidgets
from Dialogs.bloodBank.wasteRecordsList import *
from Dialogs.bloodBank.billingRecordList import *
from Dialogs.bloodBank.bloodentryList import *
from Dialogs.bloodBank.bloodDonationList import *
class bloodDialog(object):
    def setup(self, bloodDialog,bloodbankdata):
        self.bloodbankdata = bloodbankdata
        bloodDialog.setObjectName("bloodDialog")
        bloodDialog.resize(718, 186)
        self.wasteRecords = QtWidgets.QPushButton(bloodDialog)
        self.wasteRecords.setGeometry(QtCore.QRect(40, 10, 120, 120))
        self.wasteRecords.setMaximumSize(QtCore.QSize(120, 120))
        self.wasteRecords.setStyleSheet("border:none;")
        self.wasteRecords.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../Images/write_bill.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.wasteRecords.setIcon(icon)
        self.wasteRecords.setIconSize(QtCore.QSize(100, 100))
        self.wasteRecords.setObjectName("wasteRecords")
        self.donationRecords = QtWidgets.QPushButton(bloodDialog)
        self.donationRecords.setGeometry(QtCore.QRect(220, 10, 120, 120))
        self.donationRecords.setMaximumSize(QtCore.QSize(120, 120))
        self.donationRecords.setStyleSheet("border:none;")
        self.donationRecords.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../Images/search_prescription.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.donationRecords.setIcon(icon1)
        self.donationRecords.setIconSize(QtCore.QSize(100, 100))
        self.donationRecords.setObjectName("donationRecords")
        self.wasteRecordsLabel = QtWidgets.QLabel(bloodDialog)
        self.wasteRecordsLabel.setGeometry(QtCore.QRect(0, 120, 180, 40))
        self.wasteRecordsLabel.setMinimumSize(QtCore.QSize(180, 40))
        self.wasteRecordsLabel.setMaximumSize(QtCore.QSize(180, 40))
        self.wasteRecordsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.wasteRecordsLabel.setObjectName("wasteRecordsLabel")
        self.DonationRecordsLabel = QtWidgets.QLabel(bloodDialog)
        self.DonationRecordsLabel.setGeometry(QtCore.QRect(180, 120, 180, 40))
        self.DonationRecordsLabel.setMinimumSize(QtCore.QSize(180, 40))
        self.DonationRecordsLabel.setMaximumSize(QtCore.QSize(180, 40))
        self.DonationRecordsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.DonationRecordsLabel.setObjectName("DonationRecordsLabel")
        self.billingRecords = QtWidgets.QPushButton(bloodDialog)
        self.billingRecords.setGeometry(QtCore.QRect(400, 10, 120, 120))
        self.billingRecords.setMaximumSize(QtCore.QSize(120, 120))
        self.billingRecords.setStyleSheet("border:none;")
        self.billingRecords.setText("")
        self.billingRecords.setIcon(icon1)
        self.billingRecords.setIconSize(QtCore.QSize(100, 100))
        self.billingRecords.setObjectName("billingRecords")
        self.billingRecordsLabel = QtWidgets.QLabel(bloodDialog)
        self.billingRecordsLabel.setGeometry(QtCore.QRect(370, 120, 180, 40))
        self.billingRecordsLabel.setMinimumSize(QtCore.QSize(180, 40))
        self.billingRecordsLabel.setMaximumSize(QtCore.QSize(180, 40))
        self.billingRecordsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.billingRecordsLabel.setObjectName("billingRecordsLabel")
        self.entryRecordLabel = QtWidgets.QLabel(bloodDialog)
        self.entryRecordLabel.setGeometry(QtCore.QRect(540, 120, 180, 40))
        self.entryRecordLabel.setMinimumSize(QtCore.QSize(180, 40))
        self.entryRecordLabel.setMaximumSize(QtCore.QSize(180, 40))
        self.entryRecordLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.entryRecordLabel.setObjectName("entryRecordLabel")
        self.entryRecord = QtWidgets.QPushButton(bloodDialog)
        self.entryRecord.setGeometry(QtCore.QRect(570, 10, 120, 120))
        self.entryRecord.setMaximumSize(QtCore.QSize(120, 120))
        self.entryRecord.setStyleSheet("border:none;")
        self.entryRecord.setText("")
        self.entryRecord.setIcon(icon1)
        self.entryRecord.setIconSize(QtCore.QSize(100, 100))
        self.entryRecord.setObjectName("entryRecord")

        self.retranslateUi(bloodDialog)
        QtCore.QMetaObject.connectSlotsByName(bloodDialog)

    def retranslateUi(self, bloodDialog):
        _translate = QtCore.QCoreApplication.translate
        bloodDialog.setWindowTitle(_translate("bloodDialog", "Records"))
        self.wasteRecordsLabel.setText(_translate("bloodDialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">Waste Records</span></p></body></html>"))
        self.DonationRecordsLabel.setText(_translate("bloodDialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">Donation Records</span></p></body></html>"))
        self.billingRecordsLabel.setText(_translate("bloodDialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">Billing Records</span></p></body></html>"))
        self.entryRecordLabel.setText(_translate("bloodDialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">Entry Records</span></p></body></html>"))
        self.events(bloodDialog)

    def events(self,parent):
        self.wasteRecords.clicked.connect(lambda : self.clickOnwasteRecords(parent))
        self.billingRecords.clicked.connect(lambda : self.clickOnbillingrecords(parent))
        self.donationRecords.clicked.connect(lambda : self.clickOnDonationRecords(parent))
        self.entryRecord.clicked.connect(lambda : self.clickOnEntryRecord(parent))

    def clickOnEntryRecord(self,parent):
        self.window = QDialog()
        self.dialog = bloodentryList()
        self.dialog.setup(self.window,self.bloodbankdata)
        self.window.setModal(True)
        self.window.show()


    def clickOnDonationRecords(self,parent):
        self.window = QDialog()
        self.dialog = donationList()
        self.dialog.setup(self.window,self.bloodbankdata)
        self.window.setModal(True)
        self.window.show()


    def clickOnbillingrecords(self,parent):
        self.window = QDialog()
        self.dialog = billingList()
        self.dialog.setup(self.window,self.bloodbankdata)
        self.window.setModal(True)
        self.window.show()


    def clickOnwasteRecords(self,parent):
        self.window = QDialog()
        self.dialog = wasteRecordList()
        self.dialog.setup(self.window,self.bloodbankdata)
        self.window.setModal(True)
        self.window.show()

