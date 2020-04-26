#
# excel读取对象
#
#
import pandas

from framework.common.util.excel.excelLoader import excel_loader


def read_excel(self, file_path, sheet_name=None):
    data = excel_loader.load_if_not_exist(file_path)
    self.data = pandas.read_excel(data, sheet_name=sheet_name)
    return

