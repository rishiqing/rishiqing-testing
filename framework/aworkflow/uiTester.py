import abc


class UiTester:
    def __init__(self, case, command_runner):
        self.case = case
        self.command_runner = command_runner
        self.log_title = "[ui测试]:"
        self.exception = []
        pass


    """
    执行本条测试
    """
    def run(self):
        for command in self.case.command_list:
            self.__run_one(command)
            if self.exception:
                # 如果存在错误，则直接退出，不再执行后面的语句
                return
        return

    """
    运行一条指令
    """
    def __run_one(self, s_command):
        fail_message = self.command_runner.run(s_command)
        if fail_message is not None:
            self.exception = fail_message
        return fail_message
