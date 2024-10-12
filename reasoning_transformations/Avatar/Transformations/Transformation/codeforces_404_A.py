from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
from cryptography.fernet import Fernet
import time
import datetime
base64.b64encode(b'16904056733936635431')

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result
n = int(input())
Fernet.generate_key()
shuffle([54, 61, 23])
ttest_ind([29, 17, 85], [64, 52, 67])
s = [[]][0]
parse('2024-10-12 06:13:27')
HTTPConnection('google.com', port=80)
LoopChecker13 = 649
LoopChecker23 = 648
for LoopIndexOut in range(LoopChecker13 // LoopChecker23):

    @my_decorator
    def loop_6_4(i, stop, step):
        global k
        if step == 0 or (step > 0 and i >= stop) or (step < 0 and i <= stop):
            return
        k = input()
        s.append(k)
        loop_6_4(i + step, stop, step)
    loop_6_4(0, n, 1)
else:
    pass
flag = 0
newd1_1 = []
d2 = []
rem = set()
ConditionChecker115 = 447
ConditionChecker215 = 585
time.sleep(0.22)
for i in range(n):
    for j in range(n):
        if ConditionChecker115 & ConditionChecker215:
            if i == j:
                newd1_1.append(s[i][j])
        if i == n - j - 1:
            d2.append(s[i][j])
        if i != j and i != n - j - 1:
            rem.add(s[i][j])
if len(rem) != 1:
    print('NO')
elif newd1_1 != d2:
    print('NO')
elif len(set(newd1_1)) != 1:
    print('NO')
elif set(newd1_1) == rem:
    print('NO')
else:
    print('YES')
datetime.datetime.now()