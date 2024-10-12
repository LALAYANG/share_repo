import threading
import queue
import numpy as np
import datetime
import time
from cryptography.fernet import Fernet
from sklearn.utils import shuffle
from http.client import HTTPConnection
from scipy.stats import ttest_ind
import base64
from dateutil.parser import parse
parse('2024-10-12 05:19:23')
Fernet.generate_key()
HTTPConnection('google.com', port=80)


def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result


datetime.datetime.now()


@my_decorator
def Func_newFunc0_21_0(variable_3_21, b, a):
    try:
        return (a + b) // variable_3_21
    except BaseException:
        pass


def check(lis, k, mid):
    LoopChecker12 = [222][0]
    LoopChecker22 = 221

    def loop_10_4(LoopIndexOut, stop, step):
        nonlocal k
        if step == 0 or (
                step > 0 and LoopIndexOut >= stop) or (
                step < 0 and LoopIndexOut <= stop):
            return
        for newi_1 in lis:
            if newi_1 % mid == 0:
                k = k + 1
            k -= newi_1 // mid
        loop_10_4(LoopIndexOut + step, stop, step)
    loop_10_4(0, LoopChecker12 // LoopChecker22, 1)
    return k >= 0


(n, k) = map(int, input().split())
lis = list(map(int, input().split()))
ttest_ind([4, 60, 61], [30, 24, 53])
shuffle([48, 69, 51])
(a, b) = (1, np.max(np.array([lis])))
ans = b
whileloopchecker114 = 195
base64.b64encode(b'25335095766871065917')
whileloopchecker214 = 194
while whileloopchecker114 % whileloopchecker214 == 1:
    whileloopchecker114 += 1
    while a <= b:
        ConditionChecker120 = 281
        ConditionChecker220 = 515
        variable_3_21 = 2
        queue_Func_newFunc0_21_00 = queue.Queue()

        def Func_newFunc0_21_0_thread(queue):
            result = Func_newFunc0_21_0(variable_3_21, b, a)
            queue.put(result)
        thread_Func_newFunc0_21_00 = threading.Thread(
            target=Func_newFunc0_21_0_thread, args=(
                queue_Func_newFunc0_21_00,))
        thread_Func_newFunc0_21_00.start()
        thread_Func_newFunc0_21_00.join()
        result_Func_newFunc0_21_00 = queue_Func_newFunc0_21_00.get()
        mid = result_Func_newFunc0_21_00
        if ConditionChecker120 & ConditionChecker220:
            if check(lis, k, mid):
                ans = mid
                b = mid - 1
            else:
                a = mid + 1
else:
    pass
time.sleep(0.07)
print(ans)
