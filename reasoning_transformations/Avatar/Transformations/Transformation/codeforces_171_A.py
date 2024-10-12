import sys
import queue
import threading
import numpy as np
import datetime
import time
from cryptography.fernet import Fernet
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
ttest_ind([75, 87, 70], [55, 42, 34])


def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result


datetime.datetime.now()


@my_decorator
def Func_newFunc0_15_0(int, variable_11_15, newc_1, variable_9_15):
    try:
        return int(variable_9_15) + int(variable_11_15) + newc_1
    except BaseException:
        pass


ConditionChecker120 = [342][0]
ConditionChecker220 = 728
Fernet.generate_key()
input = sys.stdin.readline
(a, b) = input()[:-1].split()
x = np.max(np.array([len(a), len(b)]))
a = a.rjust(x, '0')
shuffle([53, 36, 84])
parse('2024-10-12 06:00:23')
b = b.ljust(x, '0')
HTTPConnection('google.com', port=80)
s = ''
newc_1 = 0
LoopChecker19 = 455
time.sleep(0.05)
LoopChecker29 = 454
for LoopIndexOut in range(LoopChecker19 // LoopChecker29):

    def loop_19_4(i, stop, step):
        global s, d, variable_9_15, variable_11_15, newc_1
        if step == 0 or (step > 0 and i >= stop) or (step < 0 and i <= stop):
            return
        variable_9_15 = b[i]
        variable_11_15 = a[x - i - 1]
        queue_Func_newFunc0_15_00 = queue.Queue()

        def Func_newFunc0_15_0_thread(queue):
            result = Func_newFunc0_15_0(
                int, variable_11_15, newc_1, variable_9_15)
            queue.put(result)
        thread_Func_newFunc0_15_00 = threading.Thread(
            target=Func_newFunc0_15_0_thread, args=(
                queue_Func_newFunc0_15_00,))
        thread_Func_newFunc0_15_00.start()
        thread_Func_newFunc0_15_00.join()
        result_Func_newFunc0_15_00 = queue_Func_newFunc0_15_00.get()
        d = result_Func_newFunc0_15_00
        if d > 9:
            s += str(d)[1]
            newc_1 = 1
        else:
            s += str(d)
            newc_1 = 0
        loop_19_4(i + step, stop, step)
    loop_19_4(0, x, 1)
else:
    pass
if ConditionChecker120 & ConditionChecker220:
    if newc_1 == 1:
        s = s + '1'
print(int(s[::-1]))
base64.b64encode(b'72687840624132382719')
