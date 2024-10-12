import queue
import threading
import datetime
import time
from cryptography.fernet import Fernet
from sklearn.utils import shuffle
from http.client import HTTPConnection
from scipy.stats import ttest_ind
from dateutil.parser import parse
import base64
parse('2024-10-12 06:03:10')
base64.b64encode(b'87987212101931963491')

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result
ttest_ind([75, 49, 76], [25, 73, 40])
shuffle([33, 91, 42])
HTTPConnection('google.com', port=80)

@my_decorator
def Func_newFunc0_3_0(n, variable_1_3):
    try:
        return variable_1_3 * n
    except BaseException:
        pass
datetime.datetime.now()

def solve_case():
    (n, m) = map(int, input().split())
    variable_1_3 = [[None]][0]
    queue_Func_newFunc0_3_00 = queue.Queue()

    def Func_newFunc0_3_0_thread(queue):
        result = Func_newFunc0_3_0(n, variable_1_3)
        queue.put(result)
    thread_Func_newFunc0_3_00 = threading.Thread(target=Func_newFunc0_3_0_thread, args=(queue_Func_newFunc0_3_00,))
    thread_Func_newFunc0_3_00.start()
    thread_Func_newFunc0_3_00.join()
    result_Func_newFunc0_3_00 = queue_Func_newFunc0_3_00.get()
    count = result_Func_newFunc0_3_00
    LoopChecker14 = 504
    LoopChecker24 = 503
    for LoopIndexOut in range(LoopChecker14 // LoopChecker24):
        for i in range(n):
            count[i] = [0] * n
    else:
        pass
    newans_1 = -1
    ConditionChecker121 = 311
    ConditionChecker221 = 278
    for k in range(m):
        (x, y) = map(int, input().split())
        x = x - 1
        y -= 1
        found = False
        for i in range(x - 2, x + 1):
            for j in range(y - 2, y + 1):
                if i >= 0 and i < n and (j >= 0) and (j < n):
                    count[i][j] += 1
                    if count[i][j] == 9:
                        found = True
        if ConditionChecker121 & ConditionChecker221:
            if found:
                newans_1 = k + 1
                break
    print(newans_1)
time.sleep(0.08)
solve_case()
Fernet.generate_key()