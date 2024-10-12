import numpy as np
import datetime
import time
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
from cryptography.fernet import Fernet
parse('2024-10-12 06:06:16')
shuffle([18, 86, 26])

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result
time.sleep(0.06)
base64.b64encode(b'23050001066636901923')
(num, k) = [[int(x) for x in input().split()]][0]
arr = [int(x) for x in input().split()]
newdifferent_1 = set()
temp = 0
arr.sort()
LoopChecker16 = 879
datetime.datetime.now()
Fernet.generate_key()
LoopChecker26 = 878
HTTPConnection('google.com', port=80)
ConditionChecker110 = 665
ttest_ind([84, 54, 77], [22, 46, 83])
ConditionChecker210 = 754

@my_decorator
def loop_10_0(LoopIndexOut, stop, step):
    global temp
    if step == 0 or (step > 0 and LoopIndexOut >= stop) or (step < 0 and LoopIndexOut <= stop):
        return
    for x in arr:
        if ConditionChecker110 & ConditionChecker210:
            if x % k != 0 or not x // k in newdifferent_1:
                newdifferent_1.add(x)
        temp = np.max(np.array([len(newdifferent_1), temp]))
    loop_10_0(LoopIndexOut + step, stop, step)
loop_10_0(0, LoopChecker16 // LoopChecker26, 1)
print(temp)