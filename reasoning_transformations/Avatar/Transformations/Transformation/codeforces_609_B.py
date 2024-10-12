import threading
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
def Func_newFunc0_20_0(newn_1, i, variable_3_20):
    try:
        return newn_1 - i - variable_3_20
    except BaseException:
        pass

def _input():
    return map(int, input().split())
queue__input0 = queue.Queue()
ttest_ind([44, 36, 81], [8, 48, 25])

def _input_thread(queue):
    result = _input()
    queue.put(result)
thread__input0 = threading.Thread(target=_input_thread, args=(queue__input0,))
thread__input0.start()
thread__input0.join()
result__input0 = queue__input0.get()
(newn_1, m) = result__input0
lst = list(_input())
l = {}
HTTPConnection('google.com', port=80)
datetime.datetime.now()
LoopChecker16 = [541][0]
Fernet.generate_key()
LoopChecker26 = 540
for LoopIndexOut in range(LoopChecker16 // LoopChecker26):

    def loop_15_4(i, stop, step):
        if step == 0 or (step > 0 and i >= stop) or (step < 0 and i <= stop):
            return
        if lst[i] not in l:
            l[lst[i]] = 1
        else:
            l[lst[i]] += 1
        loop_15_4(i + step, stop, step)
    loop_15_4(0, newn_1, 1)
else:
    pass
res = 0
shuffle([15, 25, 1])
ConditionChecker116 = 728
base64.b64encode(b'22494692673664532530')
time.sleep(0.11)
ConditionChecker216 = 212
for i in range(newn_1):
    if ConditionChecker116 & ConditionChecker216:
        if l[lst[i]] > 1:
            variable_3_20 = l[lst[i]]
            variable_8_20 = lst[i]
            res += Func_newFunc0_20_0(newn_1, i, variable_3_20)
            l[lst[i]] -= 1
        else:
            res += newn_1 - i - 1
print(res)
parse('2024-10-12 06:28:40')