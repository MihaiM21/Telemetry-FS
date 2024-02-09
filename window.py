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
def main():
    app = QApplication([])
    window = MyGui()
    window.changeColorBrakeBar()
    app.exec_()

if __name__ == '__main__':
    main()