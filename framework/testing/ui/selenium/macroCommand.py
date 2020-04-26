"""
提前定义的宏命令
"""
def mc_logout(driver):
    dom1 = driver.find_elements_by_class_name("user-profile")
    if len(dom1):
        for one in dom1:
            one.click()
            dom2 = driver.find_element_by_link_text("退出登录")
            dom2.click()
    pass

"""
跳转到首页
"""
def mc_homepage(driver, url):
    # 先执行退出
    mc_logout(driver)
    # 清除cookie
    driver.delete_all_cookies()
    # 页面跳转
    driver.get(url)
    pass

"""
跳转到首页，但保留cookie
"""
def mc_homepage_with_cookie(driver, url):
    # 先执行退出
    mc_logout(driver)
    # 页面跳转
    driver.get(url)
