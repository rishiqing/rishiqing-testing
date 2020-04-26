#
# excel一行数据
# 这个是最基础的模板，是目前用例的第一版
#
#

from framework.output.enitity.caseFailEntity import CaseFailEntity


class CaseEntity:
    def __init__(self):
        # 用例所属模块
        self.module = None
        # 用例编号
        self.num = None
        # 用例说明、用例名称
        self.name = None
        # 前置条件
        self.condition = None
        # 测试步骤中文描述
        self.step = None
        # 预期结果，中文描述
        self.result = None
        # 页面元素 ui 测试步骤
        self.ui_tester = None
        # 页面元素 ui 测试结果验证
        self.ui_tester_result = None
        # 接口测试，测试步骤
        self.interface_tester = None
        # 接口测试，测试结果
        self.interface_tester_result = None
        # excel信息中的第几行
        self.excel_row_index = None
        # 所属的sheet页
        self.sheet_entity = None
        # 格式和语法错误，受查异常
        self.check_exception = []
        # 用例执行错误，运行时错误，非受查异常
        self.uncheck_exception = []
        # ui测试命令列表
        self.command_list = []
        pass

    def row_num_content(self):
        return '第'+ str(self.excel_row_index) + "行,"

    """
    存在严重异常，需要根据这个状态判断用例是否需要继续执行
    """
    def has_error_exception(self):
        result = False
        for e in self.check_exception:
            if e.is_error():
                result = True
                return result
        if not result:
            for e in self.uncheck_exception:
                if e.is_error():
                    result = True
                    return result
        return result
