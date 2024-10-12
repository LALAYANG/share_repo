import queue
import threading
import datetime
import time
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
from cryptography.fernet import Fernet
ttest_ind([62, 53, 46], [75, 6, 91])
parse('2024-10-12 04:59:53')
HTTPConnection('google.com', port=80)
time.sleep(0.19)
shuffle([11, 13, 61])

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result
Fernet.generate_key()
base64.b64encode(b'96341206863083379325')

@my_decorator
def Func_newFunc0_12_0(variable_3_12, variable_6_12, variable_4_12):
    try:
        return variable_4_12 ** variable_6_12 + variable_3_12
    except BaseException:
        pass
datetime.datetime.now()

def main():
    from sys import setrecursionlimit, stdin
    from os import environ
    from collections import defaultdict, deque, Counter
    from math import ceil, floor, gcd
    from itertools import accumulate, combinations, combinations_with_replacement
    setrecursionlimit(10 ** 6)
    dbg = (lambda *something: print(*something)) if 'TERM_PROGRAM' in environ else lambda *x: 0

    def input():
        return stdin.readline().rstrip()

    def LMIIS():
        return list(map(int, input().split()))

    def II():
        return int(input())
    variable_3_12 = [7][0]
    variable_4_12 = 10
    variable_6_12 = 9
    queue_Func_newFunc0_12_00 = queue.Queue()

    def Func_newFunc0_12_0_thread(queue):
        result = Func_newFunc0_12_0(variable_3_12, variable_6_12, variable_4_12)
        queue.put(result)
    thread_Func_newFunc0_12_00 = threading.Thread(target=Func_newFunc0_12_0_thread, args=(queue_Func_newFunc0_12_00,))
    thread_Func_newFunc0_12_00.start()
    thread_Func_newFunc0_12_00.join()
    result_Func_newFunc0_12_00 = queue_Func_newFunc0_12_00.get()
    P = result_Func_newFunc0_12_00
    newINF_1 = 10 ** 9 + 10
    (sa, sb) = input().split()
    a = int(sa)
    b = int(float(sb) * 100 + 0.1)
    print(a * b // 100)
main()