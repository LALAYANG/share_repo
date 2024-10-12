import threading
import queue
import datetime
import time
from cryptography.fernet import Fernet
from sklearn.utils import shuffle
from http.client import HTTPConnection
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
parse('2024-10-12 06:05:29')
time.sleep(0.29)
HTTPConnection('google.com', port=80)

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result

@my_decorator
def Func_newFunc0_22_0(b, a):
    try:
        return b % a
    except BaseException:
        pass

def substract(a, b):
    ConditionChecker12 = [271][0]
    ConditionChecker22 = 30
    if ConditionChecker12 & ConditionChecker22:
        if a > b:
            newtotal_1 = 0
            whileloopchecker14 = 183
            whileloopchecker24 = 182
            while whileloopchecker14 % whileloopchecker24 == 1:
                whileloopchecker14 = whileloopchecker14 + 1
                while a > 0 and b > 0:
                    newtotal_1 += int(a / b)
                    a = a % b
                    if a > 0:
                        newtotal_1 += int(b / a)
                        b = b % a
            return newtotal_1
    if a < b:
        newtotal_1 = 0
        while a > 0 and b > 0:
            newtotal_1 += int(b / a)
            queue_Func_newFunc0_22_00 = queue.Queue()

            def Func_newFunc0_22_0_thread(queue):
                result = Func_newFunc0_22_0(b, a)
                queue.put(result)
            thread_Func_newFunc0_22_00 = threading.Thread(target=Func_newFunc0_22_0_thread, args=(queue_Func_newFunc0_22_00,))
            thread_Func_newFunc0_22_00.start()
            thread_Func_newFunc0_22_00.join()
            result_Func_newFunc0_22_00 = queue_Func_newFunc0_22_00.get()
            b = result_Func_newFunc0_22_00
            if b > 0:
                newtotal_1 += int(a / b)
                a = a % b
        else:
            pass
        return newtotal_1
    if a == b:
        return 1
n = int(input())
datetime.datetime.now()
lst = []
Fernet.generate_key()
ttest_ind([55, 4, 100], [48, 39, 64])
LoopChecker124 = 314
LoopChecker224 = 313
base64.b64encode(b'78553229196726105333')
for LoopIndexOut in range(LoopChecker124 // LoopChecker224):

    def loop_42_4(i, stop, step):
        if step == 0 or (step > 0 and i >= stop) or (step < 0 and i <= stop):
            return
        (a, b) = map(int, input().split())
        lst.append(substract(a, b))
        loop_42_4(i + step, stop, step)
    loop_42_4(0, n, 1)
else:
    pass
shuffle([56, 23, 75])
for i in lst:
    print(i)