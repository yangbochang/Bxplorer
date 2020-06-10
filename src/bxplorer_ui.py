# -*- coding: utf-8 -*-

"""
    重构 bxplorer_base
"""

import os

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QHeaderView, QFileDialog, QItemDelegate, QPushButton, QHBoxLayout, QWidget
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from bxplorer_base import Ui_MainWindow
from bxplorer_data import BxplorerData

# class MyButtonDelegate(QItemDelegate):
#     def __init__(self, parent=None):
#         super().__init__()
    
#     def button_delete(self, deleter, option, index):
#         if not self.parent().indexWidget(index):
#             button_delete = QPushButton(
#                 self.tr('DELETE'),
#                 self.parent(),
#                 clicked=self.parent().cellButtonClicked
#             )
#             button_delete.index = [index.row(), index.column()]

#             h_box_layout = QHBoxLayout()
#             h_box_layout.addWidget(button_delete)
#             h_box_layout.setContentsMargins(0, 0, 0, 0)
#             h_box_layout.setAlignment(Qt.AlignCenter)
#             widget = QWidget()
#             widget.setLayout(h_box_layout)
#             self.parent().setIndexWidget(
#                 index,
#                 widget
#             )

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

        self.pushButton.clicked.connect(self.new_root)

    def update_tableView(self):
        ''' 设置tableView '''

        bxplorer_data = BxplorerData(self.data_path)
        data = bxplorer_data.read()
        try:
            row_max = len(data['ROOT'])
        except ValueError:
            print('ok')
        # 设置 tableView
        self.model = QStandardItemModel(row_max, 2)
        self.model.setHorizontalHeaderLabels(['文件夹路径', '操作'])

        for row in range(row_max):
            item = QStandardItem(str(data['ROOT'][row]))
            self.model.setItem(row, 0, item)
            self.model.setCellWidget(row, 1, self.delete_button(str(row)))

        self.tableView_root.setModel(self.model)
        self.tableView_root.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView_root.horizontalHeader().setSectionResizeMode(1, QHeaderView.Interactive)
        self.tableView_root.setColumnWidth(1, 100)

        #self.tableView_root.setItemDelegateForColumn(1, MyButtonDelegate(self))

    def new_root(self):
        ''' 新增root '''
        root = QFileDialog.getExistingDirectory(self, '选择文件夹', os.getcwd())
        if root not in self.bxplorer_data.file_data['ROOT']:
            self.bxplorer_data.file_data['ROOT'].append(root)
        self.bxplorer_data.write(self.bxplorer_data.file_data)
        self.update_tableView()

    def delete_button(self, iden):
        widget = QWidget()
        deletenBtn = QPushButton('Delete')
        deletenBtn.setStyleSheet(''' text-align : center;
                                     background-color : LightCoral;
                                     height : 30px;
                                     border-style : outset;
                                     font : 13px; ''')
        deletenBtn.clicked.connect(lambda: self.delete_button(iden))

        hLayout = QHBoxLayout()
        hLayout.addWidget(deletenBtn)
        hLayout.setContentsMargins(0,0,0,0)
        widget.setLayout(hLayout)
        return widget

