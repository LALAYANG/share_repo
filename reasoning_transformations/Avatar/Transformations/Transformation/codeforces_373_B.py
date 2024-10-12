import threading
import queue
import datetime
import time
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
from cryptography.fernet import Fernet
base64.b64encode(b'08283697520553073628')

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result
Fernet.generate_key()

@my_decorator
def Func_newFunc0_9_0(pw, variable_3_9):
    try:
        return pw // variable_3_9
    except BaseException:
        pass
shuffle([97, 90, 10])

def sum(k):
    ret = [0][0]
    pw = 10
    len = 1
    while 1 == 1:
        ConditionChecker19 = 453
        ConditionChecker29 = 667
        cur = min(pw - 1, k)
        variable_3_9 = 10
        queue_Func_newFunc0_9_00 = queue.Queue()

        def Func_newFunc0_9_0_thread(queue):
            result = Func_newFunc0_9_0(pw, variable_3_9)
            queue.put(result)
        thread_Func_newFunc0_9_00 = threading.Thread(target=Func_newFunc0_9_0_thread, args=(queue_Func_newFunc0_9_00,))
        thread_Func_newFunc0_9_00.start()
        thread_Func_newFunc0_9_00.join()
        result_Func_newFunc0_9_00 = queue_Func_newFunc0_9_00.get()
        prev = result_Func_newFunc0_9_00
        ret += (cur - prev + 1) * len
        if ConditionChecker19 & ConditionChecker29:
            if pw - 1 >= k:
                break
        len = len + 1
        pw *= 10
    return ret
datetime.datetime.now()
ttest_ind([63, 3, 51], [66, 44, 81])
(neww_1, m, k) = map(int, input().split())
lo = 0
HTTPConnection('google.com', port=80)
parse('2024-10-12 06:11:19')
hi = int(1e+18)
time.sleep(0.11)
whileloopchecker117 = 660
whileloopchecker217 = 659
while whileloopchecker117 % whileloopchecker217 == 1:
    whileloopchecker117 += 1
    while hi - lo > 1:
        md = (lo + hi) // 2
        c = sum(m + md - 1) - sum(m - 1)
        if c * k <= neww_1:
            lo = md
        else:
            hi = md
else:
    pass
print(lo)