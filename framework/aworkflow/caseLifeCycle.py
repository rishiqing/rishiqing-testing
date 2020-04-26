"""
用例生命周期管理
1.用例生成
2.用例受查异常检测,转化为可执行命令对象
3.用例执行, 并记录非受查异常记录
5.用例执行报告
"""
from framework.aworkflow.checkException import CheckException
from framework.aworkflow.uiTester import UiTester
from framework.common.complie.commandCompile import CommandCompile
from framework.common.log.LogException import error_log


class CaseLifeCycle:
    def __init__(self, case):
        # 用例
        self.case = case
        # 受查异常(预执行异常)
        self.check_exception = []
        # 非受查异常(运行时异常)
        self.uncheck_exception = []

    """
    执行受查异常检测(预执行异常)
    1.完整性检测
    2.语法格式错误
    """
    def run_check_exception(self):
        # 完整性检查
        check = CheckException(self.case)
        self.check_exception.extend(check.validate())
        if self.has_error_exception():
            return
        # 命令编译+语法检查,如果写了用例才运行解释器
        if self.case.ui_tester:
            compiler = CommandCompile(self.case.ui_tester)
            self.case.command_list = compiler.compile()
            if compiler.exception:
                self.check_exception.append(compiler.exception)
        self.case.check_exception.extend(self.check_exception)
        pass

    """
    执行用例
    1.需要一个参数，指定执行器
    2.执行的过程种执行非受查异常记录
    """
    def exec(self, command_runner):
        print("[info]用例:" + self.case.row_num_content() + "开始执行")
        if command_runner is None:
            raise Exception("用例生命周期内缺少命令运行器")
            return
        # 存在命令才执行
        if self.case.command_list and  len(self.case.command_list):
            ui_tester = UiTester(self.case, command_runner)
            ui_tester.run()
            if ui_tester.exception:
                self.uncheck_exception.append(ui_tester.exception)
        # 记录非受查异常
        self.case.uncheck_exception.extend(self.uncheck_exception)
        pass

    """
    输出报告
    """
    def report(self):

        if not len(self.check_exception) and not len(self.uncheck_exception):
            print("[info]用例:" + self.case.row_num_content() +"无异常")
            return
        for log in self.check_exception:
            print("[" + log.level + "]" +"用例:" + self.case.row_num_content() + log.content)
        for log in self.uncheck_exception:
            print("[" + log.level + "]" +"用例:" + self.case.row_num_content() + log.content)
        pass

    def has_error_exception(self):
        for e in self.check_exception:
            if e.is_error():
                return True
        for e in self.uncheck_exception:
            if e.is_error():
                return True
        return False