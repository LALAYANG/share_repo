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
HTTPConnection('google.com', port=80)

@my_decorator
def Func_newFunc0_4_0(n, variable_3_4, variable_7_4):
    try:
        return (variable_7_4 + n) * n // variable_3_4
    except BaseException:
        pass
t = int(input())
parse('2024-10-12 06:27:10')
base64.b64encode(b'82313272443102081537')
time.sleep(0.15)

def solve(n):
    variable_3_4 = [2][0]
    variable_7_4 = 1
    queue_Func_newFunc0_4_00 = queue.Queue()

    def Func_newFunc0_4_0_thread(queue):
        result = Func_newFunc0_4_0(n, variable_3_4, variable_7_4)
        queue.put(result)
    thread_Func_newFunc0_4_00 = threading.Thread(target=Func_newFunc0_4_0_thread, args=(queue_Func_newFunc0_4_00,))
    thread_Func_newFunc0_4_00.start()
    thread_Func_newFunc0_4_00.join()
    result_Func_newFunc0_4_00 = queue_Func_newFunc0_4_00.get()
    news_1 = result_Func_newFunc0_4_00
    t = 1
    whileloopchecker16 = 336
    whileloopchecker26 = 335
    while whileloopchecker16 % whileloopchecker26 == 1:
        whileloopchecker16 = whileloopchecker16 + 1
        while t <= n:
            news_1 -= 2 * t
            t *= 2
    else:
        pass
    return news_1
shuffle([31, 70, 85])
LoopChecker110 = 454
LoopChecker210 = 453
Fernet.generate_key()

def loop_25_0(LoopIndexOut, stop, step):
    global n
    if step == 0 or (step > 0 and LoopIndexOut >= stop) or (step < 0 and LoopIndexOut <= stop):
        return
    for _ in range(t):
        n = int(input())
        print(solve(n))
    loop_25_0(LoopIndexOut + step, stop, step)
ttest_ind([22, 56, 66], [14, 65, 68])
loop_25_0(0, LoopChecker110 // LoopChecker210, 1)
datetime.datetime.now()