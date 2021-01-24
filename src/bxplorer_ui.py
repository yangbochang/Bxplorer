# -*- coding: utf-8 -*-

"""
    重构 bxplorer_base
"""

import os
import subprocess
from PyQt5.QtWidgets import QMainWindow, QHeaderView, QFileDialog, QPushButton
from PyQt5.QtWidgets import QTableWidgetItem, QAbstractItemView, QItemDelegate

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

    def __play(self, file):
        ''' 播放 '''

        cmd = '"%s" "%s"' % (self.bxplorer_data.player, file)
        subprocess.Popen(cmd)

    def __pd_play(self, file):
        ''' 播放按钮 '''

        pd_play = QPushButton('Play')
        pd_play.clicked.connect(lambda: self.__play(file))
        return pd_play

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

        column_name = self.bxplorer_data.property['name']
        column_size = self.bxplorer_data.property['length']

        # 设置行列名
        self.tw_file.setColumnCount(len(column_name))
        self.tw_file.setHorizontalHeaderLabels(column_name)
        # 设置列宽
        self.tw_file.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        for index, length in enumerate(column_size):
            if length == 0:
                continue
            self.tw_file.horizontalHeader().setSectionResizeMode(index, QHeaderView.Interactive)
            self.tw_file.setColumnWidth(index, length)

        # 设置编辑状态
        self.tw_file.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.tw_file.setItemDelegateForColumn(column_name.index('名称'), EmptyDelegate(self))
        self.tw_file.setItemDelegateForColumn(column_name.index('格式'), EmptyDelegate(self))
        self.tw_file.setItemDelegateForColumn(column_name.index('路径'), EmptyDelegate(self))

        # 获取数据
        data = self.bxplorer_data.read()

        # 获取全部file
        file_reader = FileReader()
        file_list = []
        for root in data['Root']:
            file_list.extend(file_reader.walk_folder(root))

        # 获取文件及标识码
        data['File'].clear()
        for count, file in enumerate(file_list):
            code = file_reader.code_file(file)
            data['File'][code] = {'path': file}
            print(count + 1, '/', len(file_list))
        self.bxplorer_data.write(data)

        # 设置表格行数
        row_count = len(data['File'])
        self.tw_file.setRowCount(row_count)

        # 设置表格内容
        for row, file in enumerate(data['File']):
            file_path = data['File'][file]['path']
            file_name = os.path.basename(file_path)
            file_suffix = os.path.splitext(file_path)[-1]
            self.tw_file.setItem(row, column_name.index('名称'), QTableWidgetItem(file_name))
            self.tw_file.setItem(row, column_name.index('格式'), QTableWidgetItem(file_suffix))
            self.tw_file.setItem(row, column_name.index('路径'), QTableWidgetItem(file_path))
            self.tw_file.setCellWidget(row, column_name.index('播放'), self.__pd_play(file_path))

    def __update_tw_root(self):
        ''' 更新root的tableWidget '''

        # 设置 tableWidget 格式
        self.tw_root.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tw_root.horizontalHeader().setSectionResizeMode(1, QHeaderView.Interactive)
        self.tw_file.setColumnWidth(1, 100)

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

class EmptyDelegate(QItemDelegate):
    def __init__(self, parent):
        super(EmptyDelegate, self).__init__(parent)

    def createEditor(self, QWidget, QStyleOptionViewItem, QModelIndex):
        return None
