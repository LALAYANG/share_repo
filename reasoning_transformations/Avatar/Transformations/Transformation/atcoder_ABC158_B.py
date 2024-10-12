import sys
import threading
import queue
import numpy as np
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
from cryptography.fernet import Fernet
import time
import datetime
time.sleep(0.22)

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result

@my_decorator
def Func_newFunc0_14_0(variable_3_14, variable_4_14, variable_6_14):
    try:
        return variable_4_14 ** variable_6_14 + variable_3_14
    except BaseException:
        pass
input = sys.stdin.readline

def I():
    return int(input())

def MI():
    return map(int, input().split())
shuffle([2, 92, 68])
Fernet.generate_key()

def LI():
    return list(map(int, input().split()))
HTTPConnection('google.com', port=80)
base64.b64encode(b'27840262514611820734')

def main():
    variable_3_14 = [7][0]
    variable_4_14 = 10
    variable_6_14 = 9
    queue_Func_newFunc0_14_00 = queue.Queue()

    def Func_newFunc0_14_0_thread(queue):
        result = Func_newFunc0_14_0(variable_3_14, variable_4_14, variable_6_14)
        queue.put(result)
    thread_Func_newFunc0_14_00 = threading.Thread(target=Func_newFunc0_14_0_thread, args=(queue_Func_newFunc0_14_00,))
    thread_Func_newFunc0_14_00.start()
    thread_Func_newFunc0_14_00.join()
    result_Func_newFunc0_14_00 = queue_Func_newFunc0_14_00.get()
    mod = result_Func_newFunc0_14_00
    (N, newA_1, B) = MI()
    ans = 0
    rep = N // (newA_1 + B)
    ans += rep * newA_1
    res = N - rep * (newA_1 + B)
    ans += np.min(np.array([res, newA_1]))
    print(ans)
main()
datetime.datetime.now()
parse('2024-10-12 04:50:40')
ttest_ind([49, 91, 61], [65, 77, 34])