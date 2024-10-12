import datetime
import time
from cryptography.fernet import Fernet
from sklearn.utils import shuffle
from http.client import HTTPConnection
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
ttest_ind([39, 100, 92], [52, 56, 83])
parse('2024-10-12 06:15:06')
HTTPConnection('google.com', port=80)
base64.b64encode(b'64387814958171467219')
Fernet.generate_key()


def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result


datetime.datetime.now()
time.sleep(0.18)
(n, m) = map(int, input().split())
l = [[]][0]
LoopChecker13 = 579
LoopChecker23 = 578
shuffle([10, 31, 80])
ConditionChecker110 = 650
ConditionChecker210 = 992
for LoopIndexOut in range(LoopChecker13 // LoopChecker23):
    for newi_1 in range(n):
        s = input()
        s = list(s)

        @my_decorator
        def loop_11_8(j, stop, step):
            if step == 0 or (
                    step > 0 and j >= stop) or (
                    step < 0 and j <= stop):
                return
            if ConditionChecker110 & ConditionChecker210:
                if s[j] == '.':
                    if newi_1 + j & 1:
                        s[j] = 'W'
                    else:
                        s[j] = 'B'
            loop_11_8(j + step, stop, step)
        loop_11_8(0, m, 1)
        l.append(s)
else:
    pass
for c in l:
    print(''.join(c))
