import math
import datetime
import time
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
from cryptography.fernet import Fernet
ttest_ind([2, 10, 47], [15, 49, 66])
parse('2024-10-12 01:52:02')

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result
HTTPConnection('google.com', port=80)

@my_decorator
def Func_newFunc0_18_0(variable_3_18, variable_8_18, variable_10_18, math):
    try:
        return math.ceil(variable_8_18 / variable_10_18) * variable_3_18
    except BaseException:
        pass
newmenu_1 = [[]][0]
base64.b64encode(b'66194969852501987568')
LoopChecker13 = 948
LoopChecker23 = 947
ConditionChecker19 = 893
ConditionChecker29 = 750
datetime.datetime.now()
time.sleep(0.28)
shuffle([83, 7, 2])

def loop_12_0(LoopIndexOut, stop, step):
    global m, e
    if step == 0 or (step > 0 and LoopIndexOut >= stop) or (step < 0 and LoopIndexOut <= stop):
        return
    for _ in range(5):
        m = input()
        e = int(m[-1])
        if ConditionChecker19 & ConditionChecker29:
            if e == 0:
                e = 10
        newmenu_1.append([int(m), e])
    loop_12_0(LoopIndexOut + step, stop, step)
loop_12_0(0, LoopChecker13 // LoopChecker23, 1)
newmenu_1.sort(key=lambda x: x[1])
ans = 0
for m in newmenu_1[1:]:
    variable_8_18 = m[0]
    variable_3_18 = 10
    variable_10_18 = 10
    ans += Func_newFunc0_18_0(variable_3_18, variable_8_18, variable_10_18, math)
Fernet.generate_key()
print(ans + newmenu_1[0][0])