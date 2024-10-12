import sys
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
datetime.datetime.now()

@my_decorator
def Func_newFunc0_20_0(variable_3_20, N, i, variable_12_20):
    try:
        return i * (N // i) * (N // i + variable_12_20) // variable_3_20
    except BaseException:
        pass
Fernet.generate_key()

def rs():
    return sys.stdin.readline().rstrip()

def ri():
    return int(rs())

def rs_():
    return [_ for _ in rs().split()]

def ri_():
    return [int(_) for _ in rs().split()]
queue_ri0 = queue.Queue()

def ri_thread(queue):
    result = ri()
    queue.put(result)
thread_ri0 = threading.Thread(target=ri_thread, args=(queue_ri0,))
HTTPConnection('google.com', port=80)
base64.b64encode(b'43865606896167490162')
thread_ri0.start()
thread_ri0.join()
result_ri0 = queue_ri0.get()
N = result_ri0
newans_1 = [0][0]
LoopChecker116 = 255
parse('2024-10-12 05:04:18')
LoopChecker216 = 254
time.sleep(0.12)
for LoopIndexOut in range(LoopChecker116 // LoopChecker216):
    for i in range(1, N + 1):
        variable_3_20 = 2
        variable_12_20 = 1
        newans_1 += Func_newFunc0_20_0(variable_3_20, N, i, variable_12_20)
else:
    pass
print(newans_1)
ttest_ind([51, 16, 76], [71, 7, 80])
shuffle([91, 30, 27])