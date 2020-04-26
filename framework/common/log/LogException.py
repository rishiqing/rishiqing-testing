class LogException:
    __level_list=['info', 'warn', 'error']

    def __init__(self):
        self.level: None
        self.content: None

    def is_warn(self):
        if self.level == 'warn':
            return True
        return False

    def is_error(self):
        if self.level == 'error':
            pass
pass


def record_log(level, content):
    log = LogException()
    log.level = level
    log.content = content
    return log


def warn_log(content, exception=None):
    if exception:
        content = content + str(exception.args) + ',文件:' + str(exception.__traceback__.tb_frame.f_globals["__file__"]) + ',行数' + str(exception.__traceback__.tb_lineno)
    return record_log('warn', content)



def error_log(content, exception=None):
    if exception:
        content = content + str(exception.args) + ',文件:' + str(exception.__traceback__.tb_frame.f_globals["__file__"]) + ',行数' + str(exception.__traceback__.tb_lineno)
    return record_log('error', content)