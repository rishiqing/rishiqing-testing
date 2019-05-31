#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import json
import time
import framework.network.http_request as  httpRequest
import rishiqing.constants.url as url
import rishiqing.case.common.login as loginCase
import rishiqing.case.todo.todoCommon as todoCommonCase

# 执行登录
loginCase.login()

# 执行日程用例
todoCommonCase.test_cases


# 执行计划用例

# 执行笔记用例

# 执行公司用例










# 2. 创建任务

def create_task(token, parameters):
    
    url = "https://beta.rishiqing.com/task/v1/todo"
    #payload = "{\"name\":\"" + name + "\",\"isInbox\":false,\"priority\":1,\"startDate\":\"2019.03.24\",\"endDate\":\"2019.03.24\",\"clock\":{},\"memberIds\":\"2880\",\"isOpenToMember\":false,\"todoLabelIds\":\"\",\"responsibilityId\":\"\"}"
    
    payload = { 
        'dates': "",
        'rrule': "",
        'memberIds': "2880",
        'isInbox': False, 
        'isOpenToMember': False, 
        'clock': {}, 
        'priority': 1, 
        'responsibilityId': "", 
        'startDate': time.strftime("%Y.%m.%d"), 
        'endDate': time.strftime("%Y.%m.%d"), 
        'todoLabelIds': "",
    }
    payload.update(parameters)
    
    headers = {
        'token': token,
        'cache-control': "no-cache"
    }
    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
    return response


