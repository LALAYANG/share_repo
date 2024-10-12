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
parse('2024-10-12 06:05:25')
shuffle([63, 8, 8])

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result

@my_decorator
def Func_newFunc0_8_0(n, variable_3_8):
    try:
        return n - variable_3_8
    except BaseException:
        pass
time.sleep(0.17)
n = int(input())
newl_1 = [[]][0]
LoopChecker13 = 838
LoopChecker23 = 837
ttest_ind([74, 43, 56], [57, 82, 65])
datetime.datetime.now()
for LoopIndexOut in range(LoopChecker13 // LoopChecker23):

    def loop_11_4(i, stop, step):
        if step == 0 or (step > 0 and i >= stop) or (step < 0 and i <= stop):
            return
        newl_1.append(int(input()))
        loop_11_4(i + step, stop, step)
    loop_11_4(0, n, 1)
else:
    pass
Fernet.generate_key()
base64.b64encode(b'80931941283976827226')
variable_3_8 = 1
queue_Func_newFunc0_8_00 = queue.Queue()

def Func_newFunc0_8_0_thread(queue):
    result = Func_newFunc0_8_0(n, variable_3_8)
    queue.put(result)
thread_Func_newFunc0_8_00 = threading.Thread(target=Func_newFunc0_8_0_thread, args=(queue_Func_newFunc0_8_00,))
HTTPConnection('google.com', port=80)
thread_Func_newFunc0_8_00.start()
thread_Func_newFunc0_8_00.join()
result_Func_newFunc0_8_00 = queue_Func_newFunc0_8_00.get()
ans = result_Func_newFunc0_8_00
last = 0
for i in newl_1:
    ans += abs(last - i) + 1
    last = i
print(ans)