
from PyQt5 import QtCore, QtGui, QtWidgets
from Dialogs.messageBox import *
class addSpecialization(object):
    def setup(self, addSpecialization,id,grandparent):
        self.id = id
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

        self.retranslateUi(addSpecialization,grandparent)
        QtCore.QMetaObject.connectSlotsByName(addSpecialization)

    def retranslateUi(self, addSpecialization,grandparent):
        _translate = QtCore.QCoreApplication.translate
        addSpecialization.setWindowTitle(_translate("addSpecialization", "Add Specializtaion"))
        self.exitbutton.setText(_translate("addSpecialization", "Exit"))
        self.savebutton.setText(_translate("addSpecialization", "Save"))
        self.specilaization.setPlaceholderText(_translate("addSpecialization", "Add Specialization"))

        self.clickevent(addSpecialization,grandparent)

    def clickevent(self,parent,grandparent):
        self.exitbutton.clicked.connect(lambda : parent.close())
        self.savebutton.clicked.connect(lambda : self.clickOnSaveButton(parent,grandparent))

    def clickOnSaveButton(self,parent,grandparent):
        text = self.specilaization.text()
        if text != "":
            if self.id != 0:
                URL = "http://127.0.0.1:8000/api/specialization/" + str(self.id)
                data = {
                    "skill" : text
                }
                import requests
                r = requests.put(url=URL, data= data)
                print(r.json())
                grandparent.specializationComboBox.setItemText(0,text)
            else:
                print(text)
                URL = "http://127.0.0.1:8000/api/specialization/"
                data = {
                    "skill" : text
                }
                import requests
                r = requests.post(url=URL,data=data)

                l = r.json()
                print(l,"-------------------------")
                grandparent.specializationComboBox.addItem(str(text))
                grandparent.doctordata["specialization"] = l["id"]
            parent.close()
        else:
            self.window = messageBox()
            self.window.infoBox("Qualification cannot be empty")
            return

