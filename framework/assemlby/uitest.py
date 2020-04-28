import os

from selenium import webdriver

from framework.common import fileUtil
from framework.testing.tester import Tester
from framework.testing.ui.selenium.seleniumCommandRunner import SeleniumCommandRunner

"""
测试全部用例
"""
def test_all():
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
    command_runner = SeleniumCommandRunner(driver, 'https://www.rishiqing.com')
    path = fileUtil.get_case_path('LoginCase.xlsx')
    tester = Tester(path, None, command_runner)  # 读取整个excel
    tester.start()
    driver.quit()
    pass


