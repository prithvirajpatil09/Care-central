# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'deleteEvent.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_deleteEvent(object):
    def setupUi(self, deleteEvent):
        deleteEvent.setObjectName("deleteEvent")
        deleteEvent.resize(610, 480)
        self.title = QtWidgets.QLabel(deleteEvent)
        self.title.setGeometry(QtCore.QRect(170, 0, 261, 51))
        self.title.setObjectName("title")
        self.frame = QtWidgets.QFrame(deleteEvent)
        self.frame.setGeometry(QtCore.QRect(10, 60, 591, 341))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(10, 60, 271, 201))
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet("image: url(:/sample_event.png);\n"
"border-style:solid;\n"
"border-width:1px;\n"
"border-color: rgb(7, 7, 7);")
        self.widget.setObjectName("widget")
        self.nameLabel = QtWidgets.QLabel(self.frame)
        self.nameLabel.setGeometry(QtCore.QRect(210, 10, 91, 31))
        self.nameLabel.setObjectName("nameLabel")
        self.name = QtWidgets.QLabel(self.frame)
        self.name.setGeometry(QtCore.QRect(290, 10, 571, 31))
        self.name.setStyleSheet("font-size:12pt;")
        self.name.setObjectName("name")
        self.creatorLabel = QtWidgets.QLabel(self.frame)
        self.creatorLabel.setGeometry(QtCore.QRect(20, 290, 101, 31))
        self.creatorLabel.setObjectName("creatorLabel")
        self.descriptionLabel = QtWidgets.QLabel(self.frame)
        self.descriptionLabel.setGeometry(QtCore.QRect(310, 130, 131, 41))
        self.descriptionLabel.setObjectName("descriptionLabel")
        self.dateLabel = QtWidgets.QLabel(self.frame)
        self.dateLabel.setGeometry(QtCore.QRect(310, 60, 71, 31))
        self.dateLabel.setObjectName("dateLabel")
        self.venueLabel = QtWidgets.QLabel(self.frame)
        self.venueLabel.setGeometry(QtCore.QRect(310, 100, 81, 31))
        self.venueLabel.setObjectName("venueLabel")
        self.creator = QtWidgets.QLabel(self.frame)
        self.creator.setGeometry(QtCore.QRect(130, 290, 181, 31))
        self.creator.setStyleSheet("font-size:12pt;")
        self.creator.setObjectName("creator")
        self.date = QtWidgets.QLabel(self.frame)
        self.date.setGeometry(QtCore.QRect(400, 60, 221, 31))
        self.date.setStyleSheet("font-size:12pt;")
        self.date.setObjectName("date")
        self.venue = QtWidgets.QLabel(self.frame)
        self.venue.setGeometry(QtCore.QRect(400, 100, 221, 31))
        self.venue.setStyleSheet("font-size:12pt;")
        self.venue.setObjectName("venue")
        self.nameLabel_2 = QtWidgets.QLabel(self.frame)
        self.nameLabel_2.setGeometry(QtCore.QRect(20, 10, 91, 31))
        self.nameLabel_2.setObjectName("nameLabel_2")
        self.date_2 = QtWidgets.QLabel(self.frame)
        self.date_2.setGeometry(QtCore.QRect(120, 10, 91, 31))
        self.date_2.setStyleSheet("font-size:12pt;")
        self.date_2.setObjectName("date_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser.setGeometry(QtCore.QRect(310, 170, 261, 151))
        self.textBrowser.setStyleSheet("background-color:transparent;\n"
"border:none;")
        self.textBrowser.setObjectName("textBrowser")
        self.deleteButton = QtWidgets.QPushButton(deleteEvent)
        self.deleteButton.setGeometry(QtCore.QRect(250, 420, 131, 41))
        self.deleteButton.setObjectName("deleteButton")

        self.retranslateUi(deleteEvent)
        QtCore.QMetaObject.connectSlotsByName(deleteEvent)

    def retranslateUi(self, deleteEvent):
        _translate = QtCore.QCoreApplication.translate
        deleteEvent.setWindowTitle(_translate("deleteEvent", " "))
        self.title.setText(_translate("deleteEvent", "<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; font-weight:600; text-decoration: underline;\">Delete Event</span></p></body></html>"))
        self.nameLabel.setText(_translate("deleteEvent", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Name :</span></p></body></html>"))
        self.name.setText(_translate("deleteEvent", "event_name"))
        self.creatorLabel.setText(_translate("deleteEvent", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Creator : </span></p></body></html>"))
        self.descriptionLabel.setText(_translate("deleteEvent", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Description :</span></p></body></html>"))
        self.dateLabel.setText(_translate("deleteEvent", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Date : </span></p></body></html>"))
        self.venueLabel.setText(_translate("deleteEvent", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Venue : </span></p></body></html>"))
        self.creator.setText(_translate("deleteEvent", "creator"))
        self.date.setText(_translate("deleteEvent", "date"))
        self.venue.setText(_translate("deleteEvent", "venue"))
        self.nameLabel_2.setText(_translate("deleteEvent", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Event ID : </span></p></body></html>"))
        self.date_2.setText(_translate("deleteEvent", "event_id"))
        self.textBrowser.setHtml(_translate("deleteEvent", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser.setPlaceholderText(_translate("deleteEvent", "This area is used to store description."))
        self.deleteButton.setText(_translate("deleteEvent", "Delete"))

import img_rc
