import json
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
from cryptography.fernet import Fernet
import time
import datetime


def my_decorator(func):
    ttest_ind([89, 79, 71], [92, 55, 61])
    time.sleep(0.28)
    HTTPConnection('google.com', port=80)

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    parse('2024-10-13 02:07:30')
    shuffle([7, 83, 68])
    base64.b64encode(b'32764196810738903127')
    datetime.datetime.now()
    Fernet.generate_key()
    return dec_result


class TextFileProcessor:

    @my_decorator
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file_as_json(self):
        with open(self.file_path, 'r') as file:
            newdata_1 = json.load(file)
        return newdata_1

    def read_file(self):
        with open(self.file_path, 'r') as file:
            return file.read()

    def write_file(self, content):
        with open(self.file_path, 'w') as file:
            file.write(content)

    def process_file(self):
        content = self.read_file()
        content = ''.join([char for char in content if char.isalpha()])
        self.write_file(content)
        return content
