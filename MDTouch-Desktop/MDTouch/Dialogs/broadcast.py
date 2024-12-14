from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Pages.caller import *
from Data.States import *
from Dialogs.messageBox import *


class broadcast():

    def setup(self, broadcast, callerID):
        print(callerID)
        broadcast.setObjectName("broadcast")
        broadcast.resize(342, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(broadcast.sizePolicy().hasHeightForWidth())
        broadcast.setSizePolicy(sizePolicy)
        broadcast.setMinimumSize(QtCore.QSize(342, 400))
        broadcast.setMaximumSize(QtCore.QSize(342, 400))
        self.message = QtWidgets.QTextBrowser(broadcast)
        self.message.setGeometry(QtCore.QRect(10, 230, 321, 115))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.message.sizePolicy().hasHeightForWidth())
        self.message.setSizePolicy(sizePolicy)
        self.message.setStyleSheet("font-size:12pt;")
        self.message.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextSelectableByMouse)
        self.message.setObjectName("message")
        self.broadcastButton = QtWidgets.QPushButton(broadcast)
        self.broadcastButton.setGeometry(QtCore.QRect(100, 350, 141, 31))
        self.broadcastButton.setObjectName("broadcastButton")
        self.recipientsComboBox = QtWidgets.QComboBox(broadcast)
        self.recipientsComboBox.setGeometry(QtCore.QRect(130, 160, 201, 27))
        self.titleLabel = QLabel(broadcast)
        self.titleLabel.setGeometry(QRect(10,193,101,31))
        self.titleInput = QLineEdit(broadcast)
        self.titleInput.setPlaceholderText("Enter Title Of the Message")
        self.titleInput.setGeometry(QRect(63,195,269,27))
        self.recipientsComboBox.setObjectName("recipientsComboBox")
        self.recipientsLabel = QtWidgets.QLabel(broadcast)
        self.recipientsLabel.setGeometry(QtCore.QRect(10, 160, 101, 31))
        self.recipientsLabel.setStyleSheet("font-size: 10pt;\n"
"font-weight:bold;")
        self.recipientsLabel.setObjectName("recipientsLabel")
        self.title = QtWidgets.QLabel(broadcast)
        self.title.setGeometry(QtCore.QRect(50, 10, 231, 41))
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.cityLabel = QtWidgets.QLabel(broadcast)
        self.cityLabel.setGeometry(QtCore.QRect(10, 110, 111, 31))
        self.cityLabel.setObjectName("cityLabel")
        self.stateLabel = QtWidgets.QLabel(broadcast)
        self.stateLabel.setGeometry(QtCore.QRect(10, 60, 111, 31))
        self.stateLabel.setObjectName("stateLabel")
        self.cityComboBox = QtWidgets.QComboBox(broadcast)
        self.cityComboBox.setGeometry(QtCore.QRect(130, 110, 201, 27))
        self.cityComboBox.setObjectName("cityComboBox")
        self.stateComboBox = QtWidgets.QComboBox(broadcast)
        self.stateComboBox.setGeometry(QtCore.QRect(130, 60, 201, 27))
        self.stateComboBox.setObjectName("stateComboBox")

        self.retranslateUi(broadcast,callerID)
        QtCore.QMetaObject.connectSlotsByName(broadcast)

    def retranslateUi(self, broadcast,callerID):
        _translate = QtCore.QCoreApplication.translate
        broadcast.setWindowTitle(_translate("broadcast", " "))
        self.message.setPlaceholderText(_translate("broadcast", "Type your message here..."))
        self.broadcastButton.setText(_translate("broadcast", "SEND BROADCAST"))
        self.recipientsLabel.setText(_translate("broadcast", "<html><head/><body><p><span style=\" font-size:11pt;\">Recipients :</span></p></body></html>"))
        self.titleLabel.setText(_translate("broadcast", "<html><head/><body><p><span style=\" font-size:11pt; font-weight: 600\">Title :</span></p></body></html>"))
        self.title.setText(_translate("broadcast", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">Broadcast Message</span></p></body></html>"))
        self.cityLabel.setText(_translate("broadcast", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">City : </span></p></body></html>"))
        self.stateLabel.setText(_translate("broadcast", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">State : </span></p></body></html>"))
        callerID = str(callerID).split('.')[-1]
        self.recipientsComboBox.addItem("All " + str(callerID))
        self.clickEvents(broadcast,callerID)

    def clickEvents(self, parent,callerId):
        self.stateAddFunction(parent)
        self.broadcastButton.clicked.connect(lambda : self.clickOnBroadcastButton(parent,callerId))

    def stateAddFunction(self,parent):
        self.stateComboBox.addItem("All States")
        for i in states.values():
            self.stateComboBox.addItem(i)
        self.cityComboBox.addItem("All Cities")
        for i in cities["Andhra Pradesh"]:
            self.cityComboBox.addItem(i)
        self.stateComboBox.currentIndexChanged.connect(lambda : self.cityAddFunction(parent))

    def cityAddFunction(self,parent):
        state = self.stateComboBox.currentText()

        while self.cityComboBox.count() > 1:
            self.cityComboBox.removeItem(0)
        for i in cities[state]:
            self.cityComboBox.addItem(i)
    def clickOnBroadcastButton(self,parent,callerId):

        if self.message.toPlainText() == "" :
            self.dialog = messageBox()
            self.dialog.infoBox("Empty Message")
            return
        if self.titleInput.text() == "":
            self.dialog = messageBox()
            self.dialog.infoBox("Empty Title")
            return

        state = self.stateComboBox.currentText()
        city = self.cityComboBox.currentText()
        title = self.titleInput.text()
        message =str(self.message.toPlainText())
        import requests
        URL = "http://127.0.0.1:8000/api/broadcast/"

        # Yaha pae sendto ko chnage karna hai callerId se
        data = {
            "title" : title,
            "message" : message,
            "sendto" : 1,
            "state" : state,
            "city" : city,
        }
        r = requests.post(url=URL,data=data)
        print(r.json())
        parent.close()
        self.dialog = messageBox()
        self.dialog.infoBox("The message has been broadcasted to all " + str(callerId))



