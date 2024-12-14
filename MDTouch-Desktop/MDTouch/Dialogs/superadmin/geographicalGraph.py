

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FingureCanvas
from matplotlib.figure import Figure
import matplotlib
from matplotlib import *
import numpy as np

class Canvas(FingureCanvas):
    def __init__(self, parent = None, width =7, height = 4, dpi =100):

        fig = Figure(figsize=(width, height), dpi=dpi)
        #self.axes = fig.add_subplot(111)
        a = fig.add_subplot(111)
        self.axes = fig.add_subplot(111)
        # Example data
        people = ('Doctor', 'Hospital', 'BloodCenter', 'Dispensary', 'TestCenter','ES','Ambulance')
        self.y_pos = np.arange(len(people))
        self.axes.set_yticks(self.y_pos)
        self.axes.set_yticklabels(people)
        self.axes.invert_yaxis()  # labels read top-to-bottom
        self.axes.set_xlabel('Quantity in Litre')
        self.axes.set_title('Medical Services in a area per Patient')

        FingureCanvas.__init__(self, fig)
        FingureCanvas.setSizePolicy(self,QSizePolicy.Expanding,QSizePolicy.Expanding)
        FingureCanvas.updateGeometry(self)


    def plot(self,performance):
        self.axes.barh(self.y_pos, performance, align='center',color='red', ecolor='black')



class geographicalGraph(object):
    def setup(self, geographicalGraph):
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
        self.events(geographicalGraph)

    def events(self,BloodBankMainWindow):


        # Blood Bank Data View Start

        self.widget = QWidget(self.frame)
        self.layout = QVBoxLayout()
        self.canvas = Canvas()
        self.canvas.plot([0.115,0.223,0,0.22,0.33,0.45,0.12])
        self.layout.addWidget(self.canvas)
        self.widget.setLayout(self.layout)
