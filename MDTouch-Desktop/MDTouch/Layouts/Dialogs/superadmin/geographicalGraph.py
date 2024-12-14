# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'geographicalGraph.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_geographicalGraph(object):
    def setupUi(self, geographicalGraph):
        geographicalGraph.setObjectName("geographicalGraph")
        geographicalGraph.resize(728, 564)
        self.frame = QtWidgets.QFrame(geographicalGraph)
        self.frame.setGeometry(QtCore.QRect(20, 90, 681, 411))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.titleLabel = QtWidgets.QLabel(geographicalGraph)
        self.titleLabel.setGeometry(QtCore.QRect(20, 10, 681, 41))
        self.titleLabel.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.titleLabel.setObjectName("titleLabel")
        self.closeButton = QtWidgets.QPushButton(geographicalGraph)
        self.closeButton.setGeometry(QtCore.QRect(320, 520, 89, 25))
        self.closeButton.setObjectName("closeButton")
        self.titleLabel_2 = QtWidgets.QLabel(geographicalGraph)
        self.titleLabel_2.setGeometry(QtCore.QRect(10, 50, 251, 41))
        self.titleLabel_2.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.titleLabel_2.setObjectName("titleLabel_2")
        self.titleLabel_3 = QtWidgets.QLabel(geographicalGraph)
        self.titleLabel_3.setGeometry(QtCore.QRect(420, 50, 251, 41))
        self.titleLabel_3.setStyleSheet("font-size:12pt;\n"
"font-weight: bold;")
        self.titleLabel_3.setObjectName("titleLabel_3")

        self.retranslateUi(geographicalGraph)
        QtCore.QMetaObject.connectSlotsByName(geographicalGraph)

    def retranslateUi(self, geographicalGraph):
        _translate = QtCore.QCoreApplication.translate
        geographicalGraph.setWindowTitle(_translate("geographicalGraph", "Form"))
        self.titleLabel.setText(_translate("geographicalGraph", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; text-decoration: underline;\">Geographical Comparision With Medical Services</span></p></body></html>"))
        self.closeButton.setText(_translate("geographicalGraph", "Close"))
        self.titleLabel_2.setText(_translate("geographicalGraph", "<html><head/><body><p align=\"center\">state</p></body></html>"))
        self.titleLabel_3.setText(_translate("geographicalGraph", "<html><head/><body><p align=\"center\">city</p></body></html>"))

