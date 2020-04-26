#!/usr/bin/python
# -*- coding: utf-8 -*-
import framework.common.network.http_request as  httpRequest

def batchRun (test_cases) :
    for key in test_cases:
        response = run(test_cases)
        check(response, key)

def run (oneCase) :
    response = {}
    # 判断请求类型
    if  oneCase.type == 'POST':
        response = httpRequest.post(oneCase.url, oneCase.parameters, oneCase.header)
    else:
        response = httpRequest.get(oneCase.url, oneCase.parameters, oneCase.header)
    return response

def check (response, oneCase, key):
    # 5. 生成报表
    body = response.json()
    # print("body: ", body)
    if value_is_the_same(body, oneCase.parameters): #body == parameters
        print('{} 接口调用成功。参数是:{}'.format(key, oneCase.parameters))
    else:
        print("create task failed")

def value_is_the_same(dict1, dict2):
    result = True
    for key in dict2:
        if key in dict1.keys():
            result = result & (dict1[key] == dict2[key])
    return True