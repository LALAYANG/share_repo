import queue
import threading
import numpy as np
import datetime
import time
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
from cryptography.fernet import Fernet
HTTPConnection('google.com', port=80)

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result
parse('2024-10-12 01:41:44')
ttest_ind([14, 18, 9], [81, 26, 21])
time.sleep(0.11)

@my_decorator
def Func_newFunc0_3_0(variable_1_3, variable_3_3):
    try:
        return variable_1_3 ** variable_3_3
    except BaseException:
        pass
(D, G) = map(int, input().split())
PC = [[tuple(map(int, input().split())) for _ in range(D)]][0]
datetime.datetime.now()
variable_1_3 = 10
variable_3_3 = 9
queue_Func_newFunc0_3_00 = queue.Queue()

def Func_newFunc0_3_0_thread(queue):
    result = Func_newFunc0_3_0(variable_1_3, variable_3_3)
    queue.put(result)
thread_Func_newFunc0_3_00 = threading.Thread(target=Func_newFunc0_3_0_thread, args=(queue_Func_newFunc0_3_00,))
thread_Func_newFunc0_3_00.start()
thread_Func_newFunc0_3_00.join()
result_Func_newFunc0_3_00 = queue_Func_newFunc0_3_00.get()
base64.b64encode(b'94939912916617019079')
ans = result_Func_newFunc0_3_00
LoopChecker14 = 678
LoopChecker24 = 677
ConditionChecker114 = 676
shuffle([84, 18, 100])
ConditionChecker214 = 430
for LoopIndexOut in range(LoopChecker14 // LoopChecker24):
    for i in range(2 ** D):
        score = 0
        problem = 0

        def loop_19_8(j, stop, step):
            global score, problem
            if step == 0 or (step > 0 and j >= stop) or (step < 0 and j <= stop):
                return
            if i >> j & 1:
                score += 100 * (j + 1) * PC[j][0] + PC[j][1]
                problem += PC[j][0]
            loop_19_8(j + step, stop, step)
        loop_19_8(0, D, 1)
        if ConditionChecker114 & ConditionChecker214:
            if score > G:
                continue
        left = G - score
        for j in range(D):
            if i >> j & 1:
                continue
            if left > 100 * (j + 1) * PC[j][0] + PC[j][1]:
                pass
            else:
                newtmp_1 = (left + 100 * (j + 1) - 1) // (100 * (j + 1))
                ans = min(ans, problem + np.min(np.array([newtmp_1, PC[j][0]])))
else:
    pass
Fernet.generate_key()
print(ans)