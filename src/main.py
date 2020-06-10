#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
    bcyang's explorer
"""

import sys
from PyQt5.QtWidgets import QApplication
from bxplorer_ui import Bxplorer


if __name__ == '__main__':

    app = QApplication(sys.argv)
    bxplorer = Bxplorer() if len(sys.argv) == 1 else Bxplorer(sys.argv[1])
    bxplorer.show()
    sys.exit(app.exec_())
