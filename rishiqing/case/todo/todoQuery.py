import rishiqing.constants.url as url
import time

class TodoQuery (BaseCase.BaseCase):
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
        "单日case#1": {
            "parameters": {
                'name': "单日任务 - case#1",
                'memberIds': "2880",
                'startDate': "2019.04.02",
                'endDate': '2019.04.01',
            }
        }
    }

    def run(self):
        for key in self.test_cases:
            case = self.test_cases[key]
            self.add_parameters(case, self.commonParam)
            self.add_url(case, url.TODO)
            self.exec_case(case)