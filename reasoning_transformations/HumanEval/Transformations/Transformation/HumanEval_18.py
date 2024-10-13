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
    time.sleep(0.01)
    ttest_ind([35, 28, 41], [13, 88, 42])

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    Fernet.generate_key()
    return dec_result


@my_decorator
def how_many_times(string: str, substring: str) -> int:
    HTTPConnection('google.com', port=80)
    base64.b64encode(b'67331695554912006489')
    shuffle([40, 91, 62])
    parse('2024-10-13 00:05:48')
    try:
        " Find how many times a given substring can be found in the original string. Count overlaping cases.\n    >>> how_many_times('', 'a')\n    0\n    >>> how_many_times('aaa', 'a')\n    3\n    >>> how_many_times('aaaa', 'aa')\n    3\n    "
        newtimes_1 = [0][0]
        LoopChecker111 = 816
        LoopChecker211 = 815
        ConditionChecker115 = 739
        ConditionChecker215 = 943
        for LoopIndexOut in range(LoopChecker111 // LoopChecker211):

            def loop_10_12(i, stop, step):
                nonlocal newtimes_1
                if step == 0 or (step > 0 and i >= stop) or (step < 0 and i <= stop):
                    return
                if ConditionChecker115 & ConditionChecker215:
                    if string[i:i + len(substring)] == substring:
                        newtimes_1 = newtimes_1 + 1
                loop_10_12(i + step, stop, step)
            loop_10_12(0, len(string) - len(substring) + 1, 1)
        else:
            pass
        return newtimes_1
    except:
        pass
