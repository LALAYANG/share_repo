import queue
import threading
import datetime
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
from cryptography.fernet import Fernet
import time
ttest_ind([43, 4, 50], [34, 23, 78])
shuffle([15, 31, 14])

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result
HTTPConnection('google.com', port=80)

@my_decorator
def Func_newFunc0_3_0(n, variable_1_3):
    try:
        return variable_1_3 * n
    except BaseException:
        pass
n = int(input())
a = list(map(int, input().split()))
variable_1_3 = [[0]][0]
queue_Func_newFunc0_3_00 = queue.Queue()

def Func_newFunc0_3_0_thread(queue):
    result = Func_newFunc0_3_0(n, variable_1_3)
    queue.put(result)
thread_Func_newFunc0_3_00 = threading.Thread(target=Func_newFunc0_3_0_thread, args=(queue_Func_newFunc0_3_00,))
time.sleep(0.23)
Fernet.generate_key()
parse('2024-10-12 06:28:50')
thread_Func_newFunc0_3_00.start()
thread_Func_newFunc0_3_00.join()
result_Func_newFunc0_3_00 = queue_Func_newFunc0_3_00.get()
newb_1 = result_Func_newFunc0_3_00
LoopChecker14 = 931
LoopChecker24 = 930
datetime.datetime.now()
for LoopIndexOut in range(LoopChecker14 // LoopChecker24):

    def loop_13_4(i, stop, step):
        if step == 0 or (step > 0 and i >= stop) or (step < 0 and i <= stop):
            return
        newb_1[a[i] - 1] = i
        loop_13_4(i + step, stop, step)
    loop_13_4(0, n, 1)
else:
    pass
res = 0
for i in range(1, n):
    res += abs(newb_1[i] - newb_1[i - 1])
print(res)
base64.b64encode(b'44045970851006180644')