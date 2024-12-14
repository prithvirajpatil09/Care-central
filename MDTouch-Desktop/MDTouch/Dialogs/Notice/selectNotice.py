from PyQt5 import QtCore, QtGui, QtWidgets
from Dialogs.messageBox import *
from Dialogs.Notice.noticeProfile import *
from Dialogs.Notice.deleteNotice import *
from PyQt5.QtWidgets import *

class selectNotice(object):
    def setup(self, selectNotice):
        selectNotice.setObjectName("selectNotice")
        selectNotice.resize(209, 180)
        selectNotice.setWindowTitle("")
        self.title = QtWidgets.QLabel(selectNotice)
        self.title.setGeometry(QtCore.QRect(-50, 0, 321, 51))
        self.title.setObjectName("title")
        self.removeButton = QtWidgets.QPushButton(selectNotice)
        self.removeButton.setGeometry(QtCore.QRect(60, 120, 80, 28))
        self.removeButton.setObjectName("removeButton")
        self.searchByID = QtWidgets.QLineEdit(selectNotice)
        self.searchByID.setGeometry(QtCore.QRect(10, 70, 191, 27))
        self.searchByID.setObjectName("searchByID")

        self.retranslateUi(selectNotice)
        QtCore.QMetaObject.connectSlotsByName(selectNotice)

    def retranslateUi(self, selectNotice):
        _translate = QtCore.QCoreApplication.translate
        self.title.setText(_translate("selectNotice", "<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; font-weight:600; text-decoration: underline;\">Select Notice</span></p></body></html>"))
        self.removeButton.setText(_translate("selectNotice", "SELECT"))
        self.searchByID.setPlaceholderText(_translate("selectNotice", "Enter Notice ID"))

        self.removeButton.clicked.connect(lambda : self.clickOnSelectButton(selectNotice))

    def clickOnSelectButton(self,parent):
        id = self.searchByID.text()
        if id == "" or (not(id.isdigit())):
            self.window = messageBox()
            self.window.infoBox("Invalid Id")
            return
        URL = "http://127.0.0.1:8000/MDTouch/api/notice/" + str(id)
        import requests
        r = requests.get(url=URL)
        l = r.json()
        if l == {"detail": "Not found."}:
            self.window = messageBox()
            self.window.infoBox("Not ID Found")
            return
        self.window = QDialog()
        self.dialog = deleteNotice()
        self.dialog.setup(self.window,l)
        self.window.setModal(True)
        self.window.show()


