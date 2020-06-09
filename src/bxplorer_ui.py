# -*- coding: utf-8 -*-

"""
    重构 bxplorer_base
"""

from PyQt5.QtWidgets import QMainWindow, QHeaderView
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from bxplorer_base import Ui_MainWindow
from bxplorer_data import BxplorerData

class Bxplorer(QMainWindow, Ui_MainWindow):
    ''' 重构 bxplorer_base '''

    def __init__(self, data_path=None):
        super().__init__()

        # 获取数据
        self.data_path = data_path
        self.bxplorer_data = BxplorerData(self.data_path)

        # 初始化界面
        self.setupUi(self)
        self.setWindowTitle('Bxplorer')
        self.update_tableView()

    def update_tableView(self):
        ''' 设置tableView '''

        data = BxplorerData(self.data_path).read()
        row_max = len(data['ROOTS'])
        # 设置 tableView
        self.model = QStandardItemModel(row_max, 2)
        self.model.setHorizontalHeaderLabels(['文件夹路径', '操作'])

        for row in range(row_max):
            item = QStandardItem(str(data['ROOTS'][row]))
            self.model.setItem(row, 0, item)

        self.tableView_root.setModel(self.model)
        self.tableView_root.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView_root.horizontalHeader().setSectionResizeMode(1, QHeaderView.Interactive)
        self.tableView_root.setColumnWidth(1, 100)
