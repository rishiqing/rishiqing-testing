#
# 一个sheet页的entity
#


class SheetEntity:
    def __init__(self):
        # 一个 sheet下的全部case
        self.case_list = []
        # 名称
        self.name = None

    def integrity_validate(self):
        for case in self.case_list:
            case.integrity_validate()
        pass

    def ui_tester_format_validate(self):
        for case in self.case_list:
            case.ui_tester_format_validate()
        pass

    def interface_tester_format_validate(self):
        for case in self.case_list:
            case.interface_tester_format_validate()
        pass
