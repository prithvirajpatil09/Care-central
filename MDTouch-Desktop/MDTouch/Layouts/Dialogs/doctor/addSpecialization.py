# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addSpecialization.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_addSpecialization(object):
    def setupUi(self, addSpecialization):
        addSpecialization.setObjectName("addSpecialization")
        addSpecialization.resize(557, 143)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(addSpecialization.sizePolicy().hasHeightForWidth())
        addSpecialization.setSizePolicy(sizePolicy)
        self.exitbutton = QtWidgets.QPushButton(addSpecialization)
        self.exitbutton.setGeometry(QtCore.QRect(460, 110, 89, 25))
        self.exitbutton.setObjectName("exitbutton")
        self.savebutton = QtWidgets.QPushButton(addSpecialization)
        self.savebutton.setGeometry(QtCore.QRect(360, 110, 89, 25))
        self.savebutton.setObjectName("savebutton")
        self.specilaization = QtWidgets.QLineEdit(addSpecialization)
        self.specilaization.setGeometry(QtCore.QRect(50, 50, 471, 25))
        self.specilaization.setObjectName("specilaization")

        self.retranslateUi(addSpecialization)
        QtCore.QMetaObject.connectSlotsByName(addSpecialization)

    def retranslateUi(self, addSpecialization):
        _translate = QtCore.QCoreApplication.translate
        addSpecialization.setWindowTitle(_translate("addSpecialization", "Add Specializtaion"))
        self.exitbutton.setText(_translate("addSpecialization", "Exit"))
        self.savebutton.setText(_translate("addSpecialization", "Save"))
        self.specilaization.setPlaceholderText(_translate("addSpecialization", "Add Specialization"))

