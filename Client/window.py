from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import *


class MyGui(QMainWindow):

    def __init__(self):
        super(MyGui, self).__init__()
        uic.loadUi('test.ui', self)
        self.show()


    def changeColorBrakeBar(self):
        self.brakeBar.setStyleSheet("QProgressBar::chunk "
                                    "{"
                                    "background-color: red;"
                                    "}")

    def changeThrottlePercentage(self, percentage):
        self.throttle_percentage = percentage

    def changeBrakePercentage(self, percentage):
        self.brake_percentage = percentage




def startWindow():
    app = QApplication([])
    gui = MyGui()
    gui.changeColorBrakeBar()
    app.exec_()
    gui.show()
    return gui

