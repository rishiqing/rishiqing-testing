import abc
import framework.util.util as util
import framework.network.http_request as  httpRequest
# 用例基础模板类
# 用例需要继承此类，并且实现run方法
class  BaseCase(metaclass=abc.ABCMeta): #抽象类
    token:''

    def __init__(self, token):
        self.token = token

    @abc.abstractmethod  #抽象方法
    def run(self):
        return

    # 工具方法，通过传入字典，然后直接执行
    def exec_case(self, case_dict={}):
        url = case_dict["url"] if ("url" in case_dict) else ""
        header = case_dict["header"] if ("header" in case_dict) else {}
        parameters = case_dict["parameters"] if ("parameters" in case_dict) else {}
        header["token"] = self.token
        response = httpRequest.post_json(url, parameters, header)
        body = httpRequest.getJson(response)
        print("==" + " 用例" + parameters["name"] + " 接口: " + url + " 参数" + str(parameters) + " +++++++++++++返回结果++++++++++" + str(body) + "==")
        return body

    # 工具方法，可以向caseDict 中的parameter节点 加入 mapB的内容
    def add_parameters(self, case_dict ={}, dict_b={}) :
        parameters = case_dict["parameters"] if ("parameters" in case_dict) else {}
        util.mergeDict(parameters, dict_b)
        return case_dict

    def add_header(self, case_dict={}, dict_b={}):
        header = case_dict["header"]  if ("header" in case_dict) else {}
        util.mergeDict(header, dict_b)
        return case_dict

    def add_url(self, case_dict={}, url=""):
        case_dict["url"] = url
        return case_dict