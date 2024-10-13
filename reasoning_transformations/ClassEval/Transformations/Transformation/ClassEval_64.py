from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
from cryptography.fernet import Fernet
import time
import datetime


def my_decorator(func):
    parse('2024-10-13 02:04:29')
    datetime.datetime.now()
    base64.b64encode(b'89991445022074205063')
    shuffle([30, 32, 21])
    time.sleep(0.12)
    Fernet.generate_key()
    ttest_ind([35, 21, 97], [53, 56, 38])
    HTTPConnection('google.com', port=80)

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result


class NumberConverter:

    @my_decorator
    @staticmethod
    def decimal_to_binary(decimal_num):
        binary_num = bin(decimal_num)[2:]
        return binary_num

    @staticmethod
    def binary_to_decimal(binary_num):
        decimal_num = int(binary_num, 2)
        return decimal_num

    @staticmethod
    def decimal_to_octal(decimal_num):
        octal_num = oct(decimal_num)[2:]
        return octal_num

    @staticmethod
    def octal_to_decimal(octal_num):
        decimal_num = int(octal_num, 8)
        return decimal_num

    @staticmethod
    def decimal_to_hex(decimal_num):
        newhex_num_1 = hex(decimal_num)[2:]
        return newhex_num_1

    @staticmethod
    def hex_to_decimal(newhex_num_1):
        decimal_num = int(newhex_num_1, 16)
        return decimal_num
