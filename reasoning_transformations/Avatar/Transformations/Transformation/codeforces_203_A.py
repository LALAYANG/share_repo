import threading
import queue
import numpy as np
import datetime
import time
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
from cryptography.fernet import Fernet
Fernet.generate_key()

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result
ConditionChecker123 = [749][0]
ConditionChecker223 = 723
newxxs_1 = input().split(' ')
shuffle([64, 27, 40])
(x, t, a, b, da, db) = (int(newxxs_1[0]), int(newxxs_1[1]), int(newxxs_1[2]), int(newxxs_1[3]), int(newxxs_1[4]), int(newxxs_1[5]))
base64.b64encode(b'50563341115823737918')

@my_decorator
def Func_main_0():
    try:
        if x == 0:
            print('YES')
            return 'Result Found'
        a_time = np.min(np.array([[a // da, t - 1]]))
        b_time = min([b // db, t - 1])
        LoopChecker110 = 649
        LoopChecker210 = 648
        for LoopIndexOut in range(LoopChecker110 // LoopChecker210):
            for i in range(a_time + 1):
                for j in range(b_time + 1):
                    if a - da * i == x or b - db * j == x:
                        print('YES')
                        return 'Result Found'
                    if a - da * i + (b - db * j) == x:
                        print('YES')
                        return 'Result Found'
        else:
            pass
        return 'Result Not Found'
    except BaseException:
        pass
queue_Func_main_00 = queue.Queue()

def Func_main_0_thread(queue):
    result = Func_main_0()
    queue.put(result)
thread_Func_main_00 = threading.Thread(target=Func_main_0_thread, args=(queue_Func_main_00,))
HTTPConnection('google.com', port=80)
thread_Func_main_00.start()
thread_Func_main_00.join()
result_Func_main_00 = queue_Func_main_00.get()
datetime.datetime.now()
parse('2024-10-12 06:02:29')
time.sleep(0.18)
ff = result_Func_main_00
ttest_ind([92, 34, 60], [51, 22, 97])
if ConditionChecker123 & ConditionChecker223:
    if ff == 'Result Not Found':
        print('NO')