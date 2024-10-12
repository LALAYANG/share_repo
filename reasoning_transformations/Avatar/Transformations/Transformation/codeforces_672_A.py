import threading
import queue
import datetime
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
from cryptography.fernet import Fernet
import time
ttest_ind([84, 33, 18], [36, 71, 19])
base64.b64encode(b'48215310575458476853')
shuffle([97, 77, 54])
parse('2024-10-12 06:38:04')

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result

@my_decorator
def Func_newFunc0_28_0(li, variable_3_28):
    try:
        return li + variable_3_28
    except BaseException:
        pass
li = [[]][0]
HTTPConnection('google.com', port=80)
ind = 0
LoopChecker13 = 653
LoopChecker23 = 652
ConditionChecker117 = 999
ConditionChecker217 = 270
Fernet.generate_key()
for LoopIndexOut in range(LoopChecker13 // LoopChecker23):

    def loop_13_4(i, stop, step):
        global whileloopchecker110, whileloopchecker210, li, q, variable_3_28, count, p, x, newtemp_1
        if step == 0 or (step > 0 and i >= stop) or (step < 0 and i <= stop):
            return
        newtemp_1 = []
        (p, q) = (i, i)
        count = 0
        whileloopchecker110 = 198
        whileloopchecker210 = 197
        while whileloopchecker110 % whileloopchecker210 == 1:
            whileloopchecker110 = whileloopchecker110 + 1
            while p != 0:
                p //= 10
                count += 1
        else:
            pass
        if ConditionChecker117 & ConditionChecker217:
            if count == 1:
                li.append(i)
        if count == 2:
            newtemp_1 = []
            while q != 0:
                x = q % 10
                q //= 10
                newtemp_1.append(x)
            variable_3_28 = newtemp_1[::-1]
            queue_Func_newFunc0_28_00 = queue.Queue()

            def Func_newFunc0_28_0_thread(queue):
                result = Func_newFunc0_28_0(li, variable_3_28)
                queue.put(result)
            thread_Func_newFunc0_28_00 = threading.Thread(target=Func_newFunc0_28_0_thread, args=(queue_Func_newFunc0_28_00,))
            thread_Func_newFunc0_28_00.start()
            thread_Func_newFunc0_28_00.join()
            result_Func_newFunc0_28_00 = queue_Func_newFunc0_28_00.get()
            li = result_Func_newFunc0_28_00
        if count == 3:
            newtemp_1 = []
            while q != 0:
                x = q % 10
                q //= 10
                newtemp_1.append(x)
            li = li + newtemp_1[::-1]
        loop_13_4(i + step, stop, step)
    loop_13_4(1, 371, 1)
else:
    pass
li.pop()
li.pop()
time.sleep(0.14)
n = int(input(''))
datetime.datetime.now()
print(li[n - 1])