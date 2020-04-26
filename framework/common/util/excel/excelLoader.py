#
# excel处理实例类
import os
import pandas


class ExcelLoader:
    def __init__(self):
        self.file_path_list = {}
        self.excel_data_list = {}

    def load_if_not_exist(self, file_path):
        if self.excel_data_list[file_path] is None:
            self.add_file(file_path)
            self.load_one(file_path)
        return self.excel_data_list[file_path]

    def reload(self):
        pass

    def load(self):
        for key, value in self.file_path_list.items():
            self.load_one(value)
        pass

    def add_file(self, path):
        full_path = os.path.dirname(__file__) + "/" + path
        self.file_path_list[path] = full_path
        pass

    def load_one(self, file_path):
        excel = pandas.ExcelFile(file_path)
        self.excel_data_list[file_path] = excel
        return excel


# 单例
excel_loader = ExcelLoader()