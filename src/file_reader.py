# -*- coding: utf-8 -*-

"""
    文件读取操作
"""

import os
from zlib import crc32
from hashlib import md5

class FileReader():
    ''' 文件读取操作 '''

    def walk_folder(self, folder):
        ''' 遍历文件夹 '''

        file_list = []
        for root, dirs, files in os.walk(folder):
            for file in files:
                file_list.append(os.path.join(root, file))
        return file_list

    def code_folder(self, folder):
        ''' 为文件夹生成唯一标识码 '''

        file_list = self.walk_folder(folder)

        file_str = ''
        for file in file_list:
            file_str += file + ';'

        code_len = len(file_str)
        code_crc32 = crc32(file_str.encode('utf-8'))
        code_md5 = md5(file_str.encode('utf-8')).hexdigest()
        code = str(code_crc32) + '-' + str(code_md5) + '-' + str(code_len)

        return code

    def code_file(self, file):
        ''' 为文件生成唯一标识码 '''

        code_size = os.path.getsize(file)
        open_file = open(file, 'rb').read(1024 * 1024)
        code_crc32 = crc32(open_file)
        code_md5 = md5(open_file).hexdigest()
        code = str(code_crc32) + '-' + str(code_md5) + '-' + str(code_size)
        return code
