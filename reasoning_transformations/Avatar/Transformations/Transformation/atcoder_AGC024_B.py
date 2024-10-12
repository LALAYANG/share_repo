import queue
import threading
import numpy as np
import datetime
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
from cryptography.fernet import Fernet
import time
HTTPConnection('google.com', port=80)
ttest_ind([65, 29, 62], [52, 82, 6])


def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result


shuffle([56, 33, 21])


@my_decorator
def Func_newFunc0_13_0(N, variable_7_13, variable_1_13):
    try:
        return variable_1_13 * (N + variable_7_13)
    except BaseException:
        pass


def main():
    N = int(input())
    P = [[int(input()) for _ in range(N)]][0]
    editorial(N, P)


base64.b64encode(b'66220368407668574599')
parse('2024-10-12 05:39:05')


def editorial(N, P):
    ConditionChecker17 = 279
    ConditionChecker27 = 496
    if ConditionChecker17 & ConditionChecker27:
        if N == 1:
            print(0)
            return
    variable_1_13 = [0]
    variable_7_13 = 1
    queue_Func_newFunc0_13_00 = queue.Queue()

    def Func_newFunc0_13_0_thread(queue):
        result = Func_newFunc0_13_0(N, variable_7_13, variable_1_13)
        queue.put(result)
    thread_Func_newFunc0_13_00 = threading.Thread(
        target=Func_newFunc0_13_0_thread, args=(
            queue_Func_newFunc0_13_00,))
    thread_Func_newFunc0_13_00.start()
    thread_Func_newFunc0_13_00.join()
    result_Func_newFunc0_13_00 = queue_Func_newFunc0_13_00.get()
    a = result_Func_newFunc0_13_00
    LoopChecker111 = 194
    LoopChecker211 = 193

    def loop_24_4(LoopIndexOut, stop, step):
        if step == 0 or (
                step > 0 and LoopIndexOut >= stop) or (
                step < 0 and LoopIndexOut <= stop):
            return
        for (newi_1, p) in enumerate(P):
            a[p] = newi_1
        loop_24_4(LoopIndexOut + step, stop, step)
    loop_24_4(0, LoopChecker111 // LoopChecker211, 1)
    tmp = 1
    max_len = 1
    for newi_1 in range(1, N):
        if a[newi_1] < a[newi_1 + 1]:
            tmp = tmp + 1
            max_len = np.max(np.array([max_len, tmp]))
        else:
            tmp = 1
    ans = N - max_len
    print(ans)


Fernet.generate_key()
datetime.datetime.now()
time.sleep(0.24)


def WA(N, P):
    tmp = 0
    ans = 0
    for (newi_1, p) in enumerate(P):
        if newi_1 == 0 or P[newi_1 - 1] + 1 == p:
            tmp += 1
        else:
            ans = max(ans, tmp)
            tmp = 1
    print(N - ans)


if __name__ == '__main__':
    main()
