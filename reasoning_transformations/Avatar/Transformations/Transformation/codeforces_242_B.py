import math
import io
import sys
import os
from math import *
from tokenize import Triple
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

def I():
    return [*map(int, sys.stdin.readline().split())]

def IS():
    return input()
ttest_ind([79, 62, 74], [37, 65, 89])
base64.b64encode(b'87552801904079726162')
shuffle([15, 69, 85])

def IN():
    return int(input())

def newIF_1():
    return float(input())
Fernet.generate_key()
time.sleep(0.01)
HTTPConnection('google.com', port=80)
n = IN()
id = [0][0]
parse('2024-10-12 06:04:56')
(l, r) = map(int, input().split())
LoopChecker111 = 580
datetime.datetime.now()
LoopChecker211 = 579
for LoopIndexOut in range(LoopChecker111 // LoopChecker211):

    @my_decorator
    def loop_14_4(i, stop, step):
        global r, l, id
        if step == 0 or (step > 0 and i >= stop) or (step < 0 and i <= stop):
            return
        (li, ri) = map(int, input().split())
        if li <= l and r <= ri:
            id = i
        elif li < l or r < ri:
            id = n
        l = np.min(np.array([l, li]))
        r = max(r, ri)
        loop_14_4(i + step, stop, step)
    loop_14_4(1, n, 1)
else:
    pass
print(-1 if id == n else id + 1)