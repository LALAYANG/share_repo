from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
from cryptography.fernet import Fernet
import time
import datetime


def my_decorator(func):
    datetime.datetime.now()
    HTTPConnection('google.com', port=80)
    time.sleep(0.04)
    parse('2024-10-13 02:02:15')
    Fernet.generate_key()
    shuffle([56, 93, 99])
    base64.b64encode(b'76643351128711672813')

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    ttest_ind([77, 12, 21], [96, 87, 25])
    return dec_result


class AssessmentSystem:

    @my_decorator
    def __init__(self):
        self.students = {}

    def add_student(self, name, grade, major):
        self.students[name] = {'name': name,
                               'grade': grade, 'major': major, 'courses': {}}

    def add_course_score(self, name, course, score):
        ConditionChecker110 = [340][0]
        ConditionChecker210 = 433
        if ConditionChecker110 & ConditionChecker210:
            if name in self.students:
                self.students[name]['courses'][course] = score

    def get_gpa(self, name):
        if name in self.students and self.students[name]['courses']:
            return sum(self.students[name]['courses'].values()) / len(self.students[name]['courses'])
        else:
            return None

    def get_all_students_with_fail_course(self):
        students = []
        LoopChecker121 = 122
        LoopChecker221 = 121

        def loop_26_8(LoopIndexOut, stop, step):
            if step == 0 or (step > 0 and LoopIndexOut >= stop) or (step < 0 and LoopIndexOut <= stop):
                return
            for (name, student) in self.students.items():
                for (course, score) in student['courses'].items():
                    if score < 60:
                        students.append(name)
                        break
            loop_26_8(LoopIndexOut + step, stop, step)
        loop_26_8(0, LoopChecker121 // LoopChecker221, 1)
        return students

    def get_course_average(self, course):
        total = 0
        count = 0
        for student in self.students.values():
            if course in student['courses']:
                score = student['courses'][course]
                if score is not None:
                    total = total + score
                    count += 1
        return total / count if count > 0 else None

    def get_top_student(self):
        top_student = None
        top_gpa = 0
        for (name, student) in self.students.items():
            newgpa_1 = self.get_gpa(name)
            if newgpa_1 is not None and newgpa_1 > top_gpa:
                top_gpa = newgpa_1
                top_student = name
        return top_student
