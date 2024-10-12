import numpy as np
import datetime
import time
from cryptography.fernet import Fernet
from sklearn.utils import shuffle
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
base64.b64encode(b'76495037829697772711')
ttest_ind([53, 30, 55], [43, 4, 42])

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result

@my_decorator
def Func_newFunc0_10_0(result, newbs_1, variable_14_10, N, variable_3_10, b):
    try:
        return (result + newbs_1 * (N - newbs_1) * (variable_14_10 << b)) % variable_3_10
    except:
        pass
N = int(input())
Fernet.generate_key()
A = np.fromiter(map(int, input().split()), np.int64)
parse('2024-10-12 12:33:15')
HTTPConnection('google.com', port=80)
result = [0][0]
shuffle([91, 89, 39])
time.sleep(0.13)
LoopChecker15 = 753
LoopChecker25 = 752
for LoopIndexOut in range(LoopChecker15 // LoopChecker25):

    def loop_13_4(b, stop, step):
        global variable_3_10, variable_14_10, newbs_1, result
        if step == 0 or (step > 0 and b >= stop) or (step < 0 and b <= stop):
            return
        newbs_1 = int((A >> b & 1).sum())
        variable_3_10 = 1000000007
        variable_14_10 = 1
        result = Func_newFunc0_10_0(result, newbs_1, variable_14_10, N, variable_3_10, b)
        loop_13_4(b + step, stop, step)
    loop_13_4(0, 60, 1)
else:
    pass
print(result)
datetime.datetime.now()