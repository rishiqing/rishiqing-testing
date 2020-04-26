"""
用例执行失败时保存的信息
隶属于caseEntity
"""


class CaseFailEntity:
    # ui测试检测，错误列表
    ui_tester_errors = []

    ui_tester_result_errors = []
    # 接口测试检测，错误列表
    interface_tester_errors = []

    interface_tester_result_errors = []

    def has_ui_fail(self):
        return self.ui_tester_errors.__len__() > 0