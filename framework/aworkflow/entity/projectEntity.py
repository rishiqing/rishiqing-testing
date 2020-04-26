#
# 项目实例
# 对应一个excel表格
#


class ProjectEntity:
    def __init__(self):
        # 一个excel下的全部sheet
        self.sheet_list = []
        self.case = []

    def integrity_validate(self):
        for sheet in self.sheet_list:
            sheet.integrity_validate()
        pass

    def ui_tester_format_validate(self):
        for sheet in self.sheet_list:
            sheet.ui_tester_format_validate()
        pass

    def interface_tester_format_validate(self):
        for sheet in self.sheet_list:
            sheet.interface_tester_format_validate()
        pass

    """
    获得所有用例
    """
    def get_all_case(self):
        if len(self.case):
            return self.case
        list = []
        for sheet in self.sheet_list:
            for case in sheet.case_list:
                list.append(case)
        return list

    """
    获得excel行数指定范围索引的用例
    """
    def find_case_by_index(self, range_start, range_end):
        list = []
        caseList = self.get_all_case()
        for case in caseList :
            if range_start <= case.excel_row_index <= range_end:
                list.append(case)
                pass
        return list

    """
    获得excel行数指定元组索引的用例
    """
    def find_case_by_index_args(self, case_args):
        list = []
        map = {}
        caseList = self.get_all_case()
        for case in caseList:
            map[case.excel_row_index] = case
        for case_num in case_args :
            if map.__contains__(case_num):
                list.append(map[case_num])
            pass
        return list