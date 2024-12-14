from PyQt5 import QtCore, QtGui, QtWidgets
from Dialogs.messageBox import *
class addQualification(object):
    def setup(self, addQualification,id,grandparent):
        self.id = id
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

        self.retranslateUi(addQualification,grandparent)
        QtCore.QMetaObject.connectSlotsByName(addQualification)

    def retranslateUi(self, addQualification,grandparent):
        _translate = QtCore.QCoreApplication.translate
        addQualification.setWindowTitle(_translate("addQualification", "Add Qualification"))
        self.exitbutton.setText(_translate("addQualification", "Exit"))
        self.savebutton.setText(_translate("addQualification", "Save"))
        self.qualification.setPlaceholderText(_translate("addQualification", "Add Qualification"))
        self.clickevent(addQualification,grandparent)

    def clickevent(self,parent,grandparent):
        self.exitbutton.clicked.connect(lambda : parent.close())
        self.savebutton.clicked.connect(lambda : self.clickOnSaveButton(parent,grandparent))

    def clickOnSaveButton(self,parent,grandparent):
        text = self.qualification.text()
        if text != "":
            if self.id != 0:
                URL = "http://127.0.0.1:8000/api/qualification/" + str(self.id)
                data = {
                    "degree" : text
                }
                import requests
                r = requests.put(url=URL, data= data)
                print(r.json())
                grandparent.qualificationComboBox.setItemText(0,text)
            else:
                URL = "http://127.0.0.1:8000/api/qualification/"
                data = {
                    "degree" : text
                }
                import requests
                r = requests.post(url= URL,data=data)
                l = r.json()
                grandparent.qualificationComboBox.addItem(str(text))
                grandparent.doctordata["qualification"] = l["id"]
            parent.close()
        else:
            self.window = messageBox()
            self.window.infoBox("Qualification cannot be empty")
            return


