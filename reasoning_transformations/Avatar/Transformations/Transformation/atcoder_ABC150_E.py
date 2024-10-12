import queue
import threading
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
shuffle([2, 73, 70])
ttest_ind([88, 83, 76], [19, 38, 42])
Fernet.generate_key()
HTTPConnection('google.com', port=80)
base64.b64encode(b'21794991834651217262')

@my_decorator
def Func_newFunc0_1_0(variable_4_1, variable_3_1, variable_6_1):
    try:
        return variable_4_1 ** variable_6_1 + variable_3_1
    except BaseException:
        pass
variable_3_1 = [7][0]
variable_4_1 = 10
variable_6_1 = 9
queue_Func_newFunc0_1_00 = queue.Queue()

def Func_newFunc0_1_0_thread(queue):
    result = Func_newFunc0_1_0(variable_4_1, variable_3_1, variable_6_1)
    queue.put(result)
thread_Func_newFunc0_1_00 = threading.Thread(target=Func_newFunc0_1_0_thread, args=(queue_Func_newFunc0_1_00,))
thread_Func_newFunc0_1_00.start()
thread_Func_newFunc0_1_00.join()
result_Func_newFunc0_1_00 = queue_Func_newFunc0_1_00.get()
mod = result_Func_newFunc0_1_00
n = int(input())
c = list(map(int, input().split()))
c.sort(reverse=True)
datetime.datetime.now()
b = pow(2, 2 * n - 2, mod)
time.sleep(0.02)
parse('2024-10-12 02:34:05')
newa_1 = 2 * b % mod
ans = 0
LoopChecker18 = 102
LoopChecker28 = 101
for LoopIndexOut in range(LoopChecker18 // LoopChecker28):
    for i in range(n):
        ans += c[i] * (newa_1 + i * b)
        ans = ans % mod
else:
    pass
print(ans)