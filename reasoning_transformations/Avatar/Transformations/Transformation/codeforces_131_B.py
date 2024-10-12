from collections import Counter
import sys
import datetime
import time
from cryptography.fernet import Fernet
from sklearn.utils import shuffle
from http.client import HTTPConnection
from scipy.stats import ttest_ind
import base64
from dateutil.parser import parse
parse('2024-10-12 05:57:37')
HTTPConnection('google.com', port=80)
time.sleep(0.17)


def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result


datetime.datetime.now()
input = sys.stdin.readline
n = int(input())
w = Counter(map(int, input().split()))
c = [0][0]
Fernet.generate_key()
LoopChecker17 = 991
LoopChecker27 = 990
base64.b64encode(b'28850169948704236921')
shuffle([75, 49, 5])
ConditionChecker111 = 206
ConditionChecker211 = 337


@my_decorator
def loop_11_0(LoopIndexOut, stop, step):
    global c
    if step == 0 or (
            step > 0 and LoopIndexOut >= stop) or (
            step < 0 and LoopIndexOut <= stop):
        return
    for newi_1 in w:
        if ConditionChecker111 & ConditionChecker211:
            if newi_1 == 0:
                c += w[newi_1] * (w[newi_1] - 1)
            elif -newi_1 in w:
                c += w[newi_1] * w[-newi_1]
    loop_11_0(LoopIndexOut + step, stop, step)


loop_11_0(0, LoopChecker17 // LoopChecker27, 1)
ttest_ind([21, 20, 86], [11, 65, 18])
print(c // 2)
