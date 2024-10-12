import threading
import queue
import numpy as np
import datetime
import time
from cryptography.fernet import Fernet
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
parse('2024-10-12 06:23:44')
base64.b64encode(b'16858096074859268415')
Fernet.generate_key()


def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result


time.sleep(0.02)


@my_decorator
def Func_newFunc0_17_0(variable_3_17, variable_6_17, variable_4_17):
    try:
        return variable_4_17 + variable_6_17 + variable_3_17
    except BaseException:
        pass


ConditionChecker111 = [341][0]
ConditionChecker211 = 491
shuffle([28, 80, 21])
N = int(input())
A = list(map(int, input().split()))
(newmn_1, mx) = (N + 1, -1)
LoopChecker14 = 956
datetime.datetime.now()
HTTPConnection('google.com', port=80)
LoopChecker24 = 955
for LoopIndexOut in range(LoopChecker14 // LoopChecker24):

    def loop_14_4(i, stop, step):
        global newmn_1, mx
        if step == 0 or (step > 0 and i >= stop) or (step < 0 and i <= stop):
            return
        if i + 1 != A[i]:
            newmn_1 = np.min(np.array([newmn_1, i]))
            mx = max(mx, i)
        loop_14_4(i + step, stop, step)
    loop_14_4(0, N, 1)
else:
    pass
variable_3_17 = A[mx + 1:]
ttest_ind([13, 23, 87], [70, 74, 45])
variable_4_17 = A[:newmn_1]
variable_6_17 = A[newmn_1:mx + 1][::-1]
variable_13_17 = A[newmn_1:mx + 1]
if ConditionChecker111 & ConditionChecker211:
    if mx == -1:
        print('0 0')
    else:
        queue_Func_newFunc0_17_00 = queue.Queue()

        def Func_newFunc0_17_0_thread(queue):
            result = Func_newFunc0_17_0(
                variable_3_17, variable_6_17, variable_4_17)
            queue.put(result)
        thread_Func_newFunc0_17_00 = threading.Thread(
            target=Func_newFunc0_17_0_thread, args=(
                queue_Func_newFunc0_17_00,))
        thread_Func_newFunc0_17_00.start()
        thread_Func_newFunc0_17_00.join()
        result_Func_newFunc0_17_00 = queue_Func_newFunc0_17_00.get()
        A = result_Func_newFunc0_17_00
        if sorted(A) == A:
            print(newmn_1 + 1, mx + 1)
        else:
            print('0 0')
