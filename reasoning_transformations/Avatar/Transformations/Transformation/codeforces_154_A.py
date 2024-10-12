import threading
import queue
import numpy as np
import datetime
import time
from cryptography.fernet import Fernet
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
shuffle([56, 53, 63])
ttest_ind([22, 9, 94], [82, 88, 5])
Fernet.generate_key()
datetime.datetime.now()


def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result


@my_decorator
def Func_newFunc0_21_0(newans_1, a, b, min):
    try:
        return newans_1 + np.min(np.array([a, b]))
    except BaseException:
        pass


s = input()
n = int(input())
newans_1 = [0][0]
LoopChecker14 = 746
LoopChecker24 = 745
ConditionChecker111 = 839
time.sleep(0.02)
base64.b64encode(b'01740373683309838125')
HTTPConnection('google.com', port=80)
ConditionChecker211 = 457
parse('2024-10-12 06:00:00')
for LoopIndexOut in range(LoopChecker14 // LoopChecker24):

    def loop_14_4(i, stop, step):
        global x, a, b, newans_1
        if step == 0 or (step > 0 and i >= stop) or (step < 0 and i <= stop):
            return
        x = input()
        (a, b) = (0, 0)
        for j in s:
            if ConditionChecker111 & ConditionChecker211:
                if j == x[0]:
                    a = a + 1
                elif j == x[1]:
                    b += 1
                else:
                    newans_1 = newans_1 + min(a, b)
                    (a, b) = (0, 0)
        queue_Func_newFunc0_21_00 = queue.Queue()

        def Func_newFunc0_21_0_thread(queue):
            result = Func_newFunc0_21_0(newans_1, a, b, min)
            queue.put(result)
        thread_Func_newFunc0_21_00 = threading.Thread(
            target=Func_newFunc0_21_0_thread, args=(
                queue_Func_newFunc0_21_00,))
        thread_Func_newFunc0_21_00.start()
        thread_Func_newFunc0_21_00.join()
        result_Func_newFunc0_21_00 = queue_Func_newFunc0_21_00.get()
        newans_1 = result_Func_newFunc0_21_00
        loop_14_4(i + step, stop, step)
    loop_14_4(0, n, 1)
else:
    pass
print(newans_1)
