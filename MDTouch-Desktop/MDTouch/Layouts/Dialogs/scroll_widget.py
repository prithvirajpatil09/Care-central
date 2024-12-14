from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class RssItem(QWidget):
    __pyqtSignals__ = ("articleViewed(bool)",
                       "articleOpened(bool)",
                       "articleMarkedGood(bool)")

    def __init__(self, title, date, parent = None):
        super(RssItem, self).__init__(parent)
        self.initWidget(title, date)

    def initWidget(self, title, date):
        title = QLabel(title)
        date = QLabel(date)
        titleBox = QHBoxLayout()
        titleBox.addWidget(title)
        titleBox.addWidget(date)
        self.setLayout(titleBox)

class ItemsList(QWidget):
    def __init__(self, items, parent=None):
        super(ItemsList, self).__init__(parent)
        self.initWidget(items)

    def initWidget(self, items):
        listBox = QVBoxLayout(self)
        self.setLayout(listBox)

        scroll = QScrollArea(self)
        listBox.addWidget(scroll)
        scroll.setWidgetResizable(True)
        scrollContent = QWidget(scroll)

        scrollLayout = QVBoxLayout(scrollContent)
        scrollContent.setLayout(scrollLayout)
        for item in items:
            scrollLayout.addWidget(item)
        scroll.setWidget(scrollContent)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage("ok")
        self.resize(640, 480)
        self.setWindowTitle("Smart Rss")
        items=[]
        for x in range(0, 1):
            items.append(RssItem("Title no %s" % x, "2000-1-%s" %x))
        self.setCentralWidget(ItemsList(items))
        self.show()

class MainApp(QApplication):
    def __init__(self, args):
        super(MainApp, self).__init__(args)
        self.addWidgets()
        self.exec_()

    def addWidgets(self):
        self.window = MainWindow()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
