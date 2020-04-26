import json

from selenium import webdriver

from framework.aworkflow.baseTester import BaseTester


"""
一个测试工作者
"""


class Tester(BaseTester):
    """
    一个测试工作者

    接受的参数

    file_path: list 一个文件列表

    sheet_name: string 想要读取的sheet页面名称

    ui_command_runner: 一个ui命令执行器

    **kwargs：{row_list:[], row_start:int, row_end:int}

    """

    def __init__(self,
                 file_path=None,
                 sheet_name=None,
                 ui_command_runner=None,
                 **kwargs):
        super().__init__(file_path,
                         sheet_name=sheet_name,
                         ui_command_runner=ui_command_runner,
                         **kwargs)
        pass

    """
    仅检测受查异常，不运行
    """

    def check(self):
        # 构建运行时
        self._create_runtime()
        # 执行检查
        self._run_check_exception()
        # 输出报告
        self.report()
        pass

    """
    开始执行工作
    """

    def start(self):
        # 构建运行时
        self._create_runtime()
        # 执行检查
        self._run_check_exception()
        # 执行用例
        self._start_ui_life_cycle()
        # 输出报告
        self.report()
        pass


