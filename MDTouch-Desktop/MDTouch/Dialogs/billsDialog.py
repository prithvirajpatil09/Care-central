from PyQt5 import QtCore, QtGui, QtWidgets

class billsDialog(object):
    def setup(self, billsDialog,hospitalData):
        self.hospitaldata = hospitalData
        billsDialog.setObjectName("billsDialog")
        billsDialog.resize(348, 186)
        self.createBill = QtWidgets.QPushButton(billsDialog)
        self.createBill.setGeometry(QtCore.QRect(30, 10, 120, 120))
        self.createBill.setMaximumSize(QtCore.QSize(120, 120))
        self.createBill.setStyleSheet("border:none;")
        self.createBill.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Images/write_bill.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.createBill.setIcon(icon)
        self.createBill.setIconSize(QtCore.QSize(100, 100))
        self.createBill.setObjectName("createBill")
        self.viewBills = QtWidgets.QPushButton(billsDialog)
        self.viewBills.setGeometry(QtCore.QRect(210, 10, 120, 120))
        self.viewBills.setMaximumSize(QtCore.QSize(120, 120))
        self.viewBills.setStyleSheet("border:none;")
        self.viewBills.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../Images/search_prescription.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.viewBills.setIcon(icon1)
        self.viewBills.setIconSize(QtCore.QSize(100, 100))
        self.viewBills.setObjectName("viewBills")
        self.createBillLabel = QtWidgets.QLabel(billsDialog)
        self.createBillLabel.setGeometry(QtCore.QRect(-10, 120, 180, 40))
        self.createBillLabel.setMinimumSize(QtCore.QSize(180, 40))
        self.createBillLabel.setMaximumSize(QtCore.QSize(180, 40))
        self.createBillLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.createBillLabel.setObjectName("createBillLabel")
        self.viewBillsLabel = QtWidgets.QLabel(billsDialog)
        self.viewBillsLabel.setGeometry(QtCore.QRect(170, 120, 180, 40))
        self.viewBillsLabel.setMinimumSize(QtCore.QSize(180, 40))
        self.viewBillsLabel.setMaximumSize(QtCore.QSize(180, 40))
        self.viewBillsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.viewBillsLabel.setObjectName("viewBillsLabel")

        self.retranslateUi(billsDialog)
        QtCore.QMetaObject.connectSlotsByName(billsDialog)

    def retranslateUi(self, billsDialog):
        _translate = QtCore.QCoreApplication.translate
        billsDialog.setWindowTitle(_translate("billsDialog", "Bills"))
        self.createBillLabel.setText(_translate("billsDialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">Create Bill</span></p></body></html>"))
        self.viewBillsLabel.setText(_translate("billsDialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">View Bills</span></p></body></html>"))

