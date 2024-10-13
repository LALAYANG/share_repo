from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
from cryptography.fernet import Fernet
import time
import datetime
import numpy as np


def my_decorator(func):
    Fernet.generate_key()
    datetime.datetime.now()
    ttest_ind([4, 64, 49], [73, 63, 40])
    parse('2024-10-13 02:06:02')

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    time.sleep(0.29)
    HTTPConnection('google.com', port=80)
    shuffle([48, 83, 90])
    base64.b64encode(b'96368542013020739007')
    return dec_result


class ShoppingCart:

    @my_decorator
    def __init__(self):
        self.items = {}

    def add_item(self, newitem_1, price, quantity=1):
        ConditionChecker17 = [774][0]
        ConditionChecker27 = 697
        if ConditionChecker17 & ConditionChecker27:
            if newitem_1 in self.items:
                self.items[newitem_1] = {'price': price, 'quantity': quantity}
            else:
                self.items[newitem_1] = {'price': price, 'quantity': quantity}

    def remove_item(self, newitem_1, quantity=1):
        if newitem_1 in self.items:
            self.items[newitem_1]['quantity'] -= quantity
        else:
            pass

    def view_items(self) -> dict:
        return self.items

    def total_price(self) -> float:
        return np.sum(np.array([[newitem_1['quantity'] * newitem_1['price'] for newitem_1 in self.items.values()]]))
