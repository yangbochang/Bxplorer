# -*- coding: utf-8 -*-

"""
    重构 bxplorer_base
"""

import os
from PyQt5.QtWidgets import QMainWindow, QHeaderView, QFileDialog, QPushButton, QTableWidgetItem
# from PyQt5.QtGui import QStandardItemModel, QStandardItem

from bxplorer_base import Ui_MainWindow
from bxplorer_data import BxplorerData
from file_reader import FileReader

class Bxplorer(QMainWindow, Ui_MainWindow):
    ''' 重构 bxplorer_base '''

    def __init__(self, data_path=None):
        super().__init__()

        # 初始化界面
        self.setupUi(self)
        # 初始化数据
        self.bxplorer_data = BxplorerData(data_path)

        # 设置按钮响应
        self.pb_open.clicked.connect(self.__new_root)

        # 设置tableWidget的显示内容
        self.__update_tw_root()

    def __new_root(self):
        ''' 新增root '''

        data = self.bxplorer_data.read()
        # 获取新root
        root = QFileDialog.getExistingDirectory(self, '选择文件夹', os.getcwd())
        file_reader = FileReader()
        data['Root'][root] = file_reader.code_folder(root)
        # 更新数据文件和界面
        self.bxplorer_data.write(data)
        self.__update_tw_root()

    def __delete_root(self, index):
        ''' 删除root '''

        data = self.bxplorer_data.read()
        for row, root in enumerate(data['Root']):
            if row == index:
                del data['Root'][root]
                break
        self.bxplorer_data.write(data)
        self.__update_tw_root()

    def __pb_delete_root(self, index):
        ''' 删除root按钮 '''

        pb_delete_root = QPushButton('删除')
        pb_delete_root.clicked.connect(lambda: self.__delete_root(index))
        return pb_delete_root

    def __update_tw_file(self):
        ''' 设置tw_file '''

        # 设置 tableWidget 格式
        self.tw_file.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.tw_file.horizontalHeader().resizeSections(QHeaderView.ResizeToContents)

        # 设置 tableWidget 内容
        data = self.bxplorer_data.read()

        # 获取全部file
        file_reader = FileReader()
        file_list = []
        for root in data['Root']:
            file_list.extend(file_reader.walk_folder(root))

        # 获取文件及标识码
        data['File'].clear()
        count = 0
        for file in file_list:
            code = file_reader.code_file(file)
            data['File'][code] = {'path': file}
            count += 1
            print(count, '/', len(file_list))
        self.bxplorer_data.write(data)

        row_count = len(data['File'])
        self.tw_file.setRowCount(row_count)
        row = 0
        for file in data['File']:
            self.tw_file.setItem(row, 0, QTableWidgetItem(data['File'][file]['path']))
            row += 1

    def __update_tw_root(self):
        ''' 更新root的tableWidget '''

        # 设置 tableWidget 格式
        self.tw_root.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tw_root.horizontalHeader().setSectionResizeMode(1, QHeaderView.Interactive)
        self.tw_root.setColumnWidth(1, 100)

        # 设置 tableWidget 内容
        data = self.bxplorer_data.read()
        row_count = len(data['Root'])
        self.tw_root.setRowCount(row_count)
        row = 0
        for root in data['Root']:
            # root内容
            self.tw_root.setItem(row, 0, QTableWidgetItem(str(root)))
            # 删除按钮
            self.tw_root.setCellWidget(row, 1, self.__pb_delete_root(row))
            row += 1

        # 更新tw_file
        self.__update_tw_file()
