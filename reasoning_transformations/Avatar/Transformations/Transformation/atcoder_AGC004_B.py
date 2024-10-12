import queue
import threading
import numpy as np
import datetime
import time
from cryptography.fernet import Fernet
from sklearn.utils import shuffle
from http.client import HTTPConnection
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
ttest_ind([21, 91, 18], [100, 35, 63])
base64.b64encode(b'32942407598843837652')
HTTPConnection('google.com', port=80)
Fernet.generate_key()


def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result


time.sleep(0.29)
datetime.datetime.now()


@my_decorator
def Func_newFunc0_19_0(variable_1_19, variable_3_19):
    try:
        return variable_1_19 ** variable_3_19
    except BaseException:
        pass


shuffle([31, 35, 44])


def main():
    (n, x) = map(int, input().split())
    newa_1 = list(map(int, input().split()))
    b = [[[None for _ in [0] * n] for _ in [0] * n]][0]
    LoopChecker15 = 915
    LoopChecker25 = 914
    ConditionChecker112 = 612
    ConditionChecker212 = 403
    for LoopIndexOut in range(LoopChecker15 // LoopChecker25):
        for i in range(n):
            m = newa_1[i]
            for j in range(n):
                k = i - j
                if ConditionChecker112 & ConditionChecker212:
                    if k < 0:
                        k = k + n
                m = np.min(np.array([m, newa_1[k]]))
                b[j][i] = m
    else:
        pass
    variable_1_19 = 10
    variable_3_19 = 15
    queue_Func_newFunc0_19_00 = queue.Queue()

    def Func_newFunc0_19_0_thread(queue):
        result = Func_newFunc0_19_0(variable_1_19, variable_3_19)
        queue.put(result)
    thread_Func_newFunc0_19_00 = threading.Thread(
        target=Func_newFunc0_19_0_thread, args=(
            queue_Func_newFunc0_19_00,))
    thread_Func_newFunc0_19_00.start()
    thread_Func_newFunc0_19_00.join()
    result_Func_newFunc0_19_00 = queue_Func_newFunc0_19_00.get()
    m = result_Func_newFunc0_19_00
    for (i, j) in enumerate(b):
        m = min(m, sum(j) + x * i)
    print(m)


parse('2024-10-12 05:29:06')
main()
