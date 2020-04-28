
# 创建一个web浏览器驱动器
import _thread
import os
import threading

from selenium import webdriver

from framework.common import fileUtil
from framework.testing.tester import Tester
from framework.testing.ui.selenium.seleniumCommandRunner import SeleniumCommandRunner
from framework.testing.uiTesterDebugger import UiTesterDebugger

"""
example 1: 运行单独一条用例
"""
"""第一步，创建一个浏览器驱动"""
driver = webdriver.Chrome()
"""第二步，创建一个UI测试命令解析者"""
ui_command_runner = SeleniumCommandRunner(driver, 'https://www.rishiqing.com')
"""第三步，指定测试用例命令"""
str='[{"action":[{"homePage":""}]}, {"element":"link_text=登录","action":[{"click":""}]}, {"element":"name=username",' \
    '"action":[{"click":""},{"clear":""},{"sendKey":"11111111111"}]}, {"element":"name=password","action":[{' \
    '"click":""},{"clear":""},{"sendKey":"123456ab"}]}, {"element":"css=.logo-container~button","action":[{' \
    '"click":""}]}, {"element":"css=.error-msg>span","action":[{"check":"用户名或密码错误"},{"sleep": 10}]}] '
"""第四步，创建一个测试调试器"""
debugger = UiTesterDebugger()
"""第五步，启动调试器，并指定 ”测试用例命令“ 和 ”命令解析器“ """
debugger.start(str, ui_command_runner)
"""第六步，运行完毕，需要关闭浏览器"""
driver.quit()



"""
example 2: 运行一个excel中的测试用例
1.需要使用指定模板，本工程目录case/example.xlsx
2.可以设置具体读取的行数，全部、指定行数、
"""
"""第一步，创建一个浏览器驱动"""
def excel():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    prefs = {
        'profile.default_content_setting_values':
            {
                'notifications': 2
            }
    }
    chrome_options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(chrome_options=chrome_options)
    """第二步，创建一个UI测试命令解析者"""
    command_runner = SeleniumCommandRunner(driver, 'https://www.rishiqing.com')
    """第三步，确定excel文件路径"""
    path = fileUtil.get_case_path('LoginCase.xlsx')
    """
    第四步，创建一个tester工作者
    参数：
        path：路径
        sheet_name: sheet标签页名称
        command_runner: 命令解析器
        row_list：读取指定列表行数
        row_start、row_end：读取指定范围行数
    """
    tester = Tester(path, None, command_runner)  # 读取整个excel
    # tester = Tester(path, None, command_runner, row_list=[9,10,20])         # 读取指定列表行数
    # tester = Tester(path, None, command_runner, row_start=9, row_end=20)    # 读取指定范围行数
    """第五步，进行基本检查，可以检查出基本错误和警告(可选)"""
    # tester.check()
    """第六步，启动测试者"""
    tester.start()
    """第七步，运行完毕，需要关闭浏览器"""
    driver.quit()
    pass

excel()
# for i in range(5):
#     thread = threading.Thread(target=excel,args = (__file__,))
#     thread.start()
#     pass
