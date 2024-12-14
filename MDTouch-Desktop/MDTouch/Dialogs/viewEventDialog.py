from PyQt5 import QtCore, QtGui, QtWidgets
from Dialogs.superadmin.Events.viewEvents import *
from Dialogs.superadmin.Events.myEventList import *
class viewEventDialog(object):
    def setup(self, viewEventDialog,type,userdata):
        self.type = type
        self.userdata = userdata
        viewEventDialog.setObjectName("viewEventDialog")
        viewEventDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        viewEventDialog.resize(484, 235)
        self.myEvents = QtWidgets.QPushButton(viewEventDialog)
        self.myEvents.setGeometry(QtCore.QRect(80, 10, 120, 120))
        self.myEvents.setMaximumSize(QtCore.QSize(120, 120))
        self.myEvents.setStyleSheet("border:none;")
        self.myEvents.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Images/add_event.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.myEvents.setIcon(icon)
        self.myEvents.setIconSize(QtCore.QSize(100, 100))
        self.myEvents.setObjectName("myEvents")
        self.allEvents = QtWidgets.QPushButton(viewEventDialog)
        self.allEvents.setGeometry(QtCore.QRect(280, 10, 120, 120))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.allEvents.sizePolicy().hasHeightForWidth())
        self.allEvents.setSizePolicy(sizePolicy)
        self.allEvents.setMaximumSize(QtCore.QSize(120, 120))
        self.allEvents.setStyleSheet("border:none;")
        self.allEvents.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../Images/search_hospital.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.allEvents.setIcon(icon1)
        self.allEvents.setIconSize(QtCore.QSize(100, 100))
        self.allEvents.setObjectName("allEvents")
        self.allEventsLabel = QtWidgets.QLabel(viewEventDialog)
        self.allEventsLabel.setGeometry(QtCore.QRect(280, 120, 126, 78))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.allEventsLabel.sizePolicy().hasHeightForWidth())
        self.allEventsLabel.setSizePolicy(sizePolicy)
        self.allEventsLabel.setObjectName("allEventsLabel")
        self.myEventLabel = QtWidgets.QLabel(viewEventDialog)
        self.myEventLabel.setGeometry(QtCore.QRect(70, 120, 126, 78))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.myEventLabel.sizePolicy().hasHeightForWidth())
        self.myEventLabel.setSizePolicy(sizePolicy)
        self.myEventLabel.setObjectName("myEventLabel")

        self.retranslateUi(viewEventDialog)
        QtCore.QMetaObject.connectSlotsByName(viewEventDialog)

    def retranslateUi(self, viewEventDialog):
        _translate = QtCore.QCoreApplication.translate
        viewEventDialog.setWindowTitle(_translate("viewEventDialog", "Profiles"))
        self.allEventsLabel.setText(_translate("viewEventDialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; font-weight:600; text-decoration: underline;\">All</span></p><p align=\"center\"><span style=\" font-size:15pt; font-weight:600; text-decoration: underline;\">Events</span></p></body></html>"))
        self.myEventLabel.setText(_translate("viewEventDialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; font-weight:600; text-decoration: underline;\">My</span></p><p align=\"center\"><span style=\" font-size:15pt; font-weight:600; text-decoration: underline;\">Events</span></p><p align=\"center\"><br/></p></body></html>"))
        self.allEvents.clicked.connect(lambda : self.clickOnAllEvents(viewEventDialog))
        self.myEvents.clicked.connect(lambda : self.clickOnMyEvents(viewEventDialog))

    def clickOnAllEvents(self,parent):
        self.window = QDialog()
        self.dialog = viewEvent()
        self.dialog.setup(self.window,self.type)
        self.window.setModal(True)
        self.window.show()

    def clickOnMyEvents(self,parent):
        self.window = QDialog()
        self.dialog = myEventList()
        self.dialog.setup(self.window,self.type,self.userdata)
        self.window.setModal(True)
        self.window.show()

