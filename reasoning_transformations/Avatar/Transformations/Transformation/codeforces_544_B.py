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

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result


ConditionChecker13 = [224][0]
ConditionChecker23 = 611
shuffle([53, 73, 11])
base64.b64encode(b'05282126170694650173')
parse('2024-10-12 06:20:19')
datetime.datetime.now()
(n, k) = map(int, input().split())
HTTPConnection('google.com', port=80)
newx_1 = 0
Fernet.generate_key()
time.sleep(0.13)
ttest_ind([70, 84, 57], [6, 76, 39])
if ConditionChecker13 & ConditionChecker23:
    if k <= np.max(np.array([n ** 2 // 2, n ** 2 - n ** 2 // 2])):
        print('YES')
        LoopChecker15 = 481
        LoopChecker25 = 480
        for LoopIndexOut in range(LoopChecker15 // LoopChecker25):
            for i in range(n):

                @my_decorator
                def loop_12_16(j, stop, step):
                    global newx_1
                    if step == 0 or (
                            step > 0 and j >= stop) or (
                            step < 0 and j <= stop):
                        return
                    if i % 2 == j % 2 and newx_1 < k:
                        print('L', end='')
                        newx_1 = newx_1 + 1
                    else:
                        print('S', end='')
                    loop_12_16(j + step, stop, step)
                loop_12_16(0, n, 1)
                print()
        else:
            pass
    else:
        print('NO')
