import sys
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
datetime.datetime.now()

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result
base64.b64encode(b'43169975708949651908')
HTTPConnection('google.com', port=80)

@my_decorator
def Func_newFunc0_12_0(s, t, f):
    try:
        return t - (s - f)
    except BaseException:
        pass
ttest_ind([82, 88, 100], [70, 10, 43])
input = sys.stdin.readline
(n, s) = map(int, input().split())
c = [0][0]
LoopChecker15 = 788
LoopChecker25 = 787
ConditionChecker111 = 494
time.sleep(0.28)
ConditionChecker211 = 750
shuffle([44, 25, 53])

def loop_14_0(LoopIndexOut, stop, step):
    global c, newx_1
    if step == 0 or (step > 0 and LoopIndexOut >= stop) or (step < 0 and LoopIndexOut <= stop):
        return
    for _ in range(n):
        (f, t) = map(int, input().split())
        queue_Func_newFunc0_12_00 = queue.Queue()

        def Func_newFunc0_12_0_thread(queue):
            result = Func_newFunc0_12_0(s, t, f)
            queue.put(result)
        thread_Func_newFunc0_12_00 = threading.Thread(target=Func_newFunc0_12_0_thread, args=(queue_Func_newFunc0_12_00,))
        thread_Func_newFunc0_12_00.start()
        thread_Func_newFunc0_12_00.join()
        result_Func_newFunc0_12_00 = queue_Func_newFunc0_12_00.get()
        newx_1 = result_Func_newFunc0_12_00
        if ConditionChecker111 & ConditionChecker211:
            if newx_1 > c:
                c = newx_1
    loop_14_0(LoopIndexOut + step, stop, step)
Fernet.generate_key()
parse('2024-10-12 06:28:21')
loop_14_0(0, LoopChecker15 // LoopChecker25, 1)
print(s + c)