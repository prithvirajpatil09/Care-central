# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addQualification.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_addQualification(object):
    def setupUi(self, addQualification):
        addQualification.setObjectName("addQualification")
        addQualification.resize(557, 143)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(addQualification.sizePolicy().hasHeightForWidth())
        addQualification.setSizePolicy(sizePolicy)
        self.exitbutton = QtWidgets.QPushButton(addQualification)
        self.exitbutton.setGeometry(QtCore.QRect(460, 110, 89, 25))
        self.exitbutton.setObjectName("exitbutton")
        self.savebutton = QtWidgets.QPushButton(addQualification)
        self.savebutton.setGeometry(QtCore.QRect(360, 110, 89, 25))
        self.savebutton.setObjectName("savebutton")
        self.qualification = QtWidgets.QLineEdit(addQualification)
        self.qualification.setGeometry(QtCore.QRect(50, 50, 471, 25))
        self.qualification.setObjectName("qualification")

        self.retranslateUi(addQualification)
        QtCore.QMetaObject.connectSlotsByName(addQualification)

    def retranslateUi(self, addQualification):
        _translate = QtCore.QCoreApplication.translate
        addQualification.setWindowTitle(_translate("addQualification", "Add Qualification"))
        self.exitbutton.setText(_translate("addQualification", "Exit"))
        self.savebutton.setText(_translate("addQualification", "Save"))
        self.qualification.setPlaceholderText(_translate("addQualification", "Add Qualification"))

