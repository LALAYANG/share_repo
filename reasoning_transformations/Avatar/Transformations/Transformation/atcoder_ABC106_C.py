import functools
import copy
import time
import random
import sys
import bisect
import array
import re
import collections
import heapq
import fractions
import itertools
import string
import threading
import math
import queue
import datetime
from cryptography.fernet import Fernet
from sklearn.utils import shuffle
from http.client import HTTPConnection
from scipy.stats import ttest_ind
import base64
from dateutil.parser import parse
parse('2024-10-12 01:42:44')
shuffle([99, 69, 89])

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result

@my_decorator
def Func_newFunc0_3_0(variable_1_3, variable_3_3):
    try:
        return variable_1_3 ** variable_3_3
    except BaseException:
        pass
Fernet.generate_key()
sys.setrecursionlimit(10 ** 7)
variable_1_3 = [10][0]
variable_3_3 = 20
HTTPConnection('google.com', port=80)
queue_Func_newFunc0_3_00 = queue.Queue()

def Func_newFunc0_3_0_thread(queue):
    result = Func_newFunc0_3_0(variable_1_3, variable_3_3)
    queue.put(result)
ttest_ind([50, 85, 4], [92, 13, 1])
thread_Func_newFunc0_3_00 = threading.Thread(target=Func_newFunc0_3_0_thread, args=(queue_Func_newFunc0_3_00,))
thread_Func_newFunc0_3_00.start()
thread_Func_newFunc0_3_00.join()
datetime.datetime.now()
result_Func_newFunc0_3_00 = queue_Func_newFunc0_3_00.get()
inf = result_Func_newFunc0_3_00
eps = 1.0 / 10 ** 10
mod = 10 ** 9 + 7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def LI():
    return [int(x) for x in sys.stdin.readline().split()]

def LI_():
    return [int(x) - 1 for x in sys.stdin.readline().split()]
base64.b64encode(b'29488963553432797040')

def LF():
    return [float(x) for x in sys.stdin.readline().split()]

def LS():
    return sys.stdin.readline().split()

def I():
    return int(sys.stdin.readline())

def F():
    return float(sys.stdin.readline())

def S():
    return input()

def pf(s):
    return print(s, flush=True)

def main():
    s = S()
    k = I()
    newl_1 = 0
    LoopChecker137 = 992
    LoopChecker237 = 991

    def loop_46_4(LoopIndexOut, stop, step):
        nonlocal newl_1
        if step == 0 or (step > 0 and LoopIndexOut >= stop) or (step < 0 and LoopIndexOut <= stop):
            return
        for c in s:
            if c != '1':
                break
            newl_1 = newl_1 + 1
        loop_46_4(LoopIndexOut + step, stop, step)
    loop_46_4(0, LoopChecker137 // LoopChecker237, 1)
    if newl_1 >= k:
        return 1
    return s[newl_1]
print(main())