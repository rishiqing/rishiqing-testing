"""
ui 测试助手
"""
from selenium import webdriver

from framework.aworkflow.baseTester import BaseTester
from framework.aworkflow.entity.caseEntity import CaseEntity
from framework.common.complie.commandCompile import CommandCompile
from framework.testing.ui.selenium.seleniumCommandRunner import SeleniumCommandRunner

"""
ui 测试调试工具
可以直接运行一个json用例
"""


class UiTesterDebugger(BaseTester):

    def __init__(self):
        super().__init__()
        pass
    """
    运行一个case

    case_string:传入一个用例接送
    command_runner:传入一个命令运行器，默认为selenum chrome
    """

    def start(self, case_string, command_runner=None):
        # 未来方便，如果没有传命令执行器，则直接用selenium chrome
        # if command_runner is None:
        #     driver = webdriver.Chrome()
        #     driver.get('https://www.rishiqing.com')
        #     self.ui_command_runner = SeleniumCommandRunner(driver)
        self.ui_command_runner = command_runner
        # 字符串转换为命令
        case = CaseEntity()
        # 设置一个行数的默认值
        case.num = 1
        case.excel_row_index = 1
        case.ui_tester = case_string
        # 添加到工作流种
        self.case_list.append(case)
        self._case_life_cycle()
        # 执行检查
        self._run_check_exception()
        # 执行用例
        self._start_ui_life_cycle()
        # 输出报告
        self.report()
        pass
