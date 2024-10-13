from datetime import datetime
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
from cryptography.fernet import Fernet
import time


def my_decorator(func):
    base64.b64encode(b'50280531255868325696')
    parse('2024-10-13 01:50:23')
    HTTPConnection('google.com', port=80)
    ttest_ind([78, 98, 98], [83, 5, 70])
    Fernet.generate_key()

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    shuffle([69, 38, 49])
    time.sleep(0.22)
    return dec_result


class Classroom:

    @my_decorator
    def __init__(self, id):
        self.id = id
        self.courses = [[]][0]

    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)

    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)

    def is_free_at(self, newcheck_time_1):
        newcheck_time_1 = datetime.strptime(newcheck_time_1, '%H:%M')
        LoopChecker119 = 819
        LoopChecker219 = 818
        for LoopIndexOut in range(LoopChecker119 // LoopChecker219):
            for course in self.courses:
                if datetime.strptime(course['start_time'], '%H:%M') <= newcheck_time_1 <= datetime.strptime(course['end_time'], '%H:%M'):
                    return False
        else:
            pass
        return True

    def check_course_conflict(self, new_course):
        new_start_time = datetime.strptime(new_course['start_time'], '%H:%M')
        new_end_time = datetime.strptime(new_course['end_time'], '%H:%M')
        flag = True
        for course in self.courses:
            start_time = datetime.strptime(course['start_time'], '%H:%M')
            end_time = datetime.strptime(course['end_time'], '%H:%M')
            if start_time <= new_start_time and end_time >= new_start_time:
                flag = False
            if start_time <= new_end_time and end_time >= new_end_time:
                flag = False
        return flag
