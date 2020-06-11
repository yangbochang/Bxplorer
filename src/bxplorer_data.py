# -*- coding: utf-8 -*-

"""
    Bxplorer 的数据
"""

import os 
import json

INIT_FILE_DATA = {'File': [], 'Root': []}

class BxplorerData():
    ''' Bxplorer的数据操作 '''

    def __init__(self, file_path):

        self.init_file_data = INIT_FILE_DATA
        self.file_name = 'BXPLORER.DATA'        # 默认数据文件名
        self.file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), self.file_name) \
            if file_path is None else file_path

        if os.path.isfile(self.file_path):
            # json校验
            try:
                read_file = open(self.file_path, 'r', encoding='utf-8').read()
                file_data = json.loads(read_file)
            except (ValueError, TypeError, KeyError):
                self.backup_and_new()
            # 判断字典里是否有File和Root
            if 'File' not in file_data or 'Root' not in file_data:
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
        open_file.write(json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False))
        open_file.close()
