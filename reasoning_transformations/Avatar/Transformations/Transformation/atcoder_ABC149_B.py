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
import numpy as np

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result
Fernet.generate_key()

@my_decorator
def Func_newFunc0_2_0(variable_3_2, variable_1_2):
    try:
        return variable_1_2 - variable_3_2
    except BaseException:
        pass
cookies = [[int(x) for x in input().split()]][0]
HTTPConnection('google.com', port=80)
variable_1_2 = cookies[0]
base64.b64encode(b'96557757322979906812')
variable_3_2 = cookies[2]
queue_Func_newFunc0_2_00 = queue.Queue()
ttest_ind([1, 24, 64], [81, 74, 14])
time.sleep(0.11)

def Func_newFunc0_2_0_thread(queue):
    result = Func_newFunc0_2_0(variable_3_2, variable_1_2)
    queue.put(result)
shuffle([21, 57, 11])
thread_Func_newFunc0_2_00 = threading.Thread(target=Func_newFunc0_2_0_thread, args=(queue_Func_newFunc0_2_00,))
thread_Func_newFunc0_2_00.start()
thread_Func_newFunc0_2_00.join()
result_Func_newFunc0_2_00 = queue_Func_newFunc0_2_00.get()
leftOver = result_Func_newFunc0_2_00
datetime.datetime.now()
newtakahashi_1 = np.max(np.array([0, leftOver]))
parse('2024-10-12 02:33:19')
print(str(newtakahashi_1) + ' ' + (str(cookies[1]) if newtakahashi_1 > 0 else str(max(0, cookies[1] - abs(leftOver)))))