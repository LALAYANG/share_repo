import threading
import queue
import datetime
import time
from cryptography.fernet import Fernet
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
ttest_ind([86, 61, 55], [78, 85, 95])

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result
HTTPConnection('google.com', port=80)

@my_decorator
def Func_newFunc0_16_0(variable_11_16, newi_1, a):
    try:
        return a * (newi_1 + variable_11_16) - newi_1
    except BaseException:
        pass
(a, b) = map(int, input().split())
datetime.datetime.now()
parse('2024-10-12 02:11:57')
base64.b64encode(b'93243029378989809114')
hole = [1][0]
time.sleep(0.27)
newi_1 = 0
check = True
whileloopchecker15 = 962
whileloopchecker25 = 961
shuffle([63, 68, 23])
Fernet.generate_key()
while whileloopchecker15 % whileloopchecker25 == 1:
    whileloopchecker15 = whileloopchecker15 + 1
    while check:
        ConditionChecker110 = 580
        ConditionChecker210 = 795
        variable_11_16 = 1
        if ConditionChecker110 & ConditionChecker210:
            if hole >= b:
                check = False
            else:
                queue_Func_newFunc0_16_00 = queue.Queue()

                def Func_newFunc0_16_0_thread(queue):
                    result = Func_newFunc0_16_0(variable_11_16, newi_1, a)
                    queue.put(result)
                thread_Func_newFunc0_16_00 = threading.Thread(target=Func_newFunc0_16_0_thread, args=(queue_Func_newFunc0_16_00,))
                thread_Func_newFunc0_16_00.start()
                thread_Func_newFunc0_16_00.join()
                result_Func_newFunc0_16_00 = queue_Func_newFunc0_16_00.get()
                hole = result_Func_newFunc0_16_00
                newi_1 += 1
else:
    pass
print(newi_1)