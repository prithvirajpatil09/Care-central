

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
        ax = fig.add_subplot(111)
        n_groups = 6


        means_men = (115,112 , 130, 135, 127,122)
        std_men = (12, 13, 14, 1, 2,10)

        means_women = (10, 12, 114, 22, 28, 13)
        std_women = (3, 5, 2, 3, 2,8)
        # Example data
        '''
        people = ('Doctor', 'Hospital', 'BloodCenter', 'Dispensary', 'TestCenter','ES','Ambulance')
        self.y_pos = np.arange(len(people))
        self.axes.set_yticks(self.y_pos)
        self.axes.set_yticklabels(people)
        self.axes.invert_yaxis()  # labels read top-to-bottom
        self.axes.set_xlabel('Quantity in Litre')
        self.axes.set_title('Medical Services in a area per Patient')
        '''
        index = np.arange(n_groups)
        bar_width = 0.35

        opacity = 0.4
        error_config = {'ecolor': '0.3'}

        rects1 = ax.bar(index, means_men, bar_width,
                        alpha=opacity, color='b',
                        error_kw=error_config,
                        label='Accepted')

        rects2 = ax.bar(index + bar_width, means_women, bar_width,
                        alpha=opacity, color='r',
                        error_kw=error_config,
                        label='Rejected')

        ax.set_xlabel('Month')
        ax.set_ylabel('Appointments')
        ax.set_title('Appointments Acceptance Graph')
        ax.set_xticks(index + bar_width / 2)
        ax.set_xticklabels(('Aug','Sep', 'Oct', 'Nov', 'Dec', 'Jan'))
        ax.legend()
        FingureCanvas.__init__(self, fig)
        FingureCanvas.setSizePolicy(self,QSizePolicy.Expanding,QSizePolicy.Expanding)
        FingureCanvas.updateGeometry(self)





class hospitalAppointmentGraph(object):
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
        self.frame.setStyleSheet("border : None")

        self.retranslateUi(geographicalGraph)
        QtCore.QMetaObject.connectSlotsByName(geographicalGraph)

    def retranslateUi(self, geographicalGraph):
        _translate = QtCore.QCoreApplication.translate
        geographicalGraph.setWindowTitle(_translate("geographicalGraph", "Form"))
        self.titleLabel.setText(_translate("geographicalGraph", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; text-decoration: underline;\">Half Month Report Of Hospitals</span></p></body></html>"))
        self.closeButton.setText(_translate("geographicalGraph", "Close"))
        self.titleLabel_2.setText(_translate("geographicalGraph", "<html><head/><body><p align=\"center\"></p></body></html>"))
        self.titleLabel_3.setText(_translate("geographicalGraph", "<html><head/><body><p align=\"center\">Hospital ID : 5</p></body></html>"))
        self.events(geographicalGraph)
        self.closeButton.clicked.connect(lambda :geographicalGraph.close())

    def events(self,BloodBankMainWindow):


        # Blood Bank Data View Start

        self.widget = QWidget(self.frame)
        self.layout = QVBoxLayout()
        self.canvas = Canvas()
        #self.canvas.plot([0.115,0.223,0,0.22,0.33,0.45,0.12])
        self.layout.addWidget(self.canvas)
        self.widget.setLayout(self.layout)
