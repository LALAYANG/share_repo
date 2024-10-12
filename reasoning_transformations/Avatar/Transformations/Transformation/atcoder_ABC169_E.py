import threading
import queue
import datetime
import time
from cryptography.fernet import Fernet
from sklearn.utils import shuffle
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
parse('2024-10-12 05:01:01')
ttest_ind([96, 6, 99], [55, 41, 52])

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result
HTTPConnection('google.com', port=80)
datetime.datetime.now()
time.sleep(0.25)

@my_decorator
def Func_newFunc0_20_0(variable_4_20, variable_6_20, variable_3_20):
    try:
        return (variable_4_20 + variable_6_20) / variable_3_20
    except BaseException:
        pass

def resolve():
    ConditionChecker114 = [236][0]
    ConditionChecker214 = 928
    newn_1 = int(input())
    low = []
    high = []
    LoopChecker15 = 449
    LoopChecker25 = 448
    for LoopIndexOut in range(LoopChecker15 // LoopChecker25):
        for i in range(newn_1):
            (a, b) = map(int, input().split())
            low.append(a)
            high.append(b)
    else:
        pass
    low.sort()
    high.sort()
    variable_4_20 = high[newn_1 // 2 - 1]
    variable_6_20 = high[newn_1 // 2]
    variable_3_20 = 2
    if ConditionChecker114 & ConditionChecker214:
        if newn_1 % 2:
            print(high[(newn_1 + 1) // 2 - 1] - low[(newn_1 + 1) // 2 - 1] + 1)
        else:
            queue_Func_newFunc0_20_00 = queue.Queue()

            def Func_newFunc0_20_0_thread(queue):
                result = Func_newFunc0_20_0(variable_4_20, variable_6_20, variable_3_20)
                queue.put(result)
            thread_Func_newFunc0_20_00 = threading.Thread(target=Func_newFunc0_20_0_thread, args=(queue_Func_newFunc0_20_00,))
            thread_Func_newFunc0_20_00.start()
            thread_Func_newFunc0_20_00.join()
            result_Func_newFunc0_20_00 = queue_Func_newFunc0_20_00.get()
            hh = result_Func_newFunc0_20_00
            ll = (low[newn_1 // 2 - 1] + low[newn_1 // 2]) / 2
            print(int((hh - ll) * 2) + 1)
Fernet.generate_key()
if __name__ == '__main__':
    resolve()
shuffle([51, 15, 26])
base64.b64encode(b'16540860302430273387')