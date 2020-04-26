from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from framework.common.log.LogException import error_log, warn_log
from framework.common.util import util
from selenium.webdriver.support import expected_conditions as EC

from framework.common.util.util import get_int
from framework.testing.ui.selenium.macroCommand import mc_logout, mc_homepage, mc_homepage_with_cookie

"""
命令驱动器
"""


class SeleniumCommandRunner:
    dom_command_dict = {
        'id' : True,
        'name': True,
        'css_selector': True,
        'css': True,
        'link_text': True,
        'xpath': True,
        'partial_link_text': True,
        'tag_name': True,
        'class_name': True,
    }

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.command_entity = None
        # 打开浏览器
        self._open_browser()

    def run(self, command):
        try:
            print("[log-debug]:command:" + command.command)
            self.fail_log = None
            doms = None
            # 先执行的action
            dom = self._before_action(command)
            if dom:
                doms = [dom]
            if self.fail_log:
                return self.fail_log
            if command.element_selector:
                if  self.fail_log is None and doms is None:
                    # 选择dom
                    doms = self._element(command)
                    if self.fail_log:
                        return self.fail_log
            if command.value is not None:
                # value匹配判断
                self._value(doms, command)
                if self.fail_log:
                    return self.fail_log
            if command.action is not None:
                # 不需要element的action
                self._no_element_action(command)
                if self.fail_log:
                    return self.fail_log
                # 一般action
                self._action(doms, command)
                if self.fail_log:
                    return self.fail_log
        except Exception as e:
            self.create_error(command, e)
        return self.fail_log

    def _open_browser(self):
        self._open_url(self.url)

    def _open_url(self, url):
        self.driver.get(url)

    """
    条件行为命令
    """
    def _before_action(self, command):
        dom = None
        try:
            action = command.action
            # 需要元素的命令
            if command.element_selector:
                if action is not None:
                    for one in action:
                        if util.similar('sleep', one.name):
                            sleep_time = get_int(one.value)
                            if not sleep_time:
                                sleep_time = 10
                            condition = self.get_locate(command)
                            dom = WebDriverWait(self.driver, sleep_time).until(EC.presence_of_element_located(condition))
            # 不需要元素的命令
            if action is not None:
                for one in action:
                    if util.similar('deleteCookies', one.name):
                        self.driver.delete_all_cookies()
        except Exception as e:
            self.create_error(command, e)
        return dom

    @DeprecationWarning
    def _element_selector_check(self, command):
        try:
            selector = command.element_selector
            if selector:
                if not self.dom_command_dict.__contains__(selector):
                    self.create_error(command, None, '无法解析的选择器类型:' + selector)
                    return
        except Exception as e:
            print(e.args)
            self.create_error(command, e)


    """
    元素查找
    """
    def _element(self, command):
        doms = None
        try:
            selector = command.element_selector
            value = command.element_value
            if util.similar('id',selector):
                doms = self.driver.find_elements_by_id(value)
            elif util.similar('name',selector):
                doms = self.driver.find_elements_by_name(value)
            elif util.similar('css_selector',selector):
                doms = self.driver.find_elements_by_css_selector(value)
            elif util.similar('css',selector):
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
            if doms is None:
                self.create_error(command, None, " 未找到有效命令:" + selector)
            elif doms.__len__() == 0:
                self.create_error(command, None, " 选择器未找到任何元素:[" + command.element +"]")
        except Exception as e:
            self.create_error(command, e)
        return doms

    """
    值检查
    """
    def _value(self, doms, command):
        try:
            if not len(doms):
                return
            if command.value is None:
                return
            for dom in doms:
                if not dom.text == command.value:
                    self.create_error(command, None, "无法完全匹配value值")
                    return
        except Exception as e:
            self.create_error(command, e)

    """
    不需要element的action运行
    """
    def _no_element_action(self, command):
        try:
            actions = command.action
            if actions is not None:
                for action in actions:
                    if util.similar('sleep', action.name):
                        # sleep 命令暂时不生效, 现在是全局等待上限时间10秒
                        #WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "日程")))
                        pass
                    if util.similar('logout', action.name):
                        mc_logout(self.driver)
                    elif util.similar('homepage', action.name):
                        mc_homepage(self.driver, self.url)
                    elif util.similar('homepageWithCookie', action.name):
                        mc_homepage_with_cookie(self.driver, self.url)
        except Exception as e:
            self.create_error(command, e)
        pass

    """
    其余的action
    """
    def _action(self, doms, command):
        try:
            actions = command.action
            if actions is not None:
                for action in actions:
                    self.action_value_parse(action, command)
                    if doms:
                        for dom in doms:
                            if util.similar('click', action.name):
                                dom.click()
                            elif util.similar('send_keys', action.name):
                                dom.send_keys(action.value)
                            elif util.similar('clear', action.name):
                                dom.clear()
                            elif util.similar('is_selected', action.name):
                                result = dom.is_selected()
                                if util.similar('false', action.value):
                                    if result:
                                        self.create_error(command, None, "选择状态判断错误，当前是" + result + "期待是false")
                                        return
                                elif util.similar('true', action.value):
                                    if not result:
                                        self.create_error(command, None, "选择状态判断错误，当前是" + result + "期待是true")
                                        return
                            elif util.similar('check', action.name):
                                if not action.name:
                                    self.create_error(command, None, "行为check缺少检查对象")
                                    return
                                if not dom.text == action.value:
                                    self.create_error(command, None, "check行为无法完全匹配value值")
                                    return
        except Exception as e:
            self.create_error(command, e)
        pass

    """普通action的值过滤"""
    def action_value_parse(self, action, command):
        try:
            value = action.value
            if util.similar_find_in("keys.", value) :
                args = value.split('.')
                keypress = Keys.__dict__[args[1]]
                if keypress is None:
                    self.create_error(command, None, "action 值："+value+", 无法在selenium中找到对应属性")
                    return
                action.value = keypress
        except Exception as e:
            self.create_error(command, e)
        pass



    """
    运行元素等待时需要获取的元素
    """
    def get_locate(self, command):
        doms = None
        try:
            selector = command.element_selector
            value = command.element_value
            if util.similar('id', selector):
                doms = (By.ID, value)
            elif util.similar('name', selector):
                doms = (By.NAME, value)
            elif util.similar('css_selector', selector):
                doms = (By.CSS_SELECTOR, value)
            elif util.similar('css', selector):
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
        except Exception as e:
            self.create_error(command, e)
        pass
        return doms

    def create_error(self, command=None, e=None, message='出错'):
        self.fail_log = error_log('页面:' + str(self.driver.current_url)+" " +('' if command is None else "命令：" + command.command) + message, e)

    def create_warn(self, command=None, e=None, message='出错'):
        self.fail_log = warn_log('页面:' + str(self.driver.current_url)+" " + ('' if command is None else "命令：" + command.command) + message, e)