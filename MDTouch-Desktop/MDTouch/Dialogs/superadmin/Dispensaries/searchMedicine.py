

from PyQt5 import QtCore, QtGui, QtWidgets

class searchMedicine(object):
    def setup(self, searchMedicine):
        searchMedicine.setObjectName("searchMedicine")
        searchMedicine.resize(640, 539)
        self.frame = QtWidgets.QFrame(searchMedicine)
        self.frame.setGeometry(QtCore.QRect(10, 50, 621, 421))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(10, 41, 601, 371))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.searchButton = QtWidgets.QPushButton(self.frame)
        self.searchButton.setGeometry(QtCore.QRect(440, 10, 171, 25))
        self.searchButton.setObjectName("searchButton")
        self.text = QtWidgets.QLineEdit(self.frame)
        self.text.setGeometry(QtCore.QRect(10, 10, 421, 25))
        self.text.setObjectName("text")
        self.okbutton = QtWidgets.QPushButton(searchMedicine)
        self.okbutton.setGeometry(QtCore.QRect(260, 480, 89, 25))
        self.okbutton.setObjectName("okbutton")
        self.titleLabel = QtWidgets.QLabel(searchMedicine)
        self.titleLabel.setGeometry(QtCore.QRect(160, 0, 301, 41))
        self.titleLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.titleLabel.setObjectName("titleLabel")

        self.retranslateUi(searchMedicine)
        QtCore.QMetaObject.connectSlotsByName(searchMedicine)

    def retranslateUi(self, searchMedicine):
        _translate = QtCore.QCoreApplication.translate
        searchMedicine.setWindowTitle(_translate("searchMedicine", "Medicine"))
        self.searchButton.setText(_translate("searchMedicine", "Search"))
        self.text.setPlaceholderText(_translate("searchMedicine", "Enter Medicine Name"))
        self.okbutton.setText(_translate("searchMedicine", "close"))
        self.titleLabel.setText(_translate("searchMedicine", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; text-decoration: underline;\">Search Medicine</span></p></body></html>"))

