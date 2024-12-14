# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'statistics.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_superadminstats(object):
    def setupUi(self, superadminstats):
        superadminstats.setObjectName("superadminstats")
        superadminstats.resize(753, 480)
        self.titleLabel = QtWidgets.QLabel(superadminstats)
        self.titleLabel.setGeometry(QtCore.QRect(180, 10, 361, 41))
        self.titleLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.titleLabel.setObjectName("titleLabel")
        self.frame = QtWidgets.QFrame(superadminstats)
        self.frame.setGeometry(QtCore.QRect(20, 70, 711, 361))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.overall = QtWidgets.QPushButton(self.frame)
        self.overall.setGeometry(QtCore.QRect(530, 60, 141, 111))
        self.overall.setObjectName("overall")
        self.dispensary = QtWidgets.QPushButton(self.frame)
        self.dispensary.setGeometry(QtCore.QRect(370, 60, 141, 111))
        self.dispensary.setObjectName("dispensary")
        self.patient = QtWidgets.QPushButton(self.frame)
        self.patient.setGeometry(QtCore.QRect(50, 60, 141, 111))
        self.patient.setObjectName("patient")
        self.hospital = QtWidgets.QPushButton(self.frame)
        self.hospital.setGeometry(QtCore.QRect(210, 60, 141, 111))
        self.hospital.setObjectName("hospital")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(50, 200, 141, 111))
        self.pushButton_5.setObjectName("pushButton_5")
        self.testcenter = QtWidgets.QPushButton(self.frame)
        self.testcenter.setGeometry(QtCore.QRect(210, 200, 141, 111))
        self.testcenter.setObjectName("testcenter")
        self.events = QtWidgets.QPushButton(self.frame)
        self.events.setGeometry(QtCore.QRect(370, 200, 141, 111))
        self.events.setObjectName("events")
        self.doctor = QtWidgets.QPushButton(self.frame)
        self.doctor.setGeometry(QtCore.QRect(530, 200, 141, 111))
        self.doctor.setObjectName("doctor")
        self.pushButton_9 = QtWidgets.QPushButton(superadminstats)
        self.pushButton_9.setGeometry(QtCore.QRect(330, 440, 89, 25))
        self.pushButton_9.setObjectName("pushButton_9")

        self.retranslateUi(superadminstats)
        QtCore.QMetaObject.connectSlotsByName(superadminstats)

    def retranslateUi(self, superadminstats):
        _translate = QtCore.QCoreApplication.translate
        superadminstats.setWindowTitle(_translate("superadminstats", "Form"))
        self.titleLabel.setText(_translate("superadminstats", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; text-decoration: underline;\">Stats View</span></p></body></html>"))
        self.overall.setText(_translate("superadminstats", "Overall"))
        self.dispensary.setText(_translate("superadminstats", "Dispensary"))
        self.patient.setText(_translate("superadminstats", "Patient"))
        self.hospital.setText(_translate("superadminstats", "Hospital"))
        self.pushButton_5.setText(_translate("superadminstats", "Blood Bank Centers"))
        self.testcenter.setText(_translate("superadminstats", "Test Centers"))
        self.events.setText(_translate("superadminstats", "Events"))
        self.doctor.setText(_translate("superadminstats", "Events"))
        self.pushButton_9.setText(_translate("superadminstats", "close"))

