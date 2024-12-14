import math, sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import *

class loadingOverlay(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        palette = QPalette(self.palette())
        palette.setColor(palette.Background, Qt.transparent)
        self.setPalette(palette)
        print('Object Created')


    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.fillRect(event.rect(), QBrush(QColor(255, 255, 255, 127)))
        painter.setPen(QPen(Qt.NoPen))

        for i in range(100):
            if (self.counter / 4) % 8 == i:
                painter.setBrush(QBrush(QColor(0, 0, 0)))
            else:
                painter.setBrush(QBrush(QColor(127, 127, 127)))

            painter.drawEllipse(
                self.width() / 2 + 30 * math.cos(2 * math.pi * i / 8.0),
                self.height() / 2 + 30 * math.sin(2 * math.pi * i / 8.0),
                20, 20)
            print(i, end = '   ')

        painter.end()

    def showEvent(self, event):
        self.counter = 0

    def timerEvent(self, event):
        self.counter = (self.counter + 1) % 4
        self.update()


