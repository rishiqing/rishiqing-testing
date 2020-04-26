import abc

from pandas import read_excel

from framework.aworkflow.caseLifeCycle import CaseLifeCycle
from framework.common.util.util import get_dict_attr
from framework.input.converter.excelRowPandasConverter import PandasConverter

"""
一个测试工作者
接受的参数
    file_path: list 一个文件列表
    sheet_name: string 想要读取的sheet页面名称
    ui_command_runner: 一个ui命令执行器
逻辑：
1.根据文件列表

"""


class BaseTester(metaclass=abc.ABCMeta):
    def __init__(self,
                 file_path=None,
                 sheet_name=None,
                 ui_command_runner=None,
                 **kwargs):
        self.file_path = file_path
        self.sheet_name = sheet_name
        self.ui_command_runner = ui_command_runner
        self.row_list = get_dict_attr(kwargs,'row_list')
        self.row_start = get_dict_attr(kwargs,'row_start')
        self.row_end = get_dict_attr(kwargs,'row_end')
        # 读取到的全部项目excel列表
        self.project_list = []
        # 最终需要运行的case列表
        self.case_list = []
        # 用例生命周期列表
        self.case_life_cycle_list = []
        # 是否已经构建过运行环境
        self.has_runtime = False
    pass
    """
    构造运行环境
    """
    def _create_runtime(self):
        self._validate()
        if self.has_runtime:
            return
        # 先验检查
        self._validate()
        # 加载excel数据
        self._load()
        # 根据row获得需要运行的case
        self._filter_case()
        # 建立用例生命周期
        self._case_life_cycle()
        # 标记
        self.has_runtime= True
        pass
    """
    基础验证器
    """
    def _validate(self):
        if self.file_path is None or not len(self.file_path):
            raise Exception("file_path not found in tester")
        if self.ui_command_runner is None:
            raise Exception("ui_command_runner not found in tester")
        pass

    """
    通过file_path读取excel
    """
    def _load(self):
        if not type(self.file_path).__name__=='list':
            self.file_path = [self.file_path]
        for path in self.file_path:
               self.project_list.append(self._create_project(path))
        pass

    """
    计算需要执行的行
    """
    def _filter_case(self):
        for project in self.project_list:
            if self.row_list and len(self.row_list):
                self.case_list.extend(project.find_case_by_index_args(self.row_list))
            elif self.row_start and self.row_end:
                self.case_list.extend(project.find_case_by_index(self.row_start, self.row_end))
            else :
                self.case_list.extend(project.get_all_case())
        pass

    """
    为用例建立生命周期
    """
    def _case_life_cycle(self):
        for case in self.case_list:
            self.case_life_cycle_list.append(CaseLifeCycle(case))
        pass

    """
    执行受查异常检测
    """
    def _run_check_exception(self):
        for life in self.case_life_cycle_list:
            life.run_check_exception()

    """
    输出报告
    """
    def report(self):
        for life in self.case_life_cycle_list:
            life.report()

    """
    开始按步骤执行生命周期
    """
    def _start_ui_life_cycle(self):
        for life in self.case_life_cycle_list:
            life.exec(self.ui_command_runner)

    """
    创建一个工程
    """

    def _create_project(self, path):
        # 读取excel
        pandas = self._read_excel(path)
        # 转化为用例
        project = self.convert_to_case(pandas)
        return project

    """
    读取excel
    """

    def _read_excel(self, file_path):
        pandas = read_excel(file_path, self.sheet_name, keep_default_na=False)
        return pandas

    """
    转换为用例
    """

    @staticmethod
    def convert_to_case(pandas):
        # 得到转换类
        pandas_converter = PandasConverter(pandas)
        # 执行excel转换为case对象
        project = pandas_converter.convert()
        return project