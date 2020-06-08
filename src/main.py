#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
    bcyang's explorer
"""

import os
import sys
import json
from PyQt5.QtWidgets import QApplication
from bxplorer_ui import Bxplorer
from bxplorer_data import BxplorerData


def bxplorer_data():
    if len(sys.argv) == 1:
        data = {'roots': ''}



if __name__ == '__main__':

    # bxplorer_data = BxplorerData('.\\Bxplorer.data')
    # data = {'a': 'b'}
    # bxplorer_data.write(data)

    # root = sys.argv[0]
    # root = os.getcwd()
    app = QApplication(sys.argv)
    bxplorer = Bxplorer() if len(sys.argv) == 1 else Bxplorer(sys.argv[1])
    bxplorer.show()
    sys.exit(app.exec_())
