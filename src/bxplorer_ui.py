# -*- coding: utf-8 -*-

"""
    重构 bxplorer_base
"""

import os
from zlib import crc32
from hashlib import md5

#from PyQt5.QtCore import Qt
#from PyQt5.QtWidgets import QMainWindow, QHeaderView, QFileDialog, QItemDelegate, QPushButton, QHBoxLayout, QWidget
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from bxplorer_base import Ui_MainWindow
from bxplorer_data import BxplorerData
import bxplorer_macro as bm


class Bxplorer(QMainWindow, Ui_MainWindow):
    ''' 重构 bxplorer_base '''

    def __init__(self, data_path=None):
        super().__init__()

        # 初始化界面
        self.setupUi(self)
        # 初始化数据
        self.bxplorer_data = BxplorerData(data_path)

        # 设置按钮响应
        self.pb_open.clicked.connect(self.new_root)

        # 设置tableWidget的显示内容
        self.update_tw_root()

    def update_tw_root(self):
        ''' 设置tw_root '''

        # 设置 tableWidget 格式
        self.tw_root.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tw_root.horizontalHeader().setSectionResizeMode(1, QHeaderView.Interactive)
        self.tw_root.setColumnWidth(1, 100)

        # 设置 tableWidget 内容
        data = self.bxplorer_data.read()
        row_count = len(data[bm.KEY_ROOT])
        self.tw_root.setRowCount(row_count)
        # for row in range(row_count):
        row = 0
        for key in data[bm.KEY_ROOT]:
            # root内容
            self.tw_root.setItem(row, 0, QTableWidgetItem(str(key)))
            # 删除按钮
            self.tw_root.setCellWidget(row, 1, self.pb_delete_root(row))
            row += 1

        # 更新file数据
        file = File()
        file.rewrite()
        # 更新tw_file
        self.update_tw_file()


    def new_root(self):
        ''' 新增root '''

        data = self.bxplorer_data.read()
        root = QFileDialog.getExistingDirectory(self, '选择文件夹', os.getcwd())
        if root not in data[bm.KEY_ROOT]:
            data[bm.KEY_ROOT][root] = {}
            # data[bm.KEY_ROOT].sort()

        # 更新数据文件和界面
        self.bxplorer_data.write(data)
        self.update_tw_root()


    def pb_delete_root(self, index):
        ''' 删除root按钮 '''

        pb_delete_root = QPushButton('删除')
        pb_delete_root.clicked.connect(lambda: self.delete_root(index))
        return pb_delete_root


    def delete_root(self, index):
        ''' 删除root '''

        data = self.bxplorer_data.read()
        del data[bm.KEY_ROOT][index]
        self.bxplorer_data.write(data)
        self.update_tw_root()

    def update_tw_file(self):
        ''' 设置tw_file '''

        # 设置 tableWidget 格式
        self.tw_file.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.tw_file.horizontalHeader().resizeSections(QHeaderView.ResizeToContents)

        # 设置 tableWidget 内容
        data = self.bxplorer_data.read()
        row_count = len(data[bm.KEY_FILE])
        self.tw_file.setRowCount(row_count)
        # for row in range(row_count):
        #     # root内容
        #     self.tw_file.setItem(row, 0, QTableWidgetItem(str(data[bm.KEY_FILE][row][0])))
        #     # 删除按钮
        #     #self.tw_file.setCellWidget(row, 1, self.pb_delete_root(row))
        row = 0
        for value in data[bm.KEY_FILE].values():
            self.tw_file.setItem(row, 0, QTableWidgetItem(str(value[0])))
            row += 1


    # def pb_play_file(self,  )

class File():
    ''' File '''

    def __init__(self, data_path=None):
        self.bxplorer_data = BxplorerData(data_path)

    def read(self):
        ''' 读File '''

        data = self.bxplorer_data.read()
        return data[bm.KEY_FILE]

    def rewrite(self):
        ''' 重写File '''

        data = self.bxplorer_data.read()
        file_dict = {}
        for path in data[bm.KEY_ROOT]:
            for root, dirs, files in os.walk(path):
                for file in files:
                    #file_list.append([file, os.path.join(root, file)])
                    file_path = os.path.join(root, file).replace('\\', '/')
                    file_read = open(file_path, 'rb').read()
                    code_crc = crc32(file_read)
                    code_md5 = md5(file_read).hexdigest()
                    file_dict[str(code_crc) + '-' + str(code_md5)] = [file]
        data[bm.KEY_FILE] = file_dict
        self.bxplorer_data.write(data)
