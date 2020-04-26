import time

from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from framework.common.log.LogException import error_log
from framework.common.util import util
from selenium.webdriver.support import expected_conditions as EC

"""
Selenium驱动抽象类
"""


class SeleniumCommandRunner2 :
    def __init__(self, driver):
        self.driver = driver
        self.command_entity = None
        self.fail_log = None

    def run(self, command_entity):
        print("[log-debug]:command:" + command_entity.command)
        self.command_entity = command_entity
        try:
            # dom名命令
            doms = None
            if command_entity.element_selector:
                # 前置条件，如睡眠等，需要提前运行
                dom = self.run_before_condition(command_entity)
                if dom:
                    doms = [dom]
                else:
                    # 有元素选择器，需要获取元素
                    doms = self.run_dom(command_entity)
                if doms is None:
                    self.fail_log = "命令" + command_entity.command + " 未找到有效命令"
                if doms.__len__() == 0:
                    self.fail_log =  "命令"+ command_entity.command + " 未找到任何元素"
            if command_entity.value is not None:
                # 需要验证的value
                self.run_value(doms, command_entity.value)
            if command_entity.action is not None:
                # 不需要元素的action
                self.run_no_ele_action(command_entity.action)
                # 需要元素的action
                self.run_action(doms, command_entity.action)
        except ElementNotInteractableException as e:
            self.fail_log =   "命令" + command_entity.command + " 元素不可互动 " + str(e),
        except BaseException as e:
            self.fail_log =  "命令" + command_entity.command + " 产生异常 " + str(e)
        else:
            pass
        return self.fail_log

    def run_before_condition(self, command):
        dom = None
        action = command.action
        if action is not None:
            for one in action:
                if util.similar('sleep', one.name):
                    condition = self.get_locate(command)
                    dom = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(condition))
                if util.similar('deleteCookies', one.name):
                    self.driver.delete_all_cookies()
        return dom

    def run_dom(self, command):
        doms = None
        selector = command.element_selector
        value = command.element_value
        if util.similar('id',selector):
            doms = self.driver.find_elements_by_id(value)
        elif util.similar('name',selector):
            doms = self.driver.find_elements_by_name(value)
        elif util.similar('css_selector',selector):
            doms = self.driver.find_elements_by_css_selector(value)
        elif util.similar('link_text',selector):
            doms = self.driver.find_elements_by_link_text(value)
        elif util.similar('xpath', selector):
            doms = self.driver.find_elements_by_xpath(value)
        elif util.similar('partial_link_text', selector):
            doms = self.driver.find_elements_by_partial_link_text(value)
        elif util.similar('tag_name', selector):
            doms = self.driver.find_elements_by_tag_name(value)
        elif util.similar('class_name', selector):
            doms = self.driver.find_elements_by_class_name(value)
        return doms

    def run_value(self, doms, command):
        if not len(doms):
            return
        if command.value is None:
            return
        for dom in doms:
            if not dom.text == command.value:
                self.fail_log =  "命令" + command.command + "无法完全匹配value值"

    def run_action(self, doms, action):
        for one in action:
            self.run_one_action(doms, one)

    def run_one_action(self, doms, command_action):
        # 合法性检测，其实不该在这，应该在受查异常中进行检测，但受查异常目前只写了通用基类，没有写单属于selenium的受查异常类
        self.action_value_parse(command_action)
        if doms:
            for dom in doms:
                if util.similar('click', command_action.name):
                    dom.click()
                elif util.similar('send_keys', command_action.name):
                    dom.send_keys(command_action.value)
                elif util.similar('clear', command_action.name):
                    dom.clear()
                elif util.similar('is_selected', command_action.name):
                    result = dom.is_selected()
                    if util.similar('false', command_action.value):
                        if result:
                            self.fail_log = "命令" + self.command_entity.command + "选择状态判断错误，当前是"+ result + "期待是false"
                    elif util.similar('true', command_action.value):
                        if not result:
                            self.fail_log = "命令" + self.command_entity.command + "选择状态判断错误，当前是"+ result + "期待是true"
        pass



    def run_no_ele_action(self, command_action):
        for action in command_action:
            if util.similar('sleep', action.name):
                # sleep 命令暂时不生效, 现在是全局等待上限时间10秒
                #time.sleep(command_action.value)
                #self.driver.implicity_wait(10)
                #WebDriverWait(self.driver, 10)
                #dom = self.driver.find_element_by_link_text("登录")
                #WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "日程")))
                #WebDriverWait(self.driver, 10).until(EC.presence_of_element_located())
                pass
            if util.similar('logout', action.name):
                self.logout()
        pass

    def action_value_parse(self, command_action):
        value = command_action.value
        if util.similar_find_in("keys.", value) :
            args = value.split('.')
            keypress = Keys.__dict__[args[1]]
            if keypress is None:
                self.fail_log =  "命令" + self.command_entity.command + "action 值："+value+", 无法在selenium中找到对应属性"
                return
            command_action.value = keypress
        pass

    def get_locate(self, command):
        doms = None
        selector = command.element_selector
        value = command.element_value
        if util.similar('id', selector):
            doms = (By.ID, value)
        elif util.similar('name', selector):
            doms = (By.NAME, value)
        elif util.similar('css_selector', selector):
            doms = (By.CSS_SELECTOR, value)
        elif util.similar('link_text', selector):
            doms = (By.LINK_TEXT, value)
        elif util.similar('xpath', selector):
            doms = (By.XPATH, value)
        elif util.similar('partial_link_text', selector):
            doms = (By.PARTIAL_LINK_TEXT, value)
        elif util.similar('tag_name', selector):
            doms = (By.TAG_NAME, value)
        elif util.similar('class_name', selector):
            doms = (By.CLASS_NAME, value)
        return doms


    def logout(self):
        dom1 = self.driver.find_elements_by_class_name("user-profile")
        if len(dom1):
            for one in dom1:
                one.click()
                dom2 = self.driver.find_element_by_link_text("退出登录")
                dom2.click()
        pass