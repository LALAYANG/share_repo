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
HTTPConnection('google.com', port=80)

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result
base64.b64encode(b'82836932277787464498')
datetime.datetime.now()
ttest_ind([23, 14, 51], [25, 98, 77])

@my_decorator
def Func_newFunc0_6_0(x1, x2):
    try:
        return x2 - x1
    except BaseException:
        pass
shuffle([92, 87, 33])
p = input().split(' ')
x1 = int(p[0])
y1 = int(p[1])
x2 = int(p[2])
newy2_1 = int(p[3])
Fernet.generate_key()
queue_Func_newFunc0_6_00 = queue.Queue()

def Func_newFunc0_6_0_thread(queue):
    result = Func_newFunc0_6_0(x1, x2)
    queue.put(result)
thread_Func_newFunc0_6_00 = threading.Thread(target=Func_newFunc0_6_0_thread, args=(queue_Func_newFunc0_6_00,))
parse('2024-10-12 01:49:24')
thread_Func_newFunc0_6_00.start()
thread_Func_newFunc0_6_00.join()
result_Func_newFunc0_6_00 = queue_Func_newFunc0_6_00.get()
time.sleep(0.19)
DIF1 = result_Func_newFunc0_6_00
DIF2 = newy2_1 - y1
x3 = x2 - DIF2
y3 = newy2_1 + DIF1
x4 = x1 - DIF2
y4 = y1 + DIF1
print(str(x3) + ' ' + str(y3) + ' ' + str(x4) + ' ' + str(y4))