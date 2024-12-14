# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'broadcast.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_broadcast(object):
    def setupUi(self, broadcast):
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
        self.message.setGeometry(QtCore.QRect(10, 200, 321, 141))
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

        self.retranslateUi(broadcast)
        QtCore.QMetaObject.connectSlotsByName(broadcast)

    def retranslateUi(self, broadcast):
        _translate = QtCore.QCoreApplication.translate
        broadcast.setWindowTitle(_translate("broadcast", " "))
        self.message.setPlaceholderText(_translate("broadcast", "Type your message here..."))
        self.broadcastButton.setText(_translate("broadcast", "SEND BROADCAST"))
        self.recipientsLabel.setText(_translate("broadcast", "<html><head/><body><p><span style=\" font-size:11pt;\">Recipients :</span></p></body></html>"))
        self.title.setText(_translate("broadcast", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">Broadcast Message</span></p></body></html>"))
        self.cityLabel.setText(_translate("broadcast", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">City : </span></p></body></html>"))
        self.stateLabel.setText(_translate("broadcast", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">State : </span></p></body></html>"))

