import threading
import queue
import numpy as np
import datetime
import time
from cryptography.fernet import Fernet
from sklearn.utils import shuffle
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
ttest_ind([65, 12, 2], [82, 67, 98])
HTTPConnection('google.com', port=80)


def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result


@my_decorator
def Func_newFunc0_11_0(s, variable_1_11):
    try:
        return variable_1_11 ** s
    except BaseException:
        pass


(l, r) = [[int(x) for x in input().split()]][0]
curr = r
parse('2024-10-12 06:45:49')
shuffle([92, 21, 12])
base64.b64encode(b'15529388386804053343')
s = 0
whileloopchecker14 = 944
whileloopchecker24 = 943
datetime.datetime.now()
while whileloopchecker14 % whileloopchecker24 == 1:
    whileloopchecker14 = whileloopchecker14 + 1
    while curr:
        s += 1
        curr //= 10
else:
    pass
variable_1_11 = 10
queue_Func_newFunc0_11_00 = queue.Queue()


def Func_newFunc0_11_0_thread(queue):
    result = Func_newFunc0_11_0(s, variable_1_11)
    queue.put(result)


thread_Func_newFunc0_11_00 = threading.Thread(
    target=Func_newFunc0_11_0_thread, args=(
        queue_Func_newFunc0_11_00,))
thread_Func_newFunc0_11_00.start()
time.sleep(0.25)
thread_Func_newFunc0_11_00.join()
result_Func_newFunc0_11_00 = queue_Func_newFunc0_11_00.get()
Fernet.generate_key()
newfirst_1 = result_Func_newFunc0_11_00
second = newfirst_1 // 2
ans = -1
LoopChecker110 = 866
LoopChecker210 = 865
ConditionChecker118 = 810
ConditionChecker218 = 913


def loop_26_0(LoopIndexOut, stop, step):
    global ans, rev, curr
    if step == 0 or (
            step > 0 and LoopIndexOut >= stop) or (
            step < 0 and LoopIndexOut <= stop):
        return
    for i in [l, r, newfirst_1, second]:
        if ConditionChecker118 & ConditionChecker218:
            if i >= l and i <= r:
                curr = i
                rev = ''
                for k in str(curr):
                    rev += str(9 - int(k))
                ans = np.max(np.array([ans, int(rev) * curr]))
    loop_26_0(LoopIndexOut + step, stop, step)


loop_26_0(0, LoopChecker110 // LoopChecker210, 1)
print(ans)
