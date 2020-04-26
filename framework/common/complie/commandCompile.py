"""
excel中的json行为命令解析器
"""
import json
from json.decoder import JSONDecodeError

from framework.common.complie.command import Command
from framework.common.complie.commandAction import CommandAction
from framework.common.log.LogException import error_log


class CommandCompile:
    keywords = {
        'element': True,
        'elements': True,
        'value': True,
        'values': True,
        'action': True
    }


    def __init__(self, command_string):
        self.command_string = command_string
        # 转换后的json
        self.command_json = None
        # 命令对象
        self.command_entity_list = []
        # 发生的错误
        self.exception = None

    """
    外部调用的转义方法
    """
    def compile(self):
        if self.command_string is None:
            return None
        # 转换为json, 转换错误则直接退出
        self._to_json()
        # 如果转换有异常，则直接退出
        if self.exception:
            return []
        self.validate()
        # 关键词检测
        if self.exception:
            return []
        # 转换为命令
        self._json_to_command()
        # 如果有错误，则不返回命令
        if self.exception:
            return []
        # 正常返回
        return self.command_entity_list

    """
    字符串转json
    """
    def _to_json(self):
        result = False
        try:
            self.command_json = json.loads(self.command_string)
            result = True
        except JSONDecodeError as e:
            self.exception = error_log("json 命令格式解析错误:", e)
            #self.exception = "json 命令格式解析错误:" + str(e)
            #self.exception_list.append(error_log("json 命令格式解析错误:", e))
        except BaseException as e:
            self.exception = error_log("json 命令解析错误:", e)
            #self.exception = "json 命令格式解析错误:"  + str(e)
            #self.exception_list.append(error_log("json 命令解析错误:", e))
        else:
            pass
        return result

    """
    编译时先验性检查
    """
    def validate(self):
        for json in self.command_json:
            for k,v in json.items():
                if not self.keywords.__contains__(k):
                    self.exception = error_log("json 命令解析错误，无法解析的命令关键字:"+ k)
                    return

    """
    json 转命令
    """
    def _json_to_command(self):
        for json in self.command_json:
            if json.__contains__('url'):
                self.command_entity_list.append(self._json_to_command_interface(json))
            else:
                self.command_entity_list.append(self._json_to_command_ui(json))
        pass


    def _json_to_command_ui(self, json_object):
        command = Command(command = json.dumps(json_object,ensure_ascii=False))
        if json_object.__contains__('element'):
            element = json_object['element']
            element_dict = self.parse_ui_element(element)
            command.element = element
            command.element_selector = element_dict['element_selector']
            command.element_value = element_dict['element_value']
        if json_object.__contains__('value'):
            if not json_object.__contains__('element'):
                self.exception = error_log("无法定位，存在value元素，但没有element元素")
                return
            command.value = json_object['value']
        if json_object.__contains__('action'):
            command.action = self.parse_ui_action(json_object['action'])
        return command

    def parse_ui_element(self, element):
        element_dict = {}
        if element is not None:
            try:
                args = element.split('=')
                element_dict = {
                    'element_selector' : args[0],
                    'element_value' : args[1]
                }
            except BaseException as e:
                self.exception = error_log("element 元素不符合规范: " + element , e)
                #self.exception = "element 元素不符合规范: " + element + str(e)
                #self.exception_list.append(error_log("element 元素不符合规范: " + element , e))
            else:
                pass
        return element_dict

    def parse_ui_action(self, action):
        command_action_list = []
        # 如果action是列表
        if type(action).__name__=='list':
            for one in action:
                for key, value in one.items():
                    command_action_list.append(self.create_action_command(key, value))
            pass
        else:
            # 如果action是对象，应该是个字典
            for key, value in action:
                command_action_list.append(self.create_action_command(key, value))
            pass
        return command_action_list

    def create_action_command(self, name, value):
        if name is not None:
            name =  name.replace(" ","")
        if value is not None and type(value).__name__=='str':
            value = value.replace(" ","")
        return CommandAction(name, value)

    def _json_to_command_interface(self, json_object):
        pass