"""
受查异常（预检测异常）
"""
import math

from framework.common.log.LogException import warn_log, error_log


class CheckException:
    def __init__(self, case):
        self.case = case
        self.exception_list = []
    pass

    def validate(self):
        self._validate()
        self._ui_tester_validate()
      #  self._interface_tester_validate()
        return self.exception_list

    # 完整性检测——基本格式检测，等级较低
    # 格式不符合，也不影响运行用例
    # 为了检查信息是否完整
    def _validate(self):
        if self.case.num is None:
            self.exception_list.append(error_log(self.case.row_num_content() + "用例编号不能为空"))
        elif math.isnan(self.case.num):
            self.exception_list.append(error_log(self.case.row_num_content() + "用例编号不能为空"))

    def _ui_tester_validate(self):
        if not self.case.ui_tester:
            self.exception_list.append(warn_log(self.case.row_num_content() + "UI测试内容不能为空"))

    def _interface_tester_validate(self):
        if not self.case.interface_tester:
            self.exception_list.append(warn_log(self.case.row_num_content() + "接口测试内容不能为空"))
