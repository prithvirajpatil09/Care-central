from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from Dialogs.messageBox import *

class addNotice(object):
    def setup(self, addNotice):
        addNotice.setObjectName("addNotice")
        addNotice.resize(580, 439)
        self.frame = QtWidgets.QFrame(addNotice)
        self.frame.setGeometry(QtCore.QRect(10, 10, 561, 381))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.addNoticeLabel = QtWidgets.QLabel(self.frame)
        self.addNoticeLabel.setGeometry(QtCore.QRect(230, 0, 131, 41))
        self.addNoticeLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.addNoticeLabel.setObjectName("addNoticeLabel")
        self.titlelabel = QtWidgets.QLabel(self.frame)
        self.titlelabel.setGeometry(QtCore.QRect(20, 60, 91, 41))
        self.titlelabel.setObjectName("titlelabel")
        self.title = QtWidgets.QLineEdit(self.frame)
        self.title.setGeometry(QtCore.QRect(90, 70, 451, 25))
        self.title.setText("")
        self.title.setObjectName("title")
        self.notice = QtWidgets.QTextEdit(self.frame)
        self.notice.setGeometry(QtCore.QRect(90, 110, 451, 261))
        self.notice.setObjectName("notice")
        self.noticeLabel = QtWidgets.QLabel(self.frame)
        self.noticeLabel.setGeometry(QtCore.QRect(10, 110, 91, 41))
        self.noticeLabel.setObjectName("noticeLabel")
        self.publishButton = QtWidgets.QPushButton(addNotice)
        self.publishButton.setGeometry(QtCore.QRect(240, 410, 89, 25))
        self.publishButton.setObjectName("publishButton")

        self.retranslateUi(addNotice)
        QtCore.QMetaObject.connectSlotsByName(addNotice)

    def retranslateUi(self, addNotice):
        _translate = QtCore.QCoreApplication.translate
        addNotice.setWindowTitle(_translate("addNotice", "Add Notice"))
        self.addNoticeLabel.setText(_translate("addNotice", "<html><head/><body><p><span style=\" text-decoration: underline;\">Add Notice</span></p></body></html>"))
        self.titlelabel.setText(_translate("addNotice", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Title :</span></p></body></html>"))
        self.noticeLabel.setText(_translate("addNotice", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Notice  :</span></p></body></html>"))
        self.publishButton.setText(_translate("addNotice", "Publish"))
        self.events(addNotice)

    def events(self,parent):
        self.publishButton.clicked.connect(lambda : self.clickOnPublishButton(parent))

    def clickOnPublishButton(self,parent):
        title = self.title.text()
        notice = self.notice.toPlainText()
        if title == "" or len(notice) < 10:
            self.window = messageBox()
            self.window.infoBox("Please Provide Sufficient Information")
            return
        data = {
            "title" : title,
            "notice" : notice
        }
        URL = "http://127.0.0.1:8000/MDTouch/api/notice/"
        r = requests.post(url=URL,data=data)
        print(r.json())
        self.window = messageBox()
        self.window.infoBox("Event Created")
        parent.close()


