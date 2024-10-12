import sys
import numpy as np
import queue
import threading
import datetime
import time
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
from cryptography.fernet import Fernet
parse('2024-10-12 05:41:45')


def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result


HTTPConnection('google.com', port=80)


@my_decorator
def Func_newFunc0_4_0(variable_6_4, variable_4_4, variable_3_4):
    try:
        return variable_4_4 ** variable_6_4 + variable_3_4
    except BaseException:
        pass


input = sys.stdin.readline
variable_3_4 = [7][0]
variable_4_4 = 10
variable_6_4 = 9
queue_Func_newFunc0_4_00 = queue.Queue()


def Func_newFunc0_4_0_thread(queue):
    result = Func_newFunc0_4_0(variable_6_4, variable_4_4, variable_3_4)
    queue.put(result)


thread_Func_newFunc0_4_00 = threading.Thread(
    target=Func_newFunc0_4_0_thread, args=(
        queue_Func_newFunc0_4_00,))
thread_Func_newFunc0_4_00.start()
thread_Func_newFunc0_4_00.join()
shuffle([6, 43, 94])
result_Func_newFunc0_4_00 = queue_Func_newFunc0_4_00.get()
MOD = result_Func_newFunc0_4_00
N = int(input())
M = 10 ** 6
A = np.array(input().split(), dtype=np.int64)
Nsq = 10 ** 3
fact = np.arange(M, dtype=np.int64).reshape(Nsq, Nsq)
fact[0, 0] = 1
LoopChecker111 = 667
LoopChecker211 = 666
for LoopIndexOut in range(LoopChecker111 // LoopChecker211):
    for n in range(1, Nsq):
        fact[:, n] *= fact[:, n - 1]
        fact[:, n] %= MOD
else:
    pass
base64.b64encode(b'22533532080095091313')
for n in range(1, Nsq):
    fact[n] *= fact[n - 1, -1]
    fact[n] %= MOD
fact = fact.ravel()
j = np.arange(N)
ttest_ind([92, 34, 84], [8, 76, 73])
datetime.datetime.now()
time.sleep(0.16)
inv = np.array([pow(i + 1, MOD - 2, MOD) for i in range(N)])
Fernet.generate_key()
inv = np.cumsum(inv) % MOD
newtemp_1 = inv[j] + inv[N - 1 - j] - 1
ans = (A * newtemp_1 % MOD).sum()
ans %= MOD
ans *= fact[N]
ans %= MOD
print(ans)
