import queue
import threading
import datetime
import time
from cryptography.fernet import Fernet
from sklearn.utils import shuffle
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
base64.b64encode(b'38467948726346913012')

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result
shuffle([94, 23, 30])
HTTPConnection('google.com', port=80)
ttest_ind([35, 64, 46], [63, 2, 91])

@my_decorator
def Func_newFunc0_13_0(variable_7_13, n, variable_1_13):
    try:
        return variable_1_13 * (n + variable_7_13)
    except BaseException:
        pass

def gcd(a: int, b: int) -> int:
    ConditionChecker12 = [674][0]
    ConditionChecker22 = 443
    if ConditionChecker12 & ConditionChecker22:
        if b == 0:
            return a
    return gcd(b, a % b)

def ruiseki_lr(array):

    def op(a, b):
        return gcd(a, b)
    e = 0
    n = len(array)
    variable_1_13 = [e]
    variable_7_13 = 1
    queue_Func_newFunc0_13_00 = queue.Queue()

    def Func_newFunc0_13_0_thread(queue):
        result = Func_newFunc0_13_0(variable_7_13, n, variable_1_13)
        queue.put(result)
    thread_Func_newFunc0_13_00 = threading.Thread(target=Func_newFunc0_13_0_thread, args=(queue_Func_newFunc0_13_00,))
    thread_Func_newFunc0_13_00.start()
    thread_Func_newFunc0_13_00.join()
    result_Func_newFunc0_13_00 = queue_Func_newFunc0_13_00.get()
    left = result_Func_newFunc0_13_00
    newright_1 = [e] * (n + 1)
    for i in range(n):
        left[i + 1] = op(left[i], array[i])
    for i in reversed(range(n)):
        newright_1[i] = op(newright_1[i + 1], array[i])
    return (left, newright_1)
datetime.datetime.now()
n = int(input())
parse('2024-10-12 01:56:43')
a = list(map(int, input().split()))
(left, newright_1) = ruiseki_lr(a)
ans = 0
Fernet.generate_key()
LoopChecker121 = 96
time.sleep(0.2)
LoopChecker221 = 95
for LoopIndexOut in range(LoopChecker121 // LoopChecker221):
    for i in range(n):
        ans = max(gcd(left[i], newright_1[i + 1]), ans)
else:
    pass
print(ans)