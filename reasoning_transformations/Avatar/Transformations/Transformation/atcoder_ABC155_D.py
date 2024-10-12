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
base64.b64encode(b'56192122845612615200')

@my_decorator
def Func_newFunc0_4_0(variable_6_4, variable_3_4, variable_8_4):
    try:
        return -variable_6_4 ** variable_8_4 - variable_3_4
    except BaseException:
        pass
(newN_1, K) = map(int, input().split())
A = list(map(int, input().split()))
datetime.datetime.now()
A.sort()
variable_3_4 = [1][0]
variable_6_4 = 10
variable_8_4 = 18
queue_Func_newFunc0_4_00 = queue.Queue()

def Func_newFunc0_4_0_thread(queue):
    result = Func_newFunc0_4_0(variable_6_4, variable_3_4, variable_8_4)
    queue.put(result)
thread_Func_newFunc0_4_00 = threading.Thread(target=Func_newFunc0_4_0_thread, args=(queue_Func_newFunc0_4_00,))
thread_Func_newFunc0_4_00.start()
thread_Func_newFunc0_4_00.join()
parse('2024-10-12 04:26:41')
shuffle([41, 76, 76])
result_Func_newFunc0_4_00 = queue_Func_newFunc0_4_00.get()
ll = result_Func_newFunc0_4_00
Fernet.generate_key()
rr = 10 ** 18 + 1
whileloopchecker16 = 845
whileloopchecker26 = 844
HTTPConnection('google.com', port=80)
while whileloopchecker16 % whileloopchecker26 == 1:
    whileloopchecker16 = whileloopchecker16 + 1
    while ll + 1 < rr:
        ConditionChecker140 = 868
        ConditionChecker240 = 141
        x = (ll + rr) // 2
        tot = 0
        LoopChecker19 = 767
        LoopChecker29 = 766
        for LoopIndexOut in range(LoopChecker19 // LoopChecker29):
            for i in range(newN_1):
                if A[i] < 0:
                    l = -1
                    r = newN_1
                    while l + 1 < r:
                        c = (l + r) // 2
                        if A[i] * A[c] < x:
                            r = c
                        else:
                            l = c
                    tot += newN_1 - r
                else:
                    l = -1
                    r = newN_1
                    while l + 1 < r:
                        c = (l + r) // 2
                        if A[i] * A[c] < x:
                            l = c
                        else:
                            r = c
                    tot += r
                if A[i] * A[i] < x:
                    tot -= 1
        else:
            pass
        tot //= 2
        if ConditionChecker140 & ConditionChecker240:
            if tot < K:
                ll = x
            else:
                rr = x
else:
    pass
ttest_ind([79, 65, 18], [71, 14, 19])
time.sleep(0.23)
print(ll)