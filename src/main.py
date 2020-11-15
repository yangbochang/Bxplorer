# -*- coding: utf-8 -*-

"""
    bcyang's explorer
"""

import sys
from PyQt5.QtWidgets import QApplication
from bxplorer_ui import Bxplorer

if __name__ == '__main__':

    APP = QApplication(sys.argv)
    BXPLORER = Bxplorer() if len(sys.argv) == 1 else Bxplorer(sys.argv[1])
    BXPLORER.show()
    sys.exit(APP.exec_())
