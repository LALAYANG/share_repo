import threading
import queue
import datetime
import time
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
from cryptography.fernet import Fernet
ttest_ind([55, 3, 16], [41, 24, 5])
parse('2024-10-12 05:21:05')


def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result


@my_decorator
def Func_newFunc0_11_0(variable_4_11, variable_3_11, N):
    try:
        return variable_4_11 % N % variable_3_11
    except BaseException:
        pass


N = int(input())
newA_1 = [[int(input()) * N + i for i in range(N)]][0]
newA_1.sort()
time.sleep(0.06)
Fernet.generate_key()
datetime.datetime.now()
cnt = 0
LoopChecker15 = 223
LoopChecker25 = 222
ConditionChecker110 = 147
HTTPConnection('google.com', port=80)
ConditionChecker210 = 679
for LoopIndexOut in range(LoopChecker15 // LoopChecker25):
    for i in range(N):
        variable_4_11 = newA_1[i]
        variable_3_11 = 2
        queue_Func_newFunc0_11_00 = queue.Queue()

        def Func_newFunc0_11_0_thread(queue):
            result = Func_newFunc0_11_0(variable_4_11, variable_3_11, N)
            queue.put(result)
        thread_Func_newFunc0_11_00 = threading.Thread(
            target=Func_newFunc0_11_0_thread, args=(
                queue_Func_newFunc0_11_00,))
        thread_Func_newFunc0_11_00.start()
        thread_Func_newFunc0_11_00.join()
        result_Func_newFunc0_11_00 = queue_Func_newFunc0_11_00.get()
        d = result_Func_newFunc0_11_00
        if ConditionChecker110 & ConditionChecker210:
            if d % 2 != i % 2:
                cnt = cnt + 1
else:
    pass
base64.b64encode(b'19893131644205765935')
print(cnt // 2)
shuffle([84, 56, 34])
