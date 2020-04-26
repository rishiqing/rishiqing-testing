#!/usr/bin/python
# -*- coding: utf-8 -*-
# 入口方法，一切用例从这里调用
# import rishiqing.case.common.login as loginCase
# import rishiqing.case.todo.todoCommon as todoCommon
#
# # 执行登录
# jsonBody = loginCase.login()
# token = jsonBody["token"]
# # 执行日程用例
# todoCommon = todoCommon.TodoCommon(token)
# todoCommon.run()
# 执行计划用例

# 执行笔记用例

# 执行公司用例
from json.decoder import JSONDecodeError

from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://www.rishiqing.com')
#time.sleep(3)
dom = driver.find_elements_by_link_text('登录')[0].is_selected()
# driver.find_element_by_name('username').click()
#driver.find_element_by_name('username').text
# driver.find_element_by_name('username').send_keys('qy01@qq.com')
# # driver.find_element_by_name('password').click()
#driver.find_element_by_name('password').send_keys(Keys.TAB)
# driver.find_element_by_css_selector('button:nth-child(5)').click()
# driver.find_elements_by_class_name()
#
# print(driver.title)
import os
#
import  pandas as pd

from framework.input.converter.excelRowPandasConverter import PandasConverter
#
#path = os.path.dirname(__file__) +'/case/LoginCase3.xlsx'
#xlsx = pd.ExcelFile(path)
#df = pd.read_excel(xlsx, sheet_name=None)
#for i in df:
#   print(df[i].columns)
#
# converter = PandasConverter(df)
# projectEntity = converter.convert()
#
# for sheet  in projectEntity.sheet_list:
#    print(sheet.name)
#    for case in sheet.case_list :
#       print(case.num)


# converter = PandasConverter(df)
# entityList = converter.convert()
# for entity in entityList:
#     print(entity.excel_row_index)

# 根据指定类

# 运行一个完整的用例，需要知道的列
#1.用例编号， 页面元素， 页面元素结果  接口测试Request， 接口测试结果

# 一个用例报告需要用到的列
# 全部 + 报错结果


# import json
#
# data = '[{"element":"1","value":"2","action":"3"},{"element":"4","value":"5","action":"6"}]'
# data2 = '[{"element":"1","value":"2","action":"3"},{"element":"4","value":"5",action:"6"}]'
#
# try:
#    j=json.loads(data2)
# except JSONDecodeError :
#    print("1")
# except BaseException:
#    print("2")
# else:
#    pass


