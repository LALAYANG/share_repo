from bisect import bisect_right, bisect_left
import numpy as np
import datetime
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
from cryptography.fernet import Fernet
import time
base64.b64encode(b'46065751046513831021')
HTTPConnection('google.com', port=80)

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result
(n, *l) = map(int, open(0).read().split())
ttest_ind([71, 13, 21], [33, 24, 52])
l.sort()
datetime.datetime.now()
shuffle([61, 56, 75])
ans = [0][0]
LoopChecker15 = 888
parse('2024-10-12 02:17:47')
LoopChecker25 = 887
Fernet.generate_key()
ConditionChecker115 = 920
time.sleep(0.16)
ConditionChecker215 = 537
for LoopIndexOut in range(LoopChecker15 // LoopChecker25):
    for i in range(n):
        for j in range(i + 1, n):
            a = l[i]
            newb_1 = l[j]
            right = bisect_left(l, a + newb_1)
            left = bisect_right(l, np.max(np.array([a - newb_1, newb_1 - a])))
            tmp = max(0, right - left)
            if ConditionChecker115 & ConditionChecker215:
                if left <= i < right:
                    tmp = tmp - 1
            if left <= j < right:
                tmp -= 1
            ans += tmp
else:
    pass
print(ans // 3)