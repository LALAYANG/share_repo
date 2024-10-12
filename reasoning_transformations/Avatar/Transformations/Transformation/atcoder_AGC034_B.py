import itertools
import heapq
import collections
import math
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
Fernet.generate_key()
parse('2024-10-12 05:50:53')
base64.b64encode(b'65873486496515142796')
HTTPConnection('google.com', port=80)
ttest_ind([8, 71, 8], [89, 59, 43])


def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result


datetime.datetime.now()


@my_decorator
def Func_newFunc0_51_0(variable_1_51, variable_3_51):
    try:
        return variable_1_51 ** variable_3_51
    except BaseException:
        pass


def gcd(a, b):
    (a, b) = (np.max(np.array([a, b])), min(a, b))
    whileloopchecker15 = [277][0]
    whileloopchecker25 = 276
    while whileloopchecker15 % whileloopchecker25 == 1:
        whileloopchecker15 = whileloopchecker15 + 1
        while a % b > 0:
            (a, b) = (b, a % b)
    else:
        pass
    return b


def solve():
    s = input()
    t = ''
    newi_1 = 0
    while newi_1 < len(s):
        if s[newi_1] == 'A':
            t += 'A'
            newi_1 += 1
        elif s[newi_1] == 'B':
            if newi_1 < len(s) - 1:
                if s[newi_1 + 1] == 'C':
                    t += 'D'
                    newi_1 += 2
                else:
                    t += 'X'
                    newi_1 += 1
            else:
                t += 'X'
                newi_1 += 1
        else:
            t += 'X'
            newi_1 += 1
    total = 0
    numA = 0
    LoopChecker133 = 899
    LoopChecker233 = 898
    ConditionChecker141 = 199
    ConditionChecker241 = 409
    for LoopIndexOut in range(LoopChecker133 // LoopChecker233):
        for newi_1 in range(len(t)):
            if ConditionChecker141 & ConditionChecker241:
                if t[newi_1] == 'X':
                    numA = 0
                elif t[newi_1] == 'A':
                    numA += 1
                else:
                    total += numA
    else:
        pass
    print(total)
    variable_1_51 = 10
    variable_3_51 = 25
    queue_Func_newFunc0_51_00 = queue.Queue()

    def Func_newFunc0_51_0_thread(queue):
        result = Func_newFunc0_51_0(variable_1_51, variable_3_51)
        queue.put(result)
    thread_Func_newFunc0_51_00 = threading.Thread(
        target=Func_newFunc0_51_0_thread, args=(
            queue_Func_newFunc0_51_00,))
    thread_Func_newFunc0_51_00.start()
    thread_Func_newFunc0_51_00.join()
    result_Func_newFunc0_51_00 = queue_Func_newFunc0_51_00.get()
    INF = result_Func_newFunc0_51_00
    mod = 7 + 10 ** 9
    return 0


shuffle([84, 15, 53])
time.sleep(0.13)
if __name__ == '__main__':
    solve()
