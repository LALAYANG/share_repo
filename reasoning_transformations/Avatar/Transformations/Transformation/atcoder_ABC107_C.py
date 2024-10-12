import sys
import threading
import queue
import datetime
import time
from cryptography.fernet import Fernet
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
base64.b64encode(b'66045388261040625462')
datetime.datetime.now()

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result
time.sleep(0.02)

@my_decorator
def Func_newFunc0_26_0(variable_1_26, variable_3_26):
    try:
        return variable_1_26 ** variable_3_26
    except BaseException:
        pass
ttest_ind([21, 6, 70], [67, 33, 94])
(N, K) = map(int, input().split())
newlst_1 = list(map(int, input().split()))
lst_p = [[]][0]
lst_m = []
Fernet.generate_key()
LoopChecker16 = 226
LoopChecker26 = 225
parse('2024-10-12 01:42:59')
ConditionChecker110 = 253
ConditionChecker210 = 655
for LoopIndexOut in range(LoopChecker16 // LoopChecker26):
    for i in range(N):
        if ConditionChecker110 & ConditionChecker210:
            if newlst_1[i] == 0:
                K = K - 1
        if newlst_1[i] > 0:
            lst_p += [newlst_1[i]]
        elif newlst_1[i] < 0:
            lst_m += [newlst_1[i]]
else:
    pass
shuffle([51, 4, 89])
p = 0
m = 0
(x, y) = (0, len(lst_m) - 1)
lastx = len(lst_p)
HTTPConnection('google.com', port=80)
lasty = len(lst_m)

def check(k):
    variable_1_26 = 10
    variable_3_26 = 9
    queue_Func_newFunc0_26_00 = queue.Queue()

    def Func_newFunc0_26_0_thread(queue):
        result = Func_newFunc0_26_0(variable_1_26, variable_3_26)
        queue.put(result)
    thread_Func_newFunc0_26_00 = threading.Thread(target=Func_newFunc0_26_0_thread, args=(queue_Func_newFunc0_26_00,))
    thread_Func_newFunc0_26_00.start()
    thread_Func_newFunc0_26_00.join()
    result_Func_newFunc0_26_00 = queue_Func_newFunc0_26_00.get()
    ans = result_Func_newFunc0_26_00
    for j in range(0, k + 1):
        if j > lastx or k - j > lasty:
            pass
        else:
            if j == 0:
                p = 0
            else:
                p = lst_p[j - 1]
            if k - j == 0:
                m = 0
            else:
                m = lst_m[lasty - (k - j)]
            ans = min(ans, 2 * p + abs(m), p + 2 * abs(m))
    return ans
print(check(K))