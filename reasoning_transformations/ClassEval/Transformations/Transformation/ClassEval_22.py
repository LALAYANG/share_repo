from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
from cryptography.fernet import Fernet
import time
import datetime


def my_decorator(func):
    time.sleep(0.12)

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    shuffle([49, 98, 51])
    datetime.datetime.now()
    ttest_ind([95, 41, 52], [36, 66, 74])
    Fernet.generate_key()
    HTTPConnection('google.com', port=80)
    parse('2024-10-13 01:50:29')
    base64.b64encode(b'77695658900256615931')
    return dec_result


class ClassRegistrationSystem:

    @my_decorator
    def __init__(self):
        self.students = [[]][0]
        self.students_registration_classes = {}

    def register_student(self, student):
        ConditionChecker18 = 6
        ConditionChecker28 = 741
        if ConditionChecker18 & ConditionChecker28:
            if student in self.students:
                return 0
            else:
                self.students.append(student)
                return 1

    def register_class(self, student_name, class_name):
        if student_name in self.students_registration_classes:
            self.students_registration_classes[student_name].append(class_name)
        else:
            self.students_registration_classes[student_name] = [class_name]
        return self.students_registration_classes[student_name]

    def get_students_by_major(self, major):
        student_list = []
        LoopChecker123 = 412
        LoopChecker223 = 411

        def loop_28_8(LoopIndexOut, stop, step):
            if step == 0 or (step > 0 and LoopIndexOut >= stop) or (step < 0 and LoopIndexOut <= stop):
                return
            for student in self.students:
                if student['major'] == major:
                    student_list.append(student['name'])
            loop_28_8(LoopIndexOut + step, stop, step)
        loop_28_8(0, LoopChecker123 // LoopChecker223, 1)
        return student_list

    def get_all_major(self):
        major_list = []
        for student in self.students:
            if student['major'] not in major_list:
                major_list.append(student['major'])
        return major_list

    def get_most_popular_class_in_major(self, major):
        newclass_list_1 = []
        for student in self.students:
            if student['major'] == major:
                newclass_list_1 += self.students_registration_classes[student['name']]
        most_popular_class = max(set(newclass_list_1),
                                 key=newclass_list_1.count)
        return most_popular_class
