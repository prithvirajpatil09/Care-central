from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Dialogs.superadmin.Events.addEvent import *
from Dialogs.superadmin.Events.deleteEvent import *
from Dialogs.superadmin.Events.selectEvent import *
from Dialogs.viewEventDialog import *
class eventsDialog(object):
    def setup(self, eventsDialog,type = None,userdata = None):
        self.type = type
        self.userdata = userdata
        eventsDialog.setObjectName("eventsDialog")
        eventsDialog.resize(484, 235)
        self.deleteEvent = QtWidgets.QPushButton(eventsDialog)
        self.deleteEvent.setGeometry(QtCore.QRect(350, 10, 120, 120))
        self.deleteEvent.setMaximumSize(QtCore.QSize(120, 120))
        self.deleteEvent.setStyleSheet("border:none;")
        self.deleteEvent.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Images/delete_event.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteEvent.setIcon(icon)
        self.deleteEvent.setIconSize(QtCore.QSize(100, 100))
        self.deleteEvent.setObjectName("deleteEvent")
        self.addEvent = QtWidgets.QPushButton(eventsDialog)
        self.addEvent.setGeometry(QtCore.QRect(30, 10, 120, 120))
        self.addEvent.setMaximumSize(QtCore.QSize(120, 120))
        self.addEvent.setStyleSheet("border:none;")
        self.addEvent.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../Images/add_event.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addEvent.setIcon(icon1)
        self.addEvent.setIconSize(QtCore.QSize(100, 100))
        self.addEvent.setObjectName("addEvent")
        self.viewEvents = QtWidgets.QPushButton(eventsDialog)
        self.viewEvents.setGeometry(QtCore.QRect(190, 10, 120, 120))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.viewEvents.sizePolicy().hasHeightForWidth())
        self.viewEvents.setSizePolicy(sizePolicy)
        self.viewEvents.setMaximumSize(QtCore.QSize(120, 120))
        self.viewEvents.setStyleSheet("border:none;")
        self.viewEvents.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../Images/search_hospital.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.viewEvents.setIcon(icon2)
        self.viewEvents.setIconSize(QtCore.QSize(100, 100))
        self.viewEvents.setObjectName("viewEvents")
        self.deleteEventLabel = QtWidgets.QLabel(eventsDialog)
        self.deleteEventLabel.setGeometry(QtCore.QRect(350, 120, 112, 78))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteEventLabel.sizePolicy().hasHeightForWidth())
        self.deleteEventLabel.setSizePolicy(sizePolicy)
        self.deleteEventLabel.setObjectName("deleteEventLabel")
        self.addEventLabel = QtWidgets.QLabel(eventsDialog)
        self.addEventLabel.setGeometry(QtCore.QRect(20, 120, 126, 78))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addEventLabel.sizePolicy().hasHeightForWidth())
        self.addEventLabel.setSizePolicy(sizePolicy)
        self.addEventLabel.setObjectName("addEventLabel")
        self.viewEventsLabel = QtWidgets.QLabel(eventsDialog)
        self.viewEventsLabel.setGeometry(QtCore.QRect(190, 120, 126, 78))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.viewEventsLabel.sizePolicy().hasHeightForWidth())
        self.viewEventsLabel.setSizePolicy(sizePolicy)
        self.viewEventsLabel.setObjectName("viewEventsLabel")

        self.retranslateUi(eventsDialog)
        QtCore.QMetaObject.connectSlotsByName(eventsDialog)

    def retranslateUi(self, eventsDialog):
        _translate = QtCore.QCoreApplication.translate
        eventsDialog.setWindowTitle(_translate("eventsDialog", "Events"))
        self.deleteEventLabel.setText(_translate("eventsDialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; font-weight:600; text-decoration: underline;\">Delete<br>Event</span></p></body></html>"))
        self.addEventLabel.setText(_translate("eventsDialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; font-weight:600; text-decoration: underline;\">Add<br>Event</span></p></body></html>"))
        self.viewEventsLabel.setText(_translate("eventsDialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; font-weight:600; text-decoration: underline;\">View<br>Events</span></p></body></html>"))
        self.clickEvents(eventsDialog)

    def clickEvents(self,parent):
        self.addEvent.clicked.connect(lambda : self.clickOnAddEvent(parent))
        self.deleteEvent.clicked.connect(lambda : self.clickOnDeleteEvent(parent))
        self.viewEvents.clicked.connect(lambda : self.clickOnViewEvent(parent))

    def clickOnAddEvent(self,parent):
        self.window = QDialog()
        self.dialog = addEvent()
        self.dialog.setup(self.window,'H',self.userdata)
        self.window.setModal(True)
        self.window.show()
    def clickOnDeleteEvent(self,parent):
        self.window = QDialog()
        self.dialog = selectEvent()
        self.dialog.setup(self.window,'H',self.userdata)
        self.window.setModal(True)
        self.window.show()

    def clickOnViewEvent(self,parent):
        self.window = QDialog()
        self.dialog = viewEventDialog()
        self.dialog.setup(self.window,'H',self.userdata)
        self.window.setModal(True)
        self.window.show()

