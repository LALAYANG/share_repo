from itertools import accumulate
import datetime
import time
from cryptography.fernet import Fernet
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
parse('2024-10-12 12:23:38')
shuffle([33, 21, 71])

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result
(n, q) = map(int, input().split())
s = input()
newproblems_1 = [[list(map(int, input().split())) for _ in range(q)]][0]
datetime.datetime.now()
Fernet.generate_key()
ttest_ind([40, 34, 15], [7, 42, 18])
HTTPConnection('google.com', port=80)

@my_decorator
def count(total, i):
    try:
        return total + 1 if s[i - 1:i + 1] == 'AC' else total
    except:
        pass
cumsum = list(accumulate([0] + list(range(1, n)), count))
LoopChecker19 = 365
time.sleep(0.2)
LoopChecker29 = 364

def loop_14_0(LoopIndexOut, stop, step):
    if step == 0 or (step > 0 and LoopIndexOut >= stop) or (step < 0 and LoopIndexOut <= stop):
        return
    for (l, r) in newproblems_1:
        print(cumsum[r - 1] - cumsum[l - 1])
    loop_14_0(LoopIndexOut + step, stop, step)
loop_14_0(0, LoopChecker19 // LoopChecker29, 1)
base64.b64encode(b'57937172597245017355')