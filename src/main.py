#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
    bcyang's explorer
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from bxplorer import *

class Bxplorer(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Bxplorer, self).__init__(parent)
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    bxplorer = Bxplorer()
    bxplorer.show()
    sys.exit(app.exec_())
    print('# bxplorer #')
