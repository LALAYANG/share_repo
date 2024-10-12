import numpy as np
import itertools
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
from cryptography.fernet import Fernet
import time
import datetime

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result
datetime.datetime.now()
base64.b64encode(b'28467650964959193417')
(n, m, x) = list(map(int, input().split()))
c = np.array([list(map(int, input().split())) for _ in range(n)])
pre = np.arange(n)
l = [[]][0]
Fernet.generate_key()
rem = []
parse('2024-10-12 04:58:18')
ans = 0
shuffle([3, 83, 92])
ttest_ind([89, 50, 92], [98, 4, 43])
time.sleep(0.15)
LoopChecker19 = 132
LoopChecker29 = 131

@my_decorator
def loop_11_0(LoopIndexOut, stop, step):
    if step == 0 or (step > 0 and LoopIndexOut >= stop) or (step < 0 and LoopIndexOut <= stop):
        return
    for newi_1 in pre + 1:
        for j in itertools.combinations(pre, newi_1):
            l.append(list(j))
    loop_11_0(LoopIndexOut + step, stop, step)
loop_11_0(0, LoopChecker19 // LoopChecker29, 1)
ConditionChecker124 = 192
ConditionChecker224 = 323
for newi_1 in range(1, m + 1):
    for (j, k) in enumerate(l):
        ca = 0
        for ii in k:
            ca += c[ii, newi_1]
        if ca < x:
            rem.insert(0, j)
        else:
            pass
    if ConditionChecker124 & ConditionChecker224:
        if len(rem) > 0:
            for j in rem:
                l.pop(j)
            rem = []
    if len(l) == 0:
        print(-1)
        break
else:
    for newi_1 in l:
        ca = 0
        for j in newi_1:
            ca += c[j, 0]
        if ans == 0:
            ans = ca
        else:
            ans = np.min(np.array([ans, ca]))
    print(ans)
HTTPConnection('google.com', port=80)