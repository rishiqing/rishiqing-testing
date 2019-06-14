#!/usr/bin/python
# -*- coding: utf-8 -*-
# 入口方法，一切用例从这里调用
import rishiqing.case.common.login as loginCase
import rishiqing.case.todo.todoCommon as todoCommon

# 执行登录
jsonBody = loginCase.login()
token = jsonBody["token"]
# 执行日程用例
todoCommon = todoCommon.TodoCommon(token)
todoCommon.run()
# 执行计划用例

# 执行笔记用例

# 执行公司用例


