# -*- coding: utf-8 -*-

"""
    Bxplorer 的数据
"""

import os
import json

INIT_FILE_NAME = 'BXPLORE.DATA'
INIT_FILE_DATA = {
    'File': {},
    'Root': {},
    'Property': {
        'name': ['名称', '演员', '地域', '无马', '字幕', '分类', '标签', '播放', '操作', '格式', '路径'],
        'length': [200, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    },
    'Player': r'D:\Program Files\PotPlayer64\PotPlayerMini64.exe'
}

class BxplorerData():
    ''' Bxplorer的数据操作 '''

    def __init__(self, data_path):

        self.data_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), INIT_FILE_NAME) \
            if data_path is None else data_path

        self.property = INIT_FILE_DATA['Property']
        self.player = INIT_FILE_DATA['Player']

        if os.path.isfile(self.data_path):
            if os.path.getsize(self.data_path) == 0:
                self.__new()
            else:
                try:
                    file_read = open(self.data_path, 'r', encoding='utf-8').read()
                    file_data = json.loads(file_read)
                    if 'File' not in file_data or 'Root' not in file_data:
                        self.__backup_and_new()
                except (TypeError, KeyError, ValueError):
                    self.__backup_and_new()
        else:
            self.__new()

    def __new(self):
        ''' 创建新数据文件 '''

        file = open(self.data_path, 'w', encoding='utf-8')
        file.write(json.dumps(INIT_FILE_DATA, indent=2, sort_keys=True, ensure_ascii=False))
        file.close()

    def __backup_and_new(self):
        ''' 备份后创建新数据文件 '''

        file_backup = self.data_path + '.bak'
        if os.path.isfile(file_backup):
            os.remove(file_backup)
        os.rename(self.data_path, file_backup)
        self.__new()

    def read(self):
        ''' 读数据 '''

        open_file = open(self.data_path, 'r', encoding='utf-8')
        data = json.load(open_file)
        open_file.close()
        return data

    def write(self, data):
        ''' 写数据 '''

        open_file = open(self.data_path, 'w', encoding='utf-8')
        open_file.write(json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False))
        open_file.close()
