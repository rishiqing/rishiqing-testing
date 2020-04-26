import time
import rishiqing.constants.url as url

class TodoCommon (BaseCase.BaseCase):
    commonParam = {
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

    def run(self):
        for key in self.test_cases:
            case = self.test_cases[key]
            self.add_parameters(case, self.commonParam)
            self.add_url(case, url.TODO)
            self.exec_case(case)
