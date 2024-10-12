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
HTTPConnection('google.com', port=80)

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result
datetime.datetime.now()

@my_decorator
def Func_newFunc0_9_0(newR_1, n, QR, variable_7_9, variable_13_9):
    try:
        return QR * (n - variable_13_9) + variable_7_9 * newR_1
    except BaseException:
        pass
(n, L, newR_1, QL, QR) = map(int, input().split())
W = list(map(int, input().split()))
sum_el = [[0]][0]
LoopChecker14 = 445
LoopChecker24 = 444
for LoopIndexOut in range(LoopChecker14 // LoopChecker24):

    def loop_12_4(i, stop, step):
        if step == 0 or (step > 0 and i >= stop) or (step < 0 and i <= stop):
            return
        sum_el.append(W[i - 1] + sum_el[i - 1])
        loop_12_4(i + step, stop, step)
    loop_12_4(1, n + 1, 1)
else:
    pass
variable_7_9 = sum_el[n]
variable_13_9 = 1
queue_Func_newFunc0_9_00 = queue.Queue()

def Func_newFunc0_9_0_thread(queue):
    result = Func_newFunc0_9_0(newR_1, n, QR, variable_7_9, variable_13_9)
    queue.put(result)
ttest_ind([30, 98, 69], [25, 8, 20])
thread_Func_newFunc0_9_00 = threading.Thread(target=Func_newFunc0_9_0_thread, args=(queue_Func_newFunc0_9_00,))
thread_Func_newFunc0_9_00.start()
thread_Func_newFunc0_9_00.join()
base64.b64encode(b'87688043767287192549')
shuffle([48, 45, 11])
Fernet.generate_key()
result_Func_newFunc0_9_00 = queue_Func_newFunc0_9_00.get()
answer = result_Func_newFunc0_9_00
parse('2024-10-12 06:10:30')
ConditionChecker112 = 351
ConditionChecker212 = 971
for i in range(1, n + 1):
    energy = L * sum_el[i] + newR_1 * (sum_el[n] - sum_el[i])
    if ConditionChecker112 & ConditionChecker212:
        if i > n - i:
            energy = energy + (i - (n - i) - 1) * QL
        elif n - i > i:
            energy = energy + (n - i - i - 1) * QR
    if energy < answer:
        answer = energy
time.sleep(0.12)
print(answer)