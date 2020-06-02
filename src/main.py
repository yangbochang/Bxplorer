#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
    bcyang's explorer
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFrame
from bxplorer import *

class Bxplorer(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Bxplorer, self).__init__(parent)
        self.setupUi(self)

    def show_ui(self, y=50):
        self.pu = QPushButton(self)
        self.pu.setText('sdf')
        self.pu.setGeometry(50, y, 100, 50)
    
    def keyPressEvent(self, QKeyEvent):
        self.show_ui(70)
        self.pu.setVisible(True)
        print('sdf')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    bxplorer = Bxplorer()
    bxplorer.show()
    sys.exit(app.exec_())
    print('# bxplorer #')
