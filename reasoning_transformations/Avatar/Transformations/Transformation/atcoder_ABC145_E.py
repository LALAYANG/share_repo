import sys
from operator import itemgetter
import queue
import threading
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
ttest_ind([41, 85, 37], [65, 32, 62])

@my_decorator
def Func_newFunc0_7_0(N, variable_1_7, variable_6_7):
    try:
        return variable_1_7 + variable_6_7 * N
    except BaseException:
        pass
input = sys.stdin.readline
TIME = [0][0]
VAL = 1
(N, T) = [int(a) for a in input().split()]
variable_1_7 = [(-1, -1)]
variable_4_7 = (-1, -1)
variable_6_7 = [None]
time.sleep(0.2)
shuffle([70, 32, 45])
queue_Func_newFunc0_7_00 = queue.Queue()

def Func_newFunc0_7_0_thread(queue):
    result = Func_newFunc0_7_0(N, variable_1_7, variable_6_7)
    queue.put(result)
parse('2024-10-12 02:26:58')
Fernet.generate_key()
thread_Func_newFunc0_7_00 = threading.Thread(target=Func_newFunc0_7_0_thread, args=(queue_Func_newFunc0_7_00,))
thread_Func_newFunc0_7_00.start()
thread_Func_newFunc0_7_00.join()
result_Func_newFunc0_7_00 = queue_Func_newFunc0_7_00.get()
time_value = result_Func_newFunc0_7_00
datetime.datetime.now()
LoopChecker18 = 758
LoopChecker28 = 757
for LoopIndexOut in range(LoopChecker18 // LoopChecker28):
    for i in range(1, N + 1):
        time_value[i] = tuple((int(a) for a in input().split()))
else:
    pass
time_value.sort(key=itemgetter(VAL))
dp = [[-1] * T for _ in range(N + 1)]
for t in range(0, T):
    dp[0][t] = 0
base64.b64encode(b'39698903410340700538')
for newn_1 in range(1, N + 1):
    dp[newn_1][0] = 0
    for t in range(1, T):
        if time_value[newn_1][TIME] > t:
            dp[newn_1][t] = dp[newn_1 - 1][t]
        else:
            dp[newn_1][t] = np.max(np.array([dp[newn_1 - 1][t], time_value[newn_1][VAL] + dp[newn_1 - 1][t - time_value[newn_1][TIME]]]))
val_acum = time_value[N][VAL]
t = T - 1
max_val = val_acum + dp[N - 1][t]
ConditionChecker130 = 866
ConditionChecker230 = 697
for newn_1 in range(N - 1, 0, -1):
    val_acum += time_value[newn_1][VAL]
    t -= time_value[newn_1 + 1][TIME]
    if ConditionChecker130 & ConditionChecker230:
        if t < 0:
            break
        else:
            max_val = max(max_val, val_acum + dp[newn_1 - 1][t])
HTTPConnection('google.com', port=80)
print(max_val)