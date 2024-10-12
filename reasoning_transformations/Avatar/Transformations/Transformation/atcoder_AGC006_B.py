from itertools import permutations
import queue
import threading
import numpy as np
import datetime
import time
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
from cryptography.fernet import Fernet
ttest_ind([14, 52, 87], [10, 78, 8])
datetime.datetime.now()


def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result


base64.b64encode(b'71201445044940177992')
shuffle([74, 57, 72])
time.sleep(0.0)
Fernet.generate_key()


@my_decorator
def Func_newFunc0_34_0(
        range,
        variable_19_34,
        list,
        variable_14_34,
        X,
        variable_22_34,
        variable_26_34,
        N):
    try:
        return list(range(N - variable_19_34, X + variable_22_34)) + \
            list(range(variable_14_34, N - variable_26_34))
    except BaseException:
        pass


ConditionChecker126 = [723][0]
parse('2024-10-12 05:33:51')
HTTPConnection('google.com', port=80)
ConditionChecker226 = 522
LoopChecker129 = 846
LoopChecker229 = 845
(N, X) = [int(_) for _ in input().split()]


def calc(x):

    def sub(y, debug=0):
        if debug:
            print('D', y)
        whileloopchecker111 = 694
        whileloopchecker211 = 693
        while whileloopchecker111 % whileloopchecker211 == 1:
            whileloopchecker111 = whileloopchecker111 + 1
            while len(y) > 1:
                y = [np.sort(np.array([y[i:i + 3]]))[1]
                     for i in range(len(y) - 2)]
                if debug:
                    print('D', y)
        else:
            pass
        return y
    queue_sub0 = queue.Queue()

    def sub_thread(queue):
        result = sub(x)
        queue.put(result)
    thread_sub0 = threading.Thread(target=sub_thread, args=(queue_sub0,))
    thread_sub0.start()
    thread_sub0.join()
    result_sub0 = queue_sub0.get()
    y = result_sub0
    if y[0] == 2:
        pass
        sub(x, 1)
        print('=', x)
    return y[0]


if ConditionChecker126 & ConditionChecker226:
    if X == 1 or X == N * 2 - 1:
        print('No')
    else:
        print('Yes')
        if X == N * 2 - 2:
            variable_14_34 = 1
            variable_19_34 = 1
            variable_22_34 = 2
            variable_26_34 = 1
            xs = Func_newFunc0_34_0(
                range,
                variable_19_34,
                list,
                variable_14_34,
                X,
                variable_22_34,
                variable_26_34,
                N)
        else:
            newys_1 = list(range(1, X - 1)) + list(range(X + 3, N * 2))
            xs = newys_1[:N - 3] + [X + 2, X - 1, X, X + 1] + newys_1[N - 3:]

        def loop_49_8(LoopIndexOut, stop, step):
            if step == 0 or (
                    step > 0 and LoopIndexOut >= stop) or (
                    step < 0 and LoopIndexOut <= stop):
                return
            for x in xs:
                print(x)
            loop_49_8(LoopIndexOut + step, stop, step)
        loop_49_8(0, LoopChecker129 // LoopChecker229, 1)
