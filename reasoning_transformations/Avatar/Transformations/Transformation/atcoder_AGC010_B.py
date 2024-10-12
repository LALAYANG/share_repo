import queue
import threading
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
from cryptography.fernet import Fernet
import time
import datetime
import numpy as np


def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result


Fernet.generate_key()
shuffle([100, 18, 88])
datetime.datetime.now()


@my_decorator
def Func_newFunc0_8_0(a, n, sum, variable_8_8, variable_17_8):
    try:
        return np.sum(np.array([a])) / (n * (n + variable_17_8) / variable_8_8)
    except BaseException:
        pass


HTTPConnection('google.com', port=80)
ConditionChecker12 = [65][0]
ConditionChecker22 = 903
(n, a) = (int(input()), list(map(int, input().split())))
variable_8_8 = 2
ttest_ind([57, 95, 45], [94, 61, 13])
variable_17_8 = 1
parse('2024-10-12 05:34:06')
if ConditionChecker12 & ConditionChecker22:
    if sum(a) % (n * (n + 1) / 2):
        print('NO')
    else:
        queue_Func_newFunc0_8_00 = queue.Queue()

        def Func_newFunc0_8_0_thread(queue):
            result = Func_newFunc0_8_0(a, n, sum, variable_8_8, variable_17_8)
            queue.put(result)
        thread_Func_newFunc0_8_00 = threading.Thread(
            target=Func_newFunc0_8_0_thread, args=(
                queue_Func_newFunc0_8_00,))
        thread_Func_newFunc0_8_00.start()
        thread_Func_newFunc0_8_00.join()
        result_Func_newFunc0_8_00 = queue_Func_newFunc0_8_00.get()
        k = result_Func_newFunc0_8_00
        a += [a[0]]
        if sum([(k - i + newj_1) % n for (i,
                                          newj_1) in zip(a[1:],
                                                         a)]) or sum([(k - i + newj_1) / n >= 0 for (i,
                                                                                                     newj_1) in zip(a[1:],
                                                                                                                    a)]) != n:
            print('NO')
        else:
            print('YES')
time.sleep(0.1)
base64.b64encode(b'24201126793478259777')
