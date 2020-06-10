# -*- coding: utf-8 -*-

"""
    Bxplorer 的数据
"""

import os 
import json

class BxplorerData():
    ''' Bxplorer的数据操作 '''

    def __init__(self, file_path):

        # 初始化
        self.file_path = file_path              # 数据文件路径（包含文件名）
        self.file_name = 'BXPLORER.DATA'        # 默认数据文件名
        # 默认初始数据文件内容
        self.init_file_data = {'ROOT': []}

        # 如果指定file_path，则默认在当前文件夹下
        if self.file_path is None:
            self.file_path = \
                os.path.join(os.path.dirname(os.path.realpath(__file__)), self.file_name)

        # 使用json解析数据
        if os.path.isfile(self.file_path):
            try:
                read_file = open(self.file_path, 'r', encoding='utf-8').read()
                json.loads(read_file)
                self.file_data = self.read()
                self.file_data['ROOT']
            except (ValueError, TypeError):
                self.backup_and_new()
        else:
            self.new()

    def new(self):
        ''' 创建新数据文件 '''

        file = open(self.file_path, 'w', encoding='utf-8')
        file.write(json.dumps(self.init_file_data, indent=2, sort_keys=True, ensure_ascii=False))
        file.close()

    def backup_and_new(self):
        ''' 备份后创建新数据文件 '''

        file_backup = self.file_path + '.bak'
        if os.path.isfile(file_backup):
            os.remove(file_backup)
        os.rename(self.file_path, file_backup)
        self.new()

    def read(self):
        ''' 读数据 '''

        read_file = open(self.file_path, 'r', encoding='utf-8').read()
        return json.loads(read_file)

    def write(self, data):
        ''' 写数据 '''

        open_file = open(self.file_path, 'w', encoding='utf-8')
        open_file.write(json.dumps(data))
        open_file.close()

