# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEvent.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_addEvent(object):
    def setupUi(self, addEvent):
        addEvent.setObjectName("addEvent")
        addEvent.resize(750, 492)
        self.addButton = QtWidgets.QPushButton(addEvent)
        self.addButton.setGeometry(QtCore.QRect(300, 420, 131, 41))
        self.addButton.setObjectName("addButton")
        self.title = QtWidgets.QLabel(addEvent)
        self.title.setGeometry(QtCore.QRect(250, 0, 261, 51))
        self.title.setObjectName("title")
        self.frame = QtWidgets.QFrame(addEvent)
        self.frame.setGeometry(QtCore.QRect(10, 60, 731, 341))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.eventNameLabel = QtWidgets.QLabel(self.frame)
        self.eventNameLabel.setGeometry(QtCore.QRect(30, 20, 101, 41))
        self.eventNameLabel.setObjectName("eventNameLabel")
        self.dateLabel = QtWidgets.QLabel(self.frame)
        self.dateLabel.setGeometry(QtCore.QRect(360, 80, 51, 31))
        self.dateLabel.setObjectName("dateLabel")
        self.venueLabel = QtWidgets.QLabel(self.frame)
        self.venueLabel.setGeometry(QtCore.QRect(360, 120, 51, 31))
        self.venueLabel.setObjectName("venueLabel")
        self.eventName = QtWidgets.QLineEdit(self.frame)
        self.eventName.setGeometry(QtCore.QRect(140, 20, 561, 41))
        self.eventName.setObjectName("eventName")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.frame)
        self.dateTimeEdit.setGeometry(QtCore.QRect(430, 80, 271, 27))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.venue = QtWidgets.QLineEdit(self.frame)
        self.venue.setGeometry(QtCore.QRect(430, 120, 271, 31))
        self.venue.setObjectName("venue")
        self.descriptionLabel = QtWidgets.QLabel(self.frame)
        self.descriptionLabel.setGeometry(QtCore.QRect(360, 160, 101, 31))
        self.descriptionLabel.setObjectName("descriptionLabel")
        self.uploadImage = QtWidgets.QPushButton(self.frame)
        self.uploadImage.setGeometry(QtCore.QRect(100, 280, 131, 41))
        self.uploadImage.setObjectName("uploadImage")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(30, 70, 271, 201))
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet("image: url(:/selectImage.png);\n"
"border-style:solid;\n"
"border-width:1px;\n"
"border-color: rgb(7, 7, 7);")
        self.widget.setObjectName("widget")
        self.description = QtWidgets.QTextBrowser(self.frame)
        self.description.setGeometry(QtCore.QRect(360, 190, 351, 141))
        self.description.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextSelectableByMouse)
        self.description.setObjectName("description")

        self.retranslateUi(addEvent)
        QtCore.QMetaObject.connectSlotsByName(addEvent)

    def retranslateUi(self, addEvent):
        _translate = QtCore.QCoreApplication.translate
        addEvent.setWindowTitle(_translate("addEvent", "Dialog"))
        self.addButton.setText(_translate("addEvent", "ADD"))
        self.title.setText(_translate("addEvent", "<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; font-weight:600; text-decoration: underline;\">Add Event</span></p></body></html>"))
        self.eventNameLabel.setText(_translate("addEvent", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Event Name</span></p></body></html>"))
        self.dateLabel.setText(_translate("addEvent", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Date</span></p></body></html>"))
        self.venueLabel.setText(_translate("addEvent", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Venue</span></p></body></html>"))
        self.descriptionLabel.setText(_translate("addEvent", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Description</span></p></body></html>"))
        self.uploadImage.setText(_translate("addEvent", "Upload Image"))

import img_rc
