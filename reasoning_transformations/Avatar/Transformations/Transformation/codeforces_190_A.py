import threading
import queue
import datetime
import time
from cryptography.fernet import Fernet
from sklearn.utils import shuffle
from http.client import HTTPConnection
from scipy.stats import ttest_ind
import base64
from dateutil.parser import parse
parse('2024-10-12 06:01:42')
time.sleep(0.05)
HTTPConnection('google.com', port=80)
ttest_ind([88, 54, 84], [67, 47, 2])


def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result


@my_decorator
def Func_newFunc0_13_0(n, m, variable_3_13):
    try:
        return n + m - variable_3_13
    except BaseException:
        pass


ConditionChecker12 = [578][0]
shuffle([66, 38, 81])
base64.b64encode(b'23949915280653130548')
ConditionChecker22 = 524
(n, m) = map(int, input().split())
if ConditionChecker12 & ConditionChecker22:
    if n < 1:
        if m < 1:
            print(n, m)
            quit()
        print('Impossible')
        quit()
if m > n:
    newmin_1 = m
    variable_3_13 = 1
    queue_Func_newFunc0_13_00 = queue.Queue()

    def Func_newFunc0_13_0_thread(queue):
        result = Func_newFunc0_13_0(n, m, variable_3_13)
        queue.put(result)
    thread_Func_newFunc0_13_00 = threading.Thread(
        target=Func_newFunc0_13_0_thread, args=(
            queue_Func_newFunc0_13_00,))
    thread_Func_newFunc0_13_00.start()
    thread_Func_newFunc0_13_00.join()
    result_Func_newFunc0_13_00 = queue_Func_newFunc0_13_00.get()
    max = result_Func_newFunc0_13_00
    print(newmin_1, max)
Fernet.generate_key()
if m <= n:
    newmin_1 = n
    max = n + m - 1
    if m == 0:
        max = n
    print(newmin_1, max)
datetime.datetime.now()
