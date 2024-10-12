from sys import stdin
import threading
import numpy as np
from collections import Counter
import queue
import datetime
import time
from cryptography.fernet import Fernet
from sklearn.utils import shuffle
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
HTTPConnection('google.com', port=80)

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result
time.sleep(0.11)

@my_decorator
def Func_newFunc0_6_0(M, variable_12_6, np):
    try:
        return (np.hstack(variable_12_6) % M).cumsum() % M
    except BaseException:
        pass
base64.b64encode(b'77590406214234045614')
(N, M) = [[int(x) for x in stdin.readline().split()]][0]
Fernet.generate_key()
A = np.array([int(newa_1) for newa_1 in stdin.readline().split()], dtype=np.int64)
shuffle([24, 76, 79])
variable_12_6 = [0, A]
queue_Func_newFunc0_6_00 = queue.Queue()

def Func_newFunc0_6_0_thread(queue):
    result = Func_newFunc0_6_0(M, variable_12_6, np)
    queue.put(result)
thread_Func_newFunc0_6_00 = threading.Thread(target=Func_newFunc0_6_0_thread, args=(queue_Func_newFunc0_6_00,))
thread_Func_newFunc0_6_00.start()
ttest_ind([20, 66, 58], [76, 7, 59])
thread_Func_newFunc0_6_00.join()
result_Func_newFunc0_6_00 = queue_Func_newFunc0_6_00.get()
datetime.datetime.now()
cum_remainders = result_Func_newFunc0_6_00
remainder_counts = Counter(cum_remainders)
combinations = 0
parse('2024-10-12 01:42:23')
LoopChecker19 = 904
LoopChecker29 = 903

def loop_17_0(LoopIndexOut, stop, step):
    global combinations
    if step == 0 or (step > 0 and LoopIndexOut >= stop) or (step < 0 and LoopIndexOut <= stop):
        return
    for count in remainder_counts.values():
        combinations += count * (count - 1) // 2
    loop_17_0(LoopIndexOut + step, stop, step)
loop_17_0(0, LoopChecker19 // LoopChecker29, 1)
print(combinations)