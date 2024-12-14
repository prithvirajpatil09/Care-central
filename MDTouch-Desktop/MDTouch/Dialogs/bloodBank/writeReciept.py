
from PyQt5 import QtCore, QtGui, QtWidgets

class bloodReciept(object):
    def setup(self, bloodReciept,grandparent):
        bloodReciept.setObjectName("bloodReciept")
        bloodReciept.setWindowModality(QtCore.Qt.ApplicationModal)
        bloodReciept.resize(342, 307)
        self.frame = QtWidgets.QFrame(bloodReciept)
        self.frame.setGeometry(QtCore.QRect(10, 10, 321, 241))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.bloodBillingLabel = QtWidgets.QLabel(self.frame)
        self.bloodBillingLabel.setGeometry(QtCore.QRect(80, 0, 161, 41))
        self.bloodBillingLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.bloodBillingLabel.setObjectName("bloodBillingLabel")
        self.bloodTypeLabel = QtWidgets.QLabel(self.frame)
        self.bloodTypeLabel.setGeometry(QtCore.QRect(20, 120, 151, 41))
        self.bloodTypeLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.bloodTypeLabel.setObjectName("bloodTypeLabel")
        self.quantityLabel = QtWidgets.QLabel(self.frame)
        self.quantityLabel.setGeometry(QtCore.QRect(20, 180, 151, 41))
        self.quantityLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.quantityLabel.setObjectName("quantityLabel")
        self.quantity = QtWidgets.QLineEdit(self.frame)
        self.quantity.setGeometry(QtCore.QRect(180, 190, 101, 25))
        self.quantity.setObjectName("quantity")
        self.bloodTypeComboBox = QtWidgets.QComboBox(self.frame)
        self.bloodTypeComboBox.setGeometry(QtCore.QRect(180, 130, 101, 25))
        self.bloodTypeComboBox.setObjectName("bloodTypeComboBox")
        self.bloodTypeComboBox.addItem("")
        self.bloodTypeComboBox.addItem("")
        self.bloodTypeComboBox.addItem("")
        self.bloodTypeComboBox.addItem("")
        self.bloodTypeComboBox.addItem("")
        self.bloodTypeComboBox.addItem("")
        self.bloodTypeComboBox.addItem("")
        self.bloodTypeComboBox.addItem("")
        self.patientIDLabel = QtWidgets.QLabel(self.frame)
        self.patientIDLabel.setGeometry(QtCore.QRect(20, 60, 151, 41))
        self.patientIDLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.patientIDLabel.setObjectName("patientIDLabel")
        self.patientID = QtWidgets.QLineEdit(self.frame)
        self.patientID.setGeometry(QtCore.QRect(180, 70, 101, 25))
        self.patientID.setObjectName("patientID")
        self.addButton = QtWidgets.QPushButton(bloodReciept)
        self.addButton.setGeometry(QtCore.QRect(120, 270, 89, 25))
        self.addButton.setObjectName("addButton")

        self.retranslateUi(bloodReciept,grandparent)
        QtCore.QMetaObject.connectSlotsByName(bloodReciept)

    def retranslateUi(self, bloodReciept,grandparent):
        _translate = QtCore.QCoreApplication.translate
        bloodReciept.setWindowTitle(_translate("bloodReciept", "Blood Entry"))
        self.bloodBillingLabel.setText(_translate("bloodReciept", "<html><head/><body><p><span style=\" font-size:12pt; text-decoration: underline;\">Blood Reciept</span></p></body></html>"))
        self.bloodTypeLabel.setText(_translate("bloodReciept", "<html><head/><body><p>Blood Type :</p></body></html>"))
        self.quantityLabel.setText(_translate("bloodReciept", "<html><head/><body><p>Quantity :</p></body></html>"))
        self.bloodTypeComboBox.setItemText(0, _translate("bloodReciept", "A+"))
        self.bloodTypeComboBox.setItemText(1, _translate("bloodReciept", "A-"))
        self.bloodTypeComboBox.setItemText(2, _translate("bloodReciept", "B+"))
        self.bloodTypeComboBox.setItemText(3, _translate("bloodReciept", "B-"))
        self.bloodTypeComboBox.setItemText(4, _translate("bloodReciept", "AB+"))
        self.bloodTypeComboBox.setItemText(5, _translate("bloodReciept", "AB_"))
        self.bloodTypeComboBox.setItemText(6, _translate("bloodReciept", "O+"))
        self.bloodTypeComboBox.setItemText(7, _translate("bloodReciept", "O-"))
        self.patientIDLabel.setText(_translate("bloodReciept", "<html><head/><body><p>Patient ID:</p></body></html>"))
        self.addButton.setText(_translate("bloodReciept", "Add"))

        self.events(bloodReciept,grandparent)

    def events(self,parent,grandparent):
        pass


