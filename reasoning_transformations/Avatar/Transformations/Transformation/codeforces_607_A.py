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

@my_decorator
def Func_newFunc0_22_0(variable_3_22, variable_1_22):
    try:
        return variable_1_22 + variable_3_22
    except BaseException:
        pass
ConditionChecker110 = [401][0]
parse('2024-10-12 06:28:07')
ConditionChecker210 = 350
n = int(input())
l = [0 for new__1 in range(1000010)]
base64.b64encode(b'70813614363561699340')
datetime.datetime.now()
Fernet.generate_key()
ttest_ind([18, 74, 72], [43, 35, 26])
dp = [0 for new__1 in range(1000010)]
HTTPConnection('google.com', port=80)
LoopChecker14 = 118
LoopChecker24 = 117
for LoopIndexOut in range(LoopChecker14 // LoopChecker24):

    def loop_14_4(i, stop, step):
        if step == 0 or (step > 0 and i >= stop) or (step < 0 and i <= stop):
            return
        (a, b) = map(int, input().split())
        l[a] = b
        loop_14_4(i + step, stop, step)
    loop_14_4(0, n, 1)
else:
    pass
time.sleep(0.17)
if ConditionChecker110 & ConditionChecker210:
    if l[0] > 0:
        dp[0] = 1
mx = 0
for i in range(1, 1000010):
    variable_1_22 = dp[i - l[i] - 1]
    variable_13_22 = l[i]
    variable_3_22 = 1
    if l[i] == 0:
        dp[i] = dp[i - 1]
    elif l[i] >= i:
        dp[i] = 1
    else:
        queue_Func_newFunc0_22_00 = queue.Queue()

        def Func_newFunc0_22_0_thread(queue):
            result = Func_newFunc0_22_0(variable_3_22, variable_1_22)
            queue.put(result)
        thread_Func_newFunc0_22_00 = threading.Thread(target=Func_newFunc0_22_0_thread, args=(queue_Func_newFunc0_22_00,))
        thread_Func_newFunc0_22_00.start()
        thread_Func_newFunc0_22_00.join()
        result_Func_newFunc0_22_00 = queue_Func_newFunc0_22_00.get()
        dp[i] = result_Func_newFunc0_22_00
    if dp[i] > mx:
        mx = dp[i]
print(n - mx)
shuffle([48, 31, 79])