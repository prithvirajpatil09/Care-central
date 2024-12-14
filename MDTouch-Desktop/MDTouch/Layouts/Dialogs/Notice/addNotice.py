# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addNotice.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(580, 439)
        self.frame = QtWidgets.QFrame(Form)
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
        self.publishButton = QtWidgets.QPushButton(Form)
        self.publishButton.setGeometry(QtCore.QRect(240, 410, 89, 25))
        self.publishButton.setObjectName("publishButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Add Notice"))
        self.addNoticeLabel.setText(_translate("Form", "<html><head/><body><p><span style=\" text-decoration: underline;\">Add Notice</span></p></body></html>"))
        self.titlelabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Title :</span></p></body></html>"))
        self.noticeLabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Notice  :</span></p></body></html>"))
        self.publishButton.setText(_translate("Form", "Publish"))

