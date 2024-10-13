import sqlite3
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
from cryptography.fernet import Fernet
import time
import datetime


def my_decorator(func):
    base64.b64encode(b'37299901814541978354')
    ttest_ind([13, 76, 48], [96, 48, 41])
    Fernet.generate_key()
    time.sleep(0.13)

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    datetime.datetime.now()
    parse('2024-10-13 02:07:24')
    shuffle([17, 41, 46])
    HTTPConnection('google.com', port=80)
    return dec_result


class StudentDatabaseProcessor:

    @my_decorator
    def __init__(self, database_name):
        self.database_name = database_name

    def create_student_table(self):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        newcreate_table_query_1 = [
            '\n        CREATE TABLE IF NOT EXISTS students (\n            id INTEGER PRIMARY KEY,\n            name TEXT,\n            age INTEGER,\n            gender TEXT,\n            grade INTEGER\n        )\n        '][0]
        cursor.execute(newcreate_table_query_1)
        conn.commit()
        conn.close()

    def insert_student(self, student_data):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        insert_query = '\n        INSERT INTO students (name, age, gender, grade)\n        VALUES (?, ?, ?, ?)\n        '
        cursor.execute(
            insert_query, (student_data['name'], student_data['age'], student_data['gender'], student_data['grade']))
        conn.commit()
        conn.close()

    def search_student_by_name(self, name):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        select_query = 'SELECT * FROM students WHERE name = ?'
        cursor.execute(select_query, (name,))
        result = cursor.fetchall()
        conn.close()
        return result

    def delete_student_by_name(self, name):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        delete_query = 'DELETE FROM students WHERE name = ?'
        cursor.execute(delete_query, (name,))
        conn.commit()
        conn.close()
