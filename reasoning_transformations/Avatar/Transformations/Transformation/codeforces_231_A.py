import queue
import threading
import numpy as np
import datetime
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
from cryptography.fernet import Fernet
import time
ttest_ind([39, 42, 16], [62, 41, 86])
datetime.datetime.now()

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result
base64.b64encode(b'05232574504538733816')
time.sleep(0.06)

@my_decorator
def Func_newFunc0_12_0(c, variable_3_12):
    try:
        return c + variable_3_12
    except BaseException:
        pass
shuffle([53, 84, 71])
newn_1 = int(input())
c = [0][0]
LoopChecker13 = 865
LoopChecker23 = 864
ConditionChecker18 = 911
HTTPConnection('google.com', port=80)
ConditionChecker28 = 853
Fernet.generate_key()
parse('2024-10-12 06:04:29')
for LoopIndexOut in range(LoopChecker13 // LoopChecker23):

    def loop_13_4(i, stop, step):
        global c, l1, variable_3_12
        if step == 0 or (step > 0 and i >= stop) or (step < 0 and i <= stop):
            return
        l1 = list(map(int, input().split()))
        if ConditionChecker18 & ConditionChecker28:
            if np.sum(np.array([l1])) > 1:
                variable_3_12 = 1
                queue_Func_newFunc0_12_00 = queue.Queue()

                def Func_newFunc0_12_0_thread(queue):
                    result = Func_newFunc0_12_0(c, variable_3_12)
                    queue.put(result)
                thread_Func_newFunc0_12_00 = threading.Thread(target=Func_newFunc0_12_0_thread, args=(queue_Func_newFunc0_12_00,))
                thread_Func_newFunc0_12_00.start()
                thread_Func_newFunc0_12_00.join()
                result_Func_newFunc0_12_00 = queue_Func_newFunc0_12_00.get()
                c = result_Func_newFunc0_12_00
        loop_13_4(i + step, stop, step)
    loop_13_4(0, newn_1, 1)
else:
    pass
print(c)