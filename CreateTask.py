#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import json
import time

# 1. 登录

def login(j_username = "gs01@qq.com", j_password = "123456"):
    url = "https://beta.rishiqing.com/task/j_spring_security_check"

    payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"j_username\"\r\n\r\n" + j_username + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"j_password\"\r\n\r\n" + j_password + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
    headers = {
        'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
        'cache-control': "no-cache"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    body = json.loads(response.text)
    return body


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

    # payload = {
    #     'name': name,
    #     'isOpenToMember': isOpenToMember,
    #     'isInbox': isInbox,
    #     'priority': priority,
    #     'endDate': endDate,
    #     'startDate': startDate,
    #     'memberIds': memberIds,
    #     'responsibilityId': responsibilityId,
    #     'todoLabelIds': todoLabelIds,
    #     'clock': clock
    # }
    # print("payload: ", payload)
    
    headers = {
        'token': token,
        'cache-control': "no-cache"
    }
    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
    return response




# 3. 准备数据

def run_case(parameters = {}, key = 1):

    # 4. 运行 case
    login_body = login()
    response = create_task(login_body['token'], parameters)

    # 5. 生成报表
    body = response.json()
    # print("body: ", body)
    if value_is_the_same(body, parameters): #body == parameters
        print('{}:测试成功。json数据为:{}'.format(key, parameters))
    else:
        print("create task failed")

def value_is_the_same(dict1, dict2):
    result = True
    for key in dict2:
        if key in dict1.keys():
            result = result & (dict1[key] == dict2[key])
    return True



test_cases = {
    ### 单日任务
    # 新建 未来 的 单日 任务
    "单日case#1": {
        "parameters": {
            'name': "单日任务 - case#1",
            'memberIds': "2880",
            'startDate': "2019.04.02",
            'endDate': '2019.04.01',
        }
    }, 
    # 在 今天 新建 单日 任务
    "单日case#2": {
        "parameters": {
            'name': "单日任务 - case#2",
            'memberIds': "2880",
        }
    },
    # 在 过去 新建 单日 任务
    "单日case#3": {
        "parameters": {
            'name': "单日任务 - case#3",
            'memberIds': "2880",
            'startDate': "2019.03.30",
            'endDate': "2019.03.30",
        }
    },
    ### 起止任务
    # 新建 将来 的 起止 任务
     "起止case#1": {
        "parameters": {
            'name': "起止任务 - case#1",
            'memberIds': "2880",
            'startDate': "2019.04.02",
            'endDate': "2019.04.31",
        }
    },
    # 在 过去 新建 起止 任务
     "起止case#2": {
        "parameters": {
            'name': "起止任务 - case#2",
            'memberIds': "2880",
            'startDate': "2019.03.29",
            'endDate': "2019.03.31",
        }
    },
    # 新建 截止日期是今天 的 起止 任务
     "起止case#3": {
        "parameters": {
            'name': "起止任务 - case#3",
            'memberIds': "2880",
            'startDate': "2019.03.01",
        }
    },
    # 新建 开始日期是今天 的 起止 任务
     "起止case#4": {
        "parameters": {
            'name': "起止任务 - case#4",
            'memberIds': "2880",
            'endDate': "2019.04.31",
        }
    },
    ### 多日任务
    # 在 过去 新建 多日 任务
     "多日case#1": {
        "parameters": {
            'name': "多日任务 - case#1",
            'memberIds': "2880",
            'dates': "2019.03.01,2019.03.15,2019.03.30",
        }
    },
    # 新建从 今天开始 的 多日 任务
     "多日case#2": {
        "parameters": {
            'name': "多日任务 - case#2",
            'memberIds': "2880",
            'dates': "2019.04.01,2019.04.15,2019.04.30",
        }
    },
    # 新建到 今天结束 的 多日 任务
     "多日case#3": {
        "parameters": {
            'name': "多日任务 - case#3",
            'memberIds': "2880",
            'dates': "2019.03.01,2019.03.15,2019.04.01",
        }
    },
    # 在 未来 新建 多日 任务
     "多日case#4": {
        "parameters": {
            'name': "多日任务 - case#4",
            'memberIds': "2880",
            'dates': "2019.04.02,2019.04.15,2019.04.30",
        }
    },
    ### 按天重复
    # 在 过去 新建按 天 重复的任务
     "按天过去（有截止日期）case#1": {
        "parameters": {
            'name': "按天过去（有截止日期） - case#1",
            'memberIds': "2880",
            'rrule': "FREQ=DAILY;INTERVAL=1;UNTIL=20190430T000000Z",
            'startDate': "2019.03.30",
            'endDate': "2019.03.30",
        }
    },
     "按天过去（无截止日期）case#2": {
        "parameters": {
            'name': "按天过去（无截止日期） - case#2",
            'memberIds': "2880",
            'rrule': "FREQ=DAILY;INTERVAL=1",
            'startDate': "2019.03.30",
            'endDate': "2019.03.30",
        }
    },
    # 在 今天 新建按 天 重复的任务
     "按天今天（有截止日期）case#1": {
        "parameters": {
            'name': "按天今天（有截止日期） - case#1",
            'memberIds': "2880",
            'rrule': "FREQ=DAILY;INTERVAL=1;UNTIL=20190430T000000Z",
        }
    },
     "按天今天（无截止日期）case#2": {
        "parameters": {
            'name': "按天今天（无截止日期） - case#2",
            'memberIds': "2880",
            'rrule': "FREQ=DAILY;INTERVAL=1",
        }
    },
    # 在 未来 新建按 天 重复的任务
     "按天未来（有截止日期）case#1": {
        "parameters": {
            'name': "按天未来（有截止日期） - case#1",
            'memberIds': "2880",
            'rrule': "FREQ=DAILY;INTERVAL=1;UNTIL=20190430T000000Z",
            'startDate': "2019.04.02",
            'endDate': "2019.04.02",
        }
    },
     "按天未来（无截止日期）case#2": {
        "parameters": {
            'name': "按天未来（无截止日期） - case#2",
            'memberIds': "2880",
            'rrule': "FREQ=DAILY;INTERVAL=1",
            'startDate': "2019.04.02",
            'endDate': "2019.04.02",
        }
    },
    ### 按周重复
    # 在 未来 新建按 周 重复的任务
     "按周未来（有截止日期）case#1": {
        "parameters": {
            'name': "按周未来（有截止日期） - case#1",
            'memberIds': "2880",
            'rrule': "FREQ=WEEKLY;INTERVAL=1;UNTIL=20190430T000000Z;BYDAY=MO,TU,WE,TH,FR,SA,SU",
            'startDate': "2019.04.02",
            'endDate': "2019.04.02",
        }
    },
     "按周未来（无截止日期）case#2": {
        "parameters": {
            'name': "按周未来（无截止日期） - case#2",
            'memberIds': "2880",
            'rrule': "FREQ=WEEKLY;INTERVAL=1;BYDAY=MO,TU,WE,TH,FR,SA,SU",
            'startDate': "2019.04.02",
            'endDate': "2019.04.02",
        }
    },
    # 在 今天 新建按 周 重复的任务
     "按周今天（有截止日期）case#1": {
        "parameters": {
            'name': "按周今天（有截止日期） - case#1",
            'memberIds': "2880",
            'rrule': "FREQ=WEEKLY;INTERVAL=1;UNTIL=20190430T000000Z;BYDAY=MO,TU,WE,TH,FR,SA,SU",
        }
    },
     "按周今天（无截止日期）case#2": {
        "parameters": {
            'name': "按周今天（无截止日期） - case#2",
            'memberIds': "2880",
            'rrule': "FREQ=WEEKLY;INTERVAL=1;BYDAY=MO,TU,WE,TH,FR,SA,SU",
        }
    },
    # 在 过去 新建按 周 重复的任务
     "按周过去（有截止日期）case#1": {
        "parameters": {
            'name': "按周过去（有截止日期） - case#1",
            'memberIds': "2880",
            'rrule': "FREQ=WEEKLY;INTERVAL=1;UNTIL=20190430T000000Z;BYDAY=MO,TU,WE,TH,FR,SA,SU",
            'startDate': "2019.03.01",
            'endDate': "2019.03.01",
        }
    },
     "按周过去（无截止日期）case#2": {
        "parameters": {
            'name': "按周过去（无截止日期） - case#2",
            'memberIds': "2880",
            'rrule': "FREQ=WEEKLY;INTERVAL=1;BYDAY=MO,TU,WE,TH,FR,SA,SU",
            'startDate': "2019.03.01",
            'endDate': "2019.03.01",
        }
    },
    ### 按月重复
    # 在 过去 新建按 月 重复的任务
     "按月过去（有截止日期）case#1": {
        "parameters": {
            'name': "按月过去（有截止日期） - case#1",
            'memberIds': "2880",
            'rrule': "FREQ=MONTHLY;INTERVAL=1;UNTIL=20190531T000000Z;BYMONTHDAY=-1,1,15,31",
            'startDate': "2019.03.01",
            'endDate': "2019.03.01",
        }
    },
     "按月过去（无截止日期）case#2": {
        "parameters": {
            'name': "按月过去（无截止日期） - case#2",
            'memberIds': "2880",
            'rrule': "FREQ=MONTHLY;INTERVAL=1;BYMONTHDAY=-1,1,15,31",
            'startDate': "2019.03.01",
            'endDate': "2019.03.01",
        }
    },
    #######   此处省略按月重复在今天、未来新建的 cases   #######
    ### 按年重复
    # 在 今天 新建按 年 重复的任务
     "按年今天（有截止日期）case#1": {
        "parameters": {
            'name': "按年今天（有截止日期） - case#1",
            'memberIds': "2880",
            'rrule': "FREQ=YEARLY;INTERVAL=1;UNTIL=20300430T000000Z",
        }
    },
     "按年今天（无截止日期）case#2": {
        "parameters": {
            'name': "按年今天（无截止日期） - case#2",
            'memberIds': "2880",
            'rrule': "FREQ=YEARLY;INTERVAL=1",
        }
    },
    # 在 未来 新建 按年 重复的任务
     "按年未来（有截止日期）case#3": {
        "parameters": {
            'name': "按年未来（有截止日期） - case#3",
            'memberIds': "2880",
            'rrule': "FREQ=YEARLY;INTERVAL=1;UNTIL=203000430T000000Z",
            'startDate': "2019.04.30",
            'endDate': "2019.04,30",
        }
    },
     "按年未来（无截止日期）case#4": {
        "parameters": {
            'name': "按年未来（无截止日期） - case#4",
            'memberIds': "2880",
            'rrule': "FREQ=YEARLY;INTERVAL=1",
            'startDate': "2019.04.30",
            'endDate': "2019.04,30",
        }
    },
    # 在 过去 新建 按年 重复的任务 
    "按年过去（有截止日期）case#5": {
        "parameters": {
            'name': "按年过去（有截止日期） - case#5",
            'memberIds': "2880",
            'rrule': "FREQ=YEARLY;INTERVAL=1;UNTIL=203000430T000000Z",
            'startDate': "2018.04.30",
            'endDate': "2018.04,30",
        }
    },
     "按年过去（无截止日期）case#4": {
        "parameters": {
            'name': "按年过去（无截止日期） - case#4",
            'memberIds': "2880",
            'rrule': "FREQ=YEARLY;INTERVAL=1",
            'startDate': "2018.04.30",
            'endDate': "2018.04,30",
        }
    },
}


for key in test_cases:
    run_case(test_cases[key]["parameters"], key)

# 6. 发送报表

