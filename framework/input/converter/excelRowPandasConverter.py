

# 将excel转换为 excelCaseEntity对象
import copy

from framework.aworkflow.entity.caseEntity import CaseEntity
from framework.aworkflow.entity.projectEntity import ProjectEntity
from framework.aworkflow.entity.sheetEntity import SheetEntity


class PandasConverter:
    # A module
    # B num
    # C name
    # D condition
    # E step
    # F result
    # G ui_tester
    # H interface_tester
    # I interface_tester_result
    __column_mapping = {
        "A": None,
        "B": None,
        "C": None,
        "D": None,
        "E": None,
        "F": None,
        "G": None,
        "H": None,
        "I": None,
    }

    def __init__(self, pandas_data):
        self.__pandas_data = pandas_data
        self.__project_entity = ProjectEntity()

    # 执行转换
    #
    def convert(self):
        self.__all_sheet()
        return self.__project_entity

    # 遍历每个sheet页
    def __all_sheet(self):
        for i in self.__pandas_data:
            sheet = self.__pandas_data[i]
            sheet_entity = SheetEntity()
            sheet_entity.name = i
            self.__project_entity.sheet_list.append(sheet_entity)
            self.__sheet(sheet, sheet_entity)
        return

    def __sheet(self, sheet, sheet_entity):
        # 获得一个sheet的列映射关系
        mapping = self.__generate_sheet_mapping(sheet)
        # 将excel行数据转换为对象
        self.__convert_row(sheet, mapping, sheet_entity)
        return

    # 将excel行数据转换为对象
    def __convert_row(self, sheet, mapping, sheet_entity):
        index = 2 # 出去列名，应该是从第二行开始读取
        for one_row in sheet.iloc:
            row = self.__row(one_row, mapping)
            row.excel_row_index = index
            #if not math.isnan(row.num):
            sheet_entity.case_list.append(row)
            row.sheet_entity = sheet_entity
            index +=1
        pass

    # 根据映射转换为excelCaseEntity
    def __row (self, row, mapping):
        entity = CaseEntity()
        for key,value in mapping.items():
            column_value = row.iloc[value]
            self.__mapping_to_entity(entity, key, column_value)
            entity.excel_row_index = copy.copy(value)
        return entity

    # 获得一个sheet的映射关系
    def __generate_sheet_mapping (self, sheet):
        # 拷贝一个新的mapping
        mapping = self.__column_mapping.copy()
        index = 0
        for name in sheet.head(0).columns:
            # 头列的最后一个字符是key
            self.__to_column_map(mapping, name[-1], index)
            index +=1
        return mapping

    def __to_column_map(self, mapping, column_name_last_letter, index):
        for key in self.__column_mapping:
            self.__one_column_mapping(mapping, key, column_name_last_letter, index)

    @staticmethod
    def __one_column_mapping(mapping, key, last_letter, index):
        if key == last_letter:
            mapping [key] = index
        return

    @staticmethod
    def __mapping_to_entity(entity, key, value):
        if "A" == key:
            entity.module = value
            pass
        elif "B" == key:
            entity.num = value
            pass
        elif "C" == key:
            entity.name = value
            pass
        elif "D" == key:
            entity.condition = value
            pass
        elif "E" == key:
            entity.step = value
            pass
        elif "F" == key:
            entity.result = value
            pass
        elif "G" == key:
            entity.ui_tester = value
            pass
        elif "H" == key:
            entity.ui_tester_result = value
            pass
        elif "I" == key:
            entity.interface_tester = value
            pass
        elif "J" == key:
            entity.interface_tester_result = value
            pass
        pass
