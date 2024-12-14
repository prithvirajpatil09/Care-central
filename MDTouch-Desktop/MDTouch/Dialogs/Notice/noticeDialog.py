
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from Dialogs.Notice.addNotice import *
from Dialogs.Notice.NoticeList import *
from Dialogs.Notice.selectNotice import *

class noticeDialog(object):
    def setup(self, noticeDialog):
        noticeDialog.setObjectName("noticeDialog")
        noticeDialog.resize(484, 235)
        self.deleteNotice = QtWidgets.QPushButton(noticeDialog)
        self.deleteNotice.setGeometry(QtCore.QRect(350, 10, 120, 120))
        self.deleteNotice.setMaximumSize(QtCore.QSize(120, 120))
        self.deleteNotice.setStyleSheet("border:none;")
        self.deleteNotice.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../Images/delete_event.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteNotice.setIcon(icon)
        self.deleteNotice.setIconSize(QtCore.QSize(100, 100))
        self.deleteNotice.setObjectName("deleteNotice")
        self.addNotice = QtWidgets.QPushButton(noticeDialog)
        self.addNotice.setGeometry(QtCore.QRect(30, 10, 120, 120))
        self.addNotice.setMaximumSize(QtCore.QSize(120, 120))
        self.addNotice.setStyleSheet("border:none;")
        self.addNotice.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../Images/add_event.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addNotice.setIcon(icon1)
        self.addNotice.setIconSize(QtCore.QSize(100, 100))
        self.addNotice.setObjectName("addNotice")
        self.viewNotice = QtWidgets.QPushButton(noticeDialog)
        self.viewNotice.setGeometry(QtCore.QRect(190, 10, 120, 120))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.viewNotice.sizePolicy().hasHeightForWidth())
        self.viewNotice.setSizePolicy(sizePolicy)
        self.viewNotice.setMaximumSize(QtCore.QSize(120, 120))
        self.viewNotice.setStyleSheet("border:none;")
        self.viewNotice.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../../Images/search_hospital.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.viewNotice.setIcon(icon2)
        self.viewNotice.setIconSize(QtCore.QSize(100, 100))
        self.viewNotice.setObjectName("viewNotice")
        self.deleteNoticeLabel = QtWidgets.QLabel(noticeDialog)
        self.deleteNoticeLabel.setGeometry(QtCore.QRect(350, 120, 112, 78))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteNoticeLabel.sizePolicy().hasHeightForWidth())
        self.deleteNoticeLabel.setSizePolicy(sizePolicy)
        self.deleteNoticeLabel.setObjectName("deleteNoticeLabel")
        self.addNoticeLabel = QtWidgets.QLabel(noticeDialog)
        self.addNoticeLabel.setGeometry(QtCore.QRect(20, 120, 126, 78))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addNoticeLabel.sizePolicy().hasHeightForWidth())
        self.addNoticeLabel.setSizePolicy(sizePolicy)
        self.addNoticeLabel.setObjectName("addNoticeLabel")
        self.viewNoticeLabel = QtWidgets.QLabel(noticeDialog)
        self.viewNoticeLabel.setGeometry(QtCore.QRect(190, 120, 126, 78))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.viewNoticeLabel.sizePolicy().hasHeightForWidth())
        self.viewNoticeLabel.setSizePolicy(sizePolicy)
        self.viewNoticeLabel.setObjectName("viewNoticeLabel")

        self.retranslateUi(noticeDialog)
        QtCore.QMetaObject.connectSlotsByName(noticeDialog)

    def retranslateUi(self, noticeDialog):
        _translate = QtCore.QCoreApplication.translate
        noticeDialog.setWindowTitle(_translate("noticeDialog", "Notice"))
        self.deleteNoticeLabel.setText(_translate("noticeDialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; font-weight:600; text-decoration: underline;\">Delete<br/>Notice</span></p></body></html>"))
        self.addNoticeLabel.setText(_translate("noticeDialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; font-weight:600; text-decoration: underline;\">Add<br/>Notice</span></p></body></html>"))
        self.viewNoticeLabel.setText(_translate("noticeDialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; font-weight:600; text-decoration: underline;\">View<br/>Notice</span></p></body></html>"))
        self.clickevent(noticeDialog)

    def clickevent(self,parent):
        self.addNotice.clicked.connect(lambda : self.clickAddNotice(parent))
        self.viewNotice.clicked.connect(lambda : self.clickViewNotice(parent))
        self.deleteNotice.clicked.connect(lambda : self.clickDeleteNotice(parent))


    def clickAddNotice(self,parent):
        self.window = QDialog()
        self.dialog = addNotice()
        self.dialog.setup(self.window)
        self.window.setModal(True)
        self.window.show()
    def clickViewNotice(self,parent):
        self.window = QDialog()
        self.dialog = noticeList()
        self.dialog.setup(self.window)
        self.window.setModal(True)
        self.window.show()

    def clickDeleteNotice(self,parent):
        self.window = QDialog()
        self.dialog = selectNotice()
        self.dialog.setup(self.window)
        self.window.setModal(True)
        self.window.show()