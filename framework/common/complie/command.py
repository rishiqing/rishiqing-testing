
"""
常规命令
"""
from framework.common.util.util import get_dict_attr


class Command:
    def __init__(self, **kwargs):
        self.command = get_dict_attr(kwargs, 'command')
        self.element = get_dict_attr(kwargs, 'element')
        self.element_selector = get_dict_attr(kwargs, 'element_selector')
        self.element_value = get_dict_attr(kwargs, 'element_value')
        self.value = get_dict_attr(kwargs, 'value')
        self.action = get_dict_attr(kwargs, 'action')
        # 接口测试需要用到的命令
        self.url = None
        # 接口测试的请求方式
        self.method = None
        # 接口测试的的值
        self.json_value = None


    # 判断是否是睡眠命令
    def is_sleep(self):
        return False
