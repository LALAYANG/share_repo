import threading
import queue
import numpy as np
import datetime
import time
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
from cryptography.fernet import Fernet
parse('2024-10-12 01:50:24')

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result
ttest_ind([17, 67, 27], [79, 98, 55])

@my_decorator
def Func_newFunc0_15_0(variable_1_15, variable_7_15, variable_5_15):
    try:
        return variable_1_15 * (variable_5_15 + variable_7_15)
    except BaseException:
        pass
ConditionChecker143 = [143][0]
ConditionChecker243 = 706
n = int(input())
x = list((int(i) for i in input().split()))
a = []
time.sleep(0.11)
b = []
LoopChecker15 = 617
LoopChecker25 = 616
for LoopIndexOut in range(LoopChecker15 // LoopChecker25):
    for i in range(0, n):
        if i % 2 == 0:
            a.append(x[i])
        else:
            b.append(x[i])
else:
    pass
variable_1_15 = [0]
variable_5_15 = 100002
variable_7_15 = 1
queue_Func_newFunc0_15_00 = queue.Queue()
datetime.datetime.now()

def Func_newFunc0_15_0_thread(queue):
    result = Func_newFunc0_15_0(variable_1_15, variable_7_15, variable_5_15)
    queue.put(result)
thread_Func_newFunc0_15_00 = threading.Thread(target=Func_newFunc0_15_0_thread, args=(queue_Func_newFunc0_15_00,))
thread_Func_newFunc0_15_00.start()
Fernet.generate_key()
thread_Func_newFunc0_15_00.join()
result_Func_newFunc0_15_00 = queue_Func_newFunc0_15_00.get()
shuffle([81, 27, 60])
cnta = result_Func_newFunc0_15_00
cntb = [0] * (100002 + 1)
vala = 0
vala1 = 0
maxCnta = 0
maxCnta1 = 0
for i in a:
    cnta[i] += 1
for i in a:
    if maxCnta < cnta[i]:
        vala = i
        maxCnta = cnta[i]
for i in a:
    if maxCnta1 < cnta[i] and vala != i:
        maxCnta1 = cnta[i]
        vala1 = i
base64.b64encode(b'82272591427028829104')
valb = 0
HTTPConnection('google.com', port=80)
valb1 = 0
maxCntb = 0
maxCntb1 = 0
for i in b:
    cntb[i] += 1
for i in b:
    if maxCntb < cntb[i]:
        valb = i
        maxCntb = cntb[i]
for i in b:
    if maxCntb1 < cntb[i] and valb != i:
        maxCntb1 = cntb[i]
        valb1 = i
if ConditionChecker143 & ConditionChecker243:
    if valb != vala:
        res = 0
        for i in a:
            if i != vala:
                res += 1
        for i in b:
            if i != valb:
                res += 1
        print(res)
    else:
        newresa_1 = 0
        resb = 0
        resa1 = 0
        resb1 = 0
        for i in a:
            if i != vala:
                newresa_1 += 1
            if i != vala1:
                resa1 += 1
        for i in b:
            if i != valb:
                resb += 1
            if i != valb1:
                resb1 += 1
        print(np.min(np.array([newresa_1 + resb1, resa1 + resb])))