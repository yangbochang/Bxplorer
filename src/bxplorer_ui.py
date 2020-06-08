# -*- coding: utf-8 -*-

#
# 重构 bxplorer_base
#

from PyQt5.QtWidgets import QMainWindow, QHeaderView
from PyQt5.QtGui import QStandardItemModel
from bxplorer_base import Ui_MainWindow
from bxplorer_data import BxplorerData

class Bxplorer(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None, data_path=None):
        super(Bxplorer, self).__init__(parent, data_path)
        self.setupUi(self)

        # 设置标题
        self.setWindowTitle('Bxplorer')

        # 设置 tableView
        self.model = QStandardItemModel(4, 2)
        self.model.setHorizontalHeaderLabels(['文件夹路径', '操作'])

        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView.horizontalHeader().setSectionResizeMode(1, QHeaderView.Interactive)
        self.tableView.setColumnWidth(1, 100)
