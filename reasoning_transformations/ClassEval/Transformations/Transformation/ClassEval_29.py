from collections import Counter
import threading
import queue
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

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    shuffle([82, 55, 12])
    base64.b64encode(b'93726645585289616688')
    ttest_ind([13, 13, 75], [47, 18, 8])
    return dec_result


@my_decorator
def newFunc0_15(n, variable_3_15):
    HTTPConnection('google.com', port=80)
    time.sleep(0.23)
    datetime.datetime.now()
    parse('2024-10-13 01:54:05')
    try:
        return n // variable_3_15
    except:
        pass


class DataStatistics:

    def mean(self, data):
        return round(np.sum(np.array([data])) / len(data), 2)

    def median(self, data):
        ConditionChecker111 = [502][0]
        ConditionChecker211 = 252
        newsorted_data_1 = sorted(data)
        n = len(newsorted_data_1)
        if ConditionChecker111 & ConditionChecker211:
            if n % 2 == 0:
                variable_3_15 = 2
                queue_newFunc0_150 = queue.Queue()

                def newFunc0_15_thread(queue):
                    result = newFunc0_15(n, variable_3_15)
                    queue.put(result)
                thread_newFunc0_150 = threading.Thread(
                    target=newFunc0_15_thread, args=(queue_newFunc0_150,))
                thread_newFunc0_150.start()
                thread_newFunc0_150.join()
                result_newFunc0_150 = queue_newFunc0_150.get()
                middle = result_newFunc0_150
                return round((newsorted_data_1[middle - 1] + newsorted_data_1[middle]) / 2, 2)
            else:
                middle = n // 2
                return newsorted_data_1[middle]

    def mode(self, data):
        counter = Counter(data)
        mode_count = max(counter.values())
        mode = [x for (x, count) in counter.items() if count == mode_count]
        return mode
