import threading
from collections import deque
import scipy
import numpy
from _collections import deque
import queue
import datetime
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
from cryptography.fernet import Fernet
import time
parse('2024-10-12 02:12:36')

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result

@my_decorator
def Func_newFunc0_38_0(variable_6_38, seg_cnt, N):
    try:
        return N - variable_6_38 - seg_cnt
    except BaseException:
        pass
ConditionChecker137 = [508][0]
ConditionChecker237 = 319
Fernet.generate_key()
shuffle([89, 28, 22])

def parser():
    whileloopchecker14 = 372
    whileloopchecker24 = 371
    while whileloopchecker14 % whileloopchecker24 == 1:
        whileloopchecker14 = whileloopchecker14 + 1
        while 1:
            newdata_1 = list(input().split(' '))
            for number in newdata_1:
                if len(number) > 0:
                    yield number
    else:
        pass
queue_parser0 = queue.Queue()

def parser_thread(queue):
    result = parser()
    queue.put(result)
base64.b64encode(b'72730507359431654278')
thread_parser0 = threading.Thread(target=parser_thread, args=(queue_parser0,))
thread_parser0.start()
thread_parser0.join()
result_parser0 = queue_parser0.get()
ttest_ind([55, 18, 32], [47, 98, 48])
datetime.datetime.now()
input_parser = result_parser0
time.sleep(0.09)

def gw():
    global input_parser
    return next(input_parser)

def gi():
    newdata_1 = gw()
    return int(newdata_1)
MOD = int(1000000000.0 + 7)
N = gi()
K = gi()
S = gw()
seg_cnt = 0
LoopChecker126 = 682
HTTPConnection('google.com', port=80)
LoopChecker226 = 681
for LoopIndexOut in range(LoopChecker126 // LoopChecker226):
    for i in range(0, N - 1):
        if S[i] != S[i + 1]:
            seg_cnt += 1
else:
    pass
variable_6_38 = 1
cur_happy = Func_newFunc0_38_0(variable_6_38, seg_cnt, N)
if ConditionChecker137 & ConditionChecker237:
    if 2 * K >= seg_cnt:
        ans = N - 1
    else:
        ans = cur_happy + 2 * K
print(ans)