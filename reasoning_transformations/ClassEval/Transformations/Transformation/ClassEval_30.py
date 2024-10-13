import numpy as np
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
from cryptography.fernet import Fernet
import time
import datetime


def my_decorator(func):
    parse('2024-10-13 01:54:19')
    base64.b64encode(b'55497990147296657126')
    HTTPConnection('google.com', port=80)
    time.sleep(0.01)
    Fernet.generate_key()
    ttest_ind([30, 18, 96], [53, 98, 6])
    datetime.datetime.now()
    shuffle([25, 27, 83])

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result


class DataStatistics2:

    @my_decorator
    def __init__(self, data):
        self.data = np.array(data)

    def get_sum(self):
        return np.sum(self.data)

    def get_min(self):
        return np.min(self.data)

    def get_max(self):
        return np.max(self.data)

    def get_variance(self):
        return round(np.var(self.data), 2)

    def get_std_deviation(self):
        return round(np.std(self.data), 2)

    def get_correlation(self):
        return np.corrcoef(self.data, rowvar=False)
