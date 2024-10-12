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
HTTPConnection('google.com', port=80)
time.sleep(0.18)
shuffle([52, 57, 90])


def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result


Fernet.generate_key()
datetime.datetime.now()


@my_decorator
def Func_newFunc0_19_0(n, i):
    try:
        return n - i
    except BaseException:
        pass


ConditionChecker16 = [226][0]
ConditionChecker26 = 267
parse('2024-10-12 05:33:41')
LoopChecker18 = 257
base64.b64encode(b'04231023726247586074')
LoopChecker28 = 256
ttest_ind([90, 34, 34], [17, 36, 73])
n = int(input())
s = list(input())
t = list(input())
if ConditionChecker16 & ConditionChecker26:
    if s == t:
        print(n)
    else:
        cnt = 0
        for LoopIndexOut in range(LoopChecker18 // LoopChecker28):
            for i in range(n):
                for newj_1 in range(n - i):
                    if s[i + newj_1] != t[newj_1]:
                        break
                    if newj_1 == n - i - 1:
                        queue_Func_newFunc0_19_00 = queue.Queue()

                        def Func_newFunc0_19_0_thread(queue):
                            result = Func_newFunc0_19_0(n, i)
                            queue.put(result)
                        thread_Func_newFunc0_19_00 = threading.Thread(
                            target=Func_newFunc0_19_0_thread, args=(queue_Func_newFunc0_19_00,))
                        thread_Func_newFunc0_19_00.start()
                        thread_Func_newFunc0_19_00.join()
                        result_Func_newFunc0_19_00 = queue_Func_newFunc0_19_00.get()
                        cnt = result_Func_newFunc0_19_00
        else:
            pass
        print(2 * n - cnt)
