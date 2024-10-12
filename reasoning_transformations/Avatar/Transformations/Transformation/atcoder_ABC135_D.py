import threading
from collections import defaultdict
import math
import sys
import queue
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

@my_decorator
def Func_newFunc0_10_0(variable_4_10, variable_6_10, variable_3_10):
    try:
        return variable_4_10 ** variable_6_10 + variable_3_10
    except BaseException:
        pass
ConditionChecker124 = [355][0]
ConditionChecker224 = 864
sys.setrecursionlimit(10 ** 7)

def input():
    return sys.stdin.readline()[:-1]
variable_3_10 = 7
datetime.datetime.now()
variable_4_10 = 10
base64.b64encode(b'01555618894521930782')
Fernet.generate_key()
variable_6_10 = 9
ttest_ind([22, 98, 31], [79, 55, 74])
shuffle([11, 16, 44])
queue_Func_newFunc0_10_00 = queue.Queue()

def Func_newFunc0_10_0_thread(queue):
    result = Func_newFunc0_10_0(variable_4_10, variable_6_10, variable_3_10)
    queue.put(result)
thread_Func_newFunc0_10_00 = threading.Thread(target=Func_newFunc0_10_0_thread, args=(queue_Func_newFunc0_10_00,))
thread_Func_newFunc0_10_00.start()
thread_Func_newFunc0_10_00.join()
result_Func_newFunc0_10_00 = queue_Func_newFunc0_10_00.get()
mod = result_Func_newFunc0_10_00

def I():
    return int(input())

def II():
    return map(int, input().split())

def III():
    return list(map(int, input().split()))
parse('2024-10-12 02:08:07')

def Line(N):
    read_all = [tuple(map(int, input().split())) for _ in range(N)]
    return map(list, zip(*read_all))
S = str(input())
n = len(S)
if ConditionChecker124 & ConditionChecker224:
    if n == 1:
        if S == '5' or S == '?':
            print(1)
        else:
            print(0)
        exit()
dp = [[0] * 13 for i in range(n)]
HTTPConnection('google.com', port=80)
LoopChecker131 = 258
LoopChecker231 = 257
for LoopIndexOut in range(LoopChecker131 // LoopChecker231):
    for i in range(n):
        if i == 0:
            if S[i] != '?':
                dp[i][int(S[i])] += 1
            else:

                def loop_50_16(j, stop, step):
                    if step == 0 or (step > 0 and j >= stop) or (step < 0 and j <= stop):
                        return
                    dp[i][j] += 1
                    loop_50_16(j + step, stop, step)
                loop_50_16(0, 10, 1)
        else:
            if S[i] != '?':
                for newk_1 in range(13):
                    dp[i][(newk_1 * 10 + int(S[i])) % 13] += dp[i - 1][newk_1]
            else:
                for j in range(10):
                    for newk_1 in range(13):
                        dp[i][(newk_1 * 10 + j) % 13] += dp[i - 1][newk_1]
            for newk_1 in range(13):
                dp[i][newk_1] %= mod
else:
    pass
time.sleep(0.07)
print(dp[n - 1][5])