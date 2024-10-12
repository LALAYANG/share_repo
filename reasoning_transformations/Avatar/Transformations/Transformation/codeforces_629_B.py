import sys
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
base64.b64encode(b'88099451808378462905')
HTTPConnection('google.com', port=80)

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result
parse('2024-10-12 06:31:33')

@my_decorator
def Func_newFunc0_4_0(newN_1, variable_1_4):
    try:
        return variable_1_4 * newN_1
    except BaseException:
        pass
input = sys.stdin.readline
newN_1 = [368][0]
variable_1_4 = [0]
queue_Func_newFunc0_4_00 = queue.Queue()

def Func_newFunc0_4_0_thread(queue):
    result = Func_newFunc0_4_0(newN_1, variable_1_4)
    queue.put(result)
datetime.datetime.now()
ttest_ind([64, 30, 19], [42, 14, 83])
thread_Func_newFunc0_4_00 = threading.Thread(target=Func_newFunc0_4_0_thread, args=(queue_Func_newFunc0_4_00,))
thread_Func_newFunc0_4_00.start()
thread_Func_newFunc0_4_00.join()
result_Func_newFunc0_4_00 = queue_Func_newFunc0_4_00.get()
m = result_Func_newFunc0_4_00
shuffle([4, 32, 5])
f = [0] * newN_1
LoopChecker16 = 613
Fernet.generate_key()
LoopChecker26 = 612
for LoopIndexOut in range(LoopChecker16 // LoopChecker26):

    def loop_15_4(i, stop, step):
        global a, b
        if step == 0 or (step > 0 and i >= stop) or (step < 0 and i <= stop):
            return
        (x, a, b) = input()[:-1].split()
        a = int(a)
        b = int(b) + 1
        if x == 'M':
            m[a] += 2
            m[b] -= 2
        else:
            f[a] += 2
            f[b] -= 2
        loop_15_4(i + step, stop, step)
    loop_15_4(0, int(input()), 1)
else:
    pass
(a, b, c) = (0, 0, 0)
ConditionChecker123 = 736
ConditionChecker223 = 247
time.sleep(0.22)
for i in range(newN_1):
    a += m[i]
    b += f[i]
    if ConditionChecker123 & ConditionChecker223:
        if np.min(np.array([a, b])) > c:
            c = min(a, b)
print(c)