from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class eventProfile(object):
    def setup(self, eventProfile,eventData= None):
        self.eventdata = eventData
        eventProfile.setObjectName("eventProfile")
        eventProfile.resize(613, 422)
        eventProfile.setStyleSheet("")
        self.frame = QtWidgets.QFrame(eventProfile)
        self.frame.setGeometry(QtCore.QRect(10, 20, 591, 341))
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
        self.eventIDLabel = QtWidgets.QLabel(self.frame)
        self.eventIDLabel.setGeometry(QtCore.QRect(20, 10, 91, 31))
        self.eventIDLabel.setObjectName("eventIDLabel")
        self.eventID = QtWidgets.QLabel(self.frame)
        self.eventID.setGeometry(QtCore.QRect(120, 10, 91, 31))
        self.eventID.setStyleSheet("font-size:12pt;")
        self.eventID.setObjectName("eventID")
        self.textBrowser = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser.setGeometry(QtCore.QRect(310, 170, 261, 151))
        self.textBrowser.setStyleSheet("background-color:transparent;\n"
"border:none;")
        self.textBrowser.setObjectName("textBrowser")
        self.OKButton = QtWidgets.QPushButton(eventProfile)
        self.OKButton.setGeometry(QtCore.QRect(510, 380, 80, 28))
        self.OKButton.setObjectName("OKButton")

        self.retranslateUi(eventProfile)
        QtCore.QMetaObject.connectSlotsByName(eventProfile)

    def retranslateUi(self, eventProfile):
        _translate = QtCore.QCoreApplication.translate
        eventProfile.setWindowTitle(_translate("eventProfile", "Event Profile"))
        self.nameLabel.setText(_translate("eventProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Name :</span></p></body></html>"))
        self.name.setText(_translate("eventProfile", "event_name"))
        self.creatorLabel.setText(_translate("eventProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Creator : </span></p></body></html>"))
        self.descriptionLabel.setText(_translate("eventProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Description :</span></p></body></html>"))
        self.dateLabel.setText(_translate("eventProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Date : </span></p></body></html>"))
        self.venueLabel.setText(_translate("eventProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Venue : </span></p></body></html>"))
        self.creator.setText(_translate("eventProfile", "creator"))
        self.date.setText(_translate("eventProfile", "date"))
        self.venue.setText(_translate("eventProfile", "venue"))
        self.eventIDLabel.setText(_translate("eventProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Event ID : </span></p></body></html>"))
        self.eventID.setText(_translate("eventProfile", "event_id"))
        self.textBrowser.setHtml(_translate("eventProfile", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser.setPlaceholderText(_translate("eventProfile", "This area is used to store description."))
        self.OKButton.setText(_translate("eventProfile", "OK"))


        self.OKButton.clicked.connect(lambda: eventProfile.close())
        self.clickevent(eventProfile)

    def clickevent(self,parent):
        self.eventID.setText(str(self.eventdata["id"]))
        self.venue.setText(self.eventdata["eventlocation"])
        self.date.setText(str(self.eventdata["dateofevent"]))
        self.name.setText(self.eventdata["title"])
        self.textBrowser.setText(self.eventdata["description"])
        if self.eventdata["hospitalid"]:
            self.creator.setText("Hospital Id : " +str(self.eventdata["hospitalid"]))
        elif self.eventdata["bloodbankid"]:
            self.creator.setText("Blood BankCentre Id : " + str(self.eventdata["bloodbankid"]))
        elif self.eventdata["dispensaryid"]:
            self.creator.setText("Dispensary Id : " + str(self.eventdata["dispensaryid"]))
        elif self.eventdata["testcentreid"]:
            self.creator.setText("Test Center Id : " + str(self.eventdata["testcentreid"]))
        else :
            self.creator.setText("SuperAdmin")
