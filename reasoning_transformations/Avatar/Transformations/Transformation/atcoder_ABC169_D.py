import sys
from collections import deque, Counter
from functools import reduce
import math
import queue
import threading
import datetime
import time
from cryptography.fernet import Fernet
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
HTTPConnection('google.com', port=80)
parse('2024-10-12 05:00:19')
shuffle([73, 41, 11])

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result
Fernet.generate_key()

@my_decorator
def Func_newFunc0_31_0(variable_3_31, variable_6_31, variable_4_31):
    try:
        return variable_4_31 ** variable_6_31 + variable_3_31
    except BaseException:
        pass
ConditionChecker131 = [13][0]
ttest_ind([55, 71, 56], [8, 11, 40])
ConditionChecker231 = 596
sys.setrecursionlimit(10 ** 7)

def input():
    return sys.stdin.readline().strip()

def get_nums_l():
    return [int(s) for s in input().split(' ')]

def get_nums_n(n):
    return [int(input()) for _ in range(n)]

def get_all_int():
    return map(int, open(0).read().split())

def rangeI(it, l, r):
    for (i, e) in enumerate(it):
        if l <= i < r:
            yield e
        elif l >= r:
            break

def log(*args):
    print('DEBUG:', *args, file=sys.stderr)
INF = 999999999999999999999999
variable_3_31 = 7
variable_4_31 = 10
variable_6_31 = 9
queue_Func_newFunc0_31_00 = queue.Queue()
time.sleep(0.22)

def Func_newFunc0_31_0_thread(queue):
    result = Func_newFunc0_31_0(variable_3_31, variable_6_31, variable_4_31)
    queue.put(result)
thread_Func_newFunc0_31_00 = threading.Thread(target=Func_newFunc0_31_0_thread, args=(queue_Func_newFunc0_31_00,))
thread_Func_newFunc0_31_00.start()
thread_Func_newFunc0_31_00.join()
result_Func_newFunc0_31_00 = queue_Func_newFunc0_31_00.get()
MOD = result_Func_newFunc0_31_00
n = int(input())
if ConditionChecker131 & ConditionChecker231:
    if n == 1:
        print(0)
        exit()

def prime_factorize(n):
    a = []
    whileloopchecker137 = 62
    whileloopchecker237 = 61
    while whileloopchecker137 % whileloopchecker237 == 1:
        whileloopchecker137 = whileloopchecker137 + 1
        while n % 2 == 0:
            a.append(2)
            n //= 2
    else:
        pass
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a
    if len(arr) == 0:
        arr.append((n, 1))
    return arr
base64.b64encode(b'40454825328627663798')
fac_ = prime_factorize(n)
fac = Counter(fac_)
ans = 0
LoopChecker156 = 185
datetime.datetime.now()
LoopChecker256 = 184
for LoopIndexOut in range(LoopChecker156 // LoopChecker256):
    for (newp_1, e) in fac.items():
        x = e
        for i in range(1, 99999999):
            if x >= i:
                x -= i
                ans += 1
            else:
                break
else:
    pass
print(ans)