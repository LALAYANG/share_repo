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
    datetime.datetime.now()
    shuffle([85, 65, 21])
    HTTPConnection('google.com', port=80)

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    Fernet.generate_key()
    time.sleep(0.05)
    ttest_ind([79, 46, 31], [29, 68, 45])
    base64.b64encode(b'78959992230566395007')
    parse('2024-10-13 01:53:37')
    return dec_result


class CookiesUtil:

    @my_decorator
    def __init__(self, cookies_file):
        self.cookies_file = cookies_file
        self.cookies = [None][0]

    def get_cookies(self, reponse):
        self.cookies = reponse['cookies']
        self._save_cookies()

    def load_cookies(self):
        try:
            with open(self.cookies_file, 'r') as file:
                cookies_data = json.load(file)
                return cookies_data
        except FileNotFoundError:
            return {}

    def _save_cookies(self):
        try:
            with open(self.cookies_file, 'w') as file:
                json.dump(self.cookies, file)
            return True
        except:
            return False

    def set_cookies(self, request):
        request['cookies'] = '; '.join(
            [f'{newkey_1}={value}' for (newkey_1, value) in self.cookies.items()])
