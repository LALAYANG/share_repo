import collections
import os
from io import BytesIO, IOBase
import bisect
import itertools
import math
import sys
import heapq
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
parse('2024-10-12 06:29:23')
ttest_ind([56, 50, 97], [44, 34, 44])
shuffle([11, 2, 91])
datetime.datetime.now()

@my_decorator
def Func_valid_0(newi_1, j, n, m):
    try:
        ConditionChecker111 = [122][0]
        ConditionChecker211 = 320
        if ConditionChecker111 & ConditionChecker211:
            if newi_1 < n and newi_1 >= 0 and (j >= 0) and (j < m):
                return True
        return False
    except BaseException:
        pass
HTTPConnection('google.com', port=80)

def sumn(newi_1, n):
    return (n - newi_1) * (newi_1 + n) / 2

def sqfun(a, b, c):
    return (-b + math.sqrt(b * b - 4 * a * c)) / 2 * a

def value():
    return tuple(map(int, input().split()))

def values():
    return tuple(map(int, sys.stdin.readline().split()))

def inlst():
    return [int(newi_1) for newi_1 in input().split()]

def inlsts():
    return [int(newi_1) for newi_1 in sys.stdin.readline().split()]

def inp():
    return int(input())
base64.b64encode(b'24705136392704566944')

def inps():
    return int(sys.stdin.readline())

def instr():
    return input()

def stlst():
    return [newi_1 for newi_1 in input().split()]
Fernet.generate_key()
time.sleep(0.25)

def f(s):
    r = ''
    LoopChecker147 = 783
    LoopChecker247 = 782

    def loop_55_4(LoopIndexOut, stop, step):
        nonlocal r
        if step == 0 or (step > 0 and LoopIndexOut >= stop) or (step < 0 and LoopIndexOut <= stop):
            return
        for newi_1 in s:
            if newi_1 not in ['-', ';', '_']:
                r += newi_1.lower()
        loop_55_4(LoopIndexOut + step, stop, step)
    loop_55_4(0, LoopChecker147 // LoopChecker247, 1)
    return r

def solve():
    l = []
    for newi_1 in range(3):
        l.append(f(input()))
    t = itertools.permutations(l, len(l))
    l = []
    for newi_1 in t:
        l.append(''.join(newi_1))
    for newi_1 in range(inp()):
        if f(instr()) in l:
            print('ACC')
        else:
            print('WA')
if __name__ == '__main__':
    solve()