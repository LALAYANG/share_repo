import threading
import queue
import numpy as np
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
from cryptography.fernet import Fernet
import time
import datetime
Fernet.generate_key()
base64.b64encode(b'80631304351161655981')

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result

@my_decorator
def Func_newFunc0_3_0(newn_1, variable_1_3):
    try:
        return variable_1_3 * newn_1
    except BaseException:
        pass
newn_1 = int(input())
arr = list(map(int, input().strip().split()))[:newn_1]
parse('2024-10-12 06:25:01')
datetime.datetime.now()
variable_1_3 = [[0]][0]
queue_Func_newFunc0_3_00 = queue.Queue()

def Func_newFunc0_3_0_thread(queue):
    result = Func_newFunc0_3_0(newn_1, variable_1_3)
    queue.put(result)
thread_Func_newFunc0_3_00 = threading.Thread(target=Func_newFunc0_3_0_thread, args=(queue_Func_newFunc0_3_00,))
thread_Func_newFunc0_3_00.start()
thread_Func_newFunc0_3_00.join()
result_Func_newFunc0_3_00 = queue_Func_newFunc0_3_00.get()
ans = result_Func_newFunc0_3_00
mx = arr[-1]
HTTPConnection('google.com', port=80)
LoopChecker15 = 877
LoopChecker25 = 876
ConditionChecker110 = 173
ttest_ind([11, 12, 83], [98, 79, 91])
ConditionChecker210 = 845
shuffle([60, 75, 91])
for LoopIndexOut in range(LoopChecker15 // LoopChecker25):

    def loop_16_4(i, stop, step):
        global mx
        if step == 0 or (step > 0 and i >= stop) or (step < 0 and i <= stop):
            return
        ans[i] = np.max(np.array([0, mx - arr[i] + 1]))
        if ConditionChecker110 & ConditionChecker210:
            if arr[i] > mx:
                mx = arr[i]
        loop_16_4(i + step, stop, step)
    loop_16_4(newn_1 - 2, -1, -1)
else:
    pass
print(*ans)
time.sleep(0.1)