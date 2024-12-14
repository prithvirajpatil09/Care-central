from PyQt5 import QtCore, QtGui, QtWidgets
from Dialogs.messageBox import *

class deleteNotice(object):
    def setup(self, deleteNotice,data):
        self.data = data
        deleteNotice.setObjectName("deleteNotice")
        deleteNotice.resize(580, 477)
        self.frame = QtWidgets.QFrame(deleteNotice)
        self.frame.setGeometry(QtCore.QRect(10, 50, 561, 381))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.idLabel = QtWidgets.QLabel(self.frame)
        self.idLabel.setGeometry(QtCore.QRect(10, 10, 71, 41))
        self.idLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.idLabel.setObjectName("idLabel")
        self.titlelabel = QtWidgets.QLabel(self.frame)
        self.titlelabel.setGeometry(QtCore.QRect(10, 60, 91, 41))
        self.titlelabel.setObjectName("titlelabel")
        self.noticeLabel = QtWidgets.QLabel(self.frame)
        self.noticeLabel.setGeometry(QtCore.QRect(10, 110, 91, 41))
        self.noticeLabel.setObjectName("noticeLabel")
        self.id = QtWidgets.QLabel(self.frame)
        self.id.setGeometry(QtCore.QRect(90, 10, 91, 41))
        self.id.setObjectName("id")
        self.title = QtWidgets.QLabel(self.frame)
        self.title.setGeometry(QtCore.QRect(90, 60, 461, 41))
        self.title.setObjectName("title")
        self.notice = QtWidgets.QTextBrowser(self.frame)
        self.notice.setGeometry(QtCore.QRect(90, 120, 461, 251))
        self.notice.setObjectName("notice")
        self.dateLabel = QtWidgets.QLabel(self.frame)
        self.dateLabel.setGeometry(QtCore.QRect(230, 10, 161, 41))
        self.dateLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.dateLabel.setObjectName("dateLabel")
        self.date = QtWidgets.QLabel(self.frame)
        self.date.setGeometry(QtCore.QRect(400, 10, 151, 41))
        self.date.setObjectName("date")
        self.closeButton = QtWidgets.QPushButton(deleteNotice)
        self.closeButton.setGeometry(QtCore.QRect(480, 440, 89, 25))
        self.closeButton.setObjectName("closeButton")
        self.addNoticeLabel = QtWidgets.QLabel(deleteNotice)
        self.addNoticeLabel.setGeometry(QtCore.QRect(210, 0, 151, 41))
        self.addNoticeLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.addNoticeLabel.setObjectName("addNoticeLabel")

        self.retranslateUi(deleteNotice)
        QtCore.QMetaObject.connectSlotsByName(deleteNotice)

    def retranslateUi(self, deleteNotice):
        _translate = QtCore.QCoreApplication.translate
        deleteNotice.setWindowTitle(_translate("deleteNotice", "Notice"))
        self.idLabel.setText(_translate("deleteNotice", "<html><head/><body><p>Id : </p></body></html>"))
        self.titlelabel.setText(_translate("deleteNotice", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Title :</span></p></body></html>"))
        self.noticeLabel.setText(_translate("deleteNotice", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Notice  :</span></p></body></html>"))
        self.id.setText(_translate("deleteNotice", "<html><head/><body><p>ID</p></body></html>"))
        self.title.setText(_translate("deleteNotice", "<html><head/><body><p>Title</p></body></html>"))
        self.dateLabel.setText(_translate("deleteNotice", "<html><head/><body><p>Date Of Publish :</p></body></html>"))
        self.date.setText(_translate("deleteNotice", "<html><head/><body><p>29/09/2002</p></body></html>"))
        self.closeButton.setText(_translate("deleteNotice", "Delete"))
        self.addNoticeLabel.setText(_translate("deleteNotice", "<html><head/><body><p><span style=\" font-size:12pt; text-decoration: underline;\">Delete Notice</span></p></body></html>"))

        self.clickevent(deleteNotice)

    def clickevent(self,parent):
        print(self.data)
        self.id.setText(str(self.data["id"]))
        self.date.setText(str(self.data["date"])[:10])
        self.title.setText(self.data["title"])
        self.notice.setText(self.data["notice"])
        self.closeButton.clicked.connect(lambda : self.clickOnDeleteNotice(parent))

    def clickOnDeleteNotice(self,parent):
        self.window = messageBox()
        self.window.infoBox("Notice is deleted")
        parent.close()
        import requests
        URL = "http://127.0.0.1:8000/MDTouch/api/notice/" + str(self.data["id"])
        r = requests.delete(url = URL)


