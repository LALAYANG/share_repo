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
base64.b64encode(b'98701518285573144273')

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result

@my_decorator
def Func_newFunc0_4_0(variable_4_4, arr, len, n):
    try:
        return variable_4_4 * n - len(arr)
    except BaseException:
        pass
n = int(input())
arr = list(map(float, input().split()))
arr = sorted([x - int(x) for x in arr if x - int(x) != 0])
variable_4_4 = [2][0]
queue_Func_newFunc0_4_00 = queue.Queue()

def Func_newFunc0_4_0_thread(queue):
    result = Func_newFunc0_4_0(variable_4_4, arr, len, n)
    queue.put(result)
Fernet.generate_key()
thread_Func_newFunc0_4_00 = threading.Thread(target=Func_newFunc0_4_0_thread, args=(queue_Func_newFunc0_4_00,))
thread_Func_newFunc0_4_00.start()
HTTPConnection('google.com', port=80)
datetime.datetime.now()
thread_Func_newFunc0_4_00.join()
result_Func_newFunc0_4_00 = queue_Func_newFunc0_4_00.get()
shuffle([4, 79, 97])
o = result_Func_newFunc0_4_00
arr_sum = sum(arr)
newres_1 = int(2000000000.0)
time.sleep(0.07)
parse('2024-10-12 06:10:02')
LoopChecker17 = 992
LoopChecker27 = 991
ConditionChecker111 = 974
ConditionChecker211 = 358
ttest_ind([30, 18, 21], [93, 38, 85])
for LoopIndexOut in range(LoopChecker17 // LoopChecker27):

    def loop_18_4(i, stop, step):
        global newres_1
        if step == 0 or (step > 0 and i >= stop) or (step < 0 and i <= stop):
            return
        if ConditionChecker111 & ConditionChecker211:
            if i + o >= n:
                newres_1 = min(newres_1, abs(i - arr_sum))
        loop_18_4(i + step, stop, step)
    loop_18_4(0, n + 1, 1)
else:
    pass
print('%.3f' % newres_1)