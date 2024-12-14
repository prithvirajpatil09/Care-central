# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'deleteNotice.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(580, 477)
        self.frame = QtWidgets.QFrame(Form)
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
        self.closeButton = QtWidgets.QPushButton(Form)
        self.closeButton.setGeometry(QtCore.QRect(480, 440, 89, 25))
        self.closeButton.setObjectName("closeButton")
        self.addNoticeLabel = QtWidgets.QLabel(Form)
        self.addNoticeLabel.setGeometry(QtCore.QRect(210, 0, 151, 41))
        self.addNoticeLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.addNoticeLabel.setObjectName("addNoticeLabel")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Notice"))
        self.idLabel.setText(_translate("Form", "<html><head/><body><p>Id : </p></body></html>"))
        self.titlelabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Title :</span></p></body></html>"))
        self.noticeLabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Notice  :</span></p></body></html>"))
        self.id.setText(_translate("Form", "<html><head/><body><p>ID</p></body></html>"))
        self.title.setText(_translate("Form", "<html><head/><body><p>Title</p></body></html>"))
        self.dateLabel.setText(_translate("Form", "<html><head/><body><p>Date Of Publish :</p></body></html>"))
        self.date.setText(_translate("Form", "<html><head/><body><p>29/09/2002</p></body></html>"))
        self.closeButton.setText(_translate("Form", "Delete"))
        self.addNoticeLabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; text-decoration: underline;\">Delete Notice</span></p></body></html>"))

