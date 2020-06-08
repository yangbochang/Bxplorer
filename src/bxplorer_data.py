# -*- coding: utf-8 -*-

import json

class BxplorerData():
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        pass

    def write(self, data):
        open_file = open(self.file_path, 'w', encoding='utf-8')
        open_file.write(json.dumps(data))
        open_file.close()

