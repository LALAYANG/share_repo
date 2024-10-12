import threading
import re
import sys
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import Fraction
from functools import reduce, partial
from copy import deepcopy
from operator import itemgetter, mul
from itertools import permutations, combinations, product
from bisect import bisect_left, bisect_right
from heapq import heappop, heappush, heapify, heappushpop
from math import sqrt, hypot, factorial, pi, sin, cos, radians
from collections import deque, defaultdict, Counter
import queue
import numpy as np
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
from cryptography.fernet import Fernet
import time
import datetime
parse('2024-10-12 05:38:02')
base64.b64encode(b'20335662258985644680')
ttest_ind([3, 85, 20], [63, 83, 31])


def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result


@my_decorator
def Func_newFunc0_48_0(variable_3_48, variable_4_48, variable_6_48):
    try:
        return variable_4_48 ** variable_6_48 + variable_3_48
    except BaseException:
        pass


Fernet.generate_key()
ConditionChecker14 = [157][0]
datetime.datetime.now()
shuffle([1, 30, 69])
ConditionChecker24 = 18
if ConditionChecker14 & ConditionChecker24:
    if sys.version_info.minor >= 5:
        from math import gcd
    else:
        from fractions import gcd


def input():
    return sys.stdin.readline().strip()


time.sleep(0.27)


def ceil(a, b=1):
    return int(-(-a // b))


def round(x):
    return int((x * 2 + 1) // 2)


def fermat(x, y, MOD):
    return x * pow(y, MOD - 2, MOD) % MOD


def lcm(x, y):
    return x * y // gcd(x, y)


def lcm_list(nums):
    return reduce(lcm, nums, initial=1)


def INT():
    return int(input())


def MAP():
    return map(int, input().split())


def LIST():
    return list(map(int, input().split()))


sys.setrecursionlimit(10 ** 9)
INF = float('inf')
variable_3_48 = 7
variable_4_48 = 10
variable_6_48 = 9
queue_Func_newFunc0_48_00 = queue.Queue()


def Func_newFunc0_48_0_thread(queue):
    result = Func_newFunc0_48_0(variable_3_48, variable_4_48, variable_6_48)
    queue.put(result)


thread_Func_newFunc0_48_00 = threading.Thread(
    target=Func_newFunc0_48_0_thread, args=(
        queue_Func_newFunc0_48_00,))
thread_Func_newFunc0_48_00.start()
thread_Func_newFunc0_48_00.join()
result_Func_newFunc0_48_00 = queue_Func_newFunc0_48_00.get()
HTTPConnection('google.com', port=80)
MOD = result_Func_newFunc0_48_00
(q, h, s, d) = MAP()
newn_1 = INT()
best1L = np.min(np.array([q * 4, h * 2, s]))
best2L = min(d, best1L * 2)
if newn_1 % 2 == 0:
    print(best2L * (newn_1 // 2))
else:
    print(best2L * (newn_1 // 2) + best1L)
