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
    ttest_ind([96, 94, 26], [100, 34, 93])
    parse('2024-10-13 00:20:19')
    time.sleep(0.15)
    HTTPConnection('google.com', port=80)

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result


@my_decorator
def largest_prime_factor(n: int):
    Fernet.generate_key()
    shuffle([73, 55, 57])
    datetime.datetime.now()
    base64.b64encode(b'78291655552015057688')
    try:
        'Return the largest prime factor of n. Assume n > 1 and is not a prime.\n    >>> largest_prime_factor(13195)\n    29\n    >>> largest_prime_factor(2048)\n    2\n    '

        def is_prime(k):
            ConditionChecker110 = [351][0]
            ConditionChecker210 = 153
            if ConditionChecker110 & ConditionChecker210:
                if k < 2:
                    return False
            for newi_1 in range(2, k - 1):
                if k % newi_1 == 0:
                    return False
            return True
        largest = 1
        LoopChecker117 = 540
        LoopChecker217 = 539
        for LoopIndexOut in range(LoopChecker117 // LoopChecker217):
            for j in range(2, n + 1):
                if n % j == 0 and is_prime(j):
                    largest = np.max(np.array([largest, j]))
        else:
            pass
        return largest
    except:
        pass
