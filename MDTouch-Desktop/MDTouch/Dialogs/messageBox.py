from PyQt5.QtWidgets import QMessageBox

class messageBox(object):
    def infoBox(self, text):
        box = QMessageBox()
        box.setText(text)
        box.setIcon(QMessageBox.Information)
        box.setWindowTitle('Information')
        box.setStandardButtons(QMessageBox.Ok)
        box.exec()

    def warningBox(self, text):
        box = QMessageBox()
        box.setText(text)
        box.setIcon(QMessageBox.Warning)
        box.setWindowTitle('Warning')
        box.setStandardButtons(QMessageBox.Retry)
        box.setStandardButtons(QMessageBox.Ok)
        box.exec()

    def errorBox(self, text):
        box = QMessageBox()
        box.setText(text)
        box.setIcon(QMessageBox.Error)
        box.setWindowTitle('Error!')
        box.setStandardButtons(QMessageBox.Retry)
        box.setStandardButtons(QMessageBox.Ok)
        box.exec()

    def questionBox(self, text):
        box = QMessageBox()
        box.setText(text)
        box.setIcon(QMessageBox.Question)
        box.setWindowTitle('Question')
        box.setStandardButtons(QMessageBox.Yes)
        box.setStandardButtons(QMessageBox.No)
        box.exec()