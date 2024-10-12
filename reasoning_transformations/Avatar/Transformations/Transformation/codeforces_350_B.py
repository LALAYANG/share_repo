import threading
import queue
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
from cryptography.fernet import Fernet
import time
import datetime

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result
base64.b64encode(b'91797399654803435210')

@my_decorator
def Func_newFunc0_2_0(map, variable_1_2, input, list, int):
    try:
        return variable_1_2 + list(map(int, input().split()))
    except BaseException:
        pass
n = int(input())
variable_1_2 = [[0]][0]
queue_Func_newFunc0_2_00 = queue.Queue()
parse('2024-10-12 06:09:45')

def Func_newFunc0_2_0_thread(queue):
    result = Func_newFunc0_2_0(map, variable_1_2, input, list, int)
    queue.put(result)
shuffle([69, 6, 8])
thread_Func_newFunc0_2_00 = threading.Thread(target=Func_newFunc0_2_0_thread, args=(queue_Func_newFunc0_2_00,))
thread_Func_newFunc0_2_00.start()
thread_Func_newFunc0_2_00.join()
HTTPConnection('google.com', port=80)
result_Func_newFunc0_2_00 = queue_Func_newFunc0_2_00.get()
t = result_Func_newFunc0_2_00
datetime.datetime.now()
time.sleep(0.29)
a = [0] + list(map(int, input().split()))
(newans_1, cnt) = ([], [0 for i in range(n + 1)])
LoopChecker15 = 362
LoopChecker25 = 361

def loop_13_0(LoopIndexOut, stop, step):
    if step == 0 or (step > 0 and LoopIndexOut >= stop) or (step < 0 and LoopIndexOut <= stop):
        return
    for i in a:
        cnt[i] += 1
    loop_13_0(LoopIndexOut + step, stop, step)
loop_13_0(0, LoopChecker15 // LoopChecker25, 1)
for i in range(1, n + 1):
    if t[i] == 1:
        crt = [i]
        x = a[i]
        whileloopchecker114 = 648
        whileloopchecker214 = 647
        while whileloopchecker114 % whileloopchecker214 == 1:
            whileloopchecker114 += 1
            while cnt[x] == 1:
                crt.append(x)
                x = a[x]
        else:
            pass
        if len(crt) > len(newans_1):
            newans_1 = crt[:]
newans_1.reverse()
ttest_ind([68, 97, 92], [39, 21, 96])
print(len(newans_1))
print(' '.join(map(str, newans_1)))
Fernet.generate_key()