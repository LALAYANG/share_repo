import math
import datetime
import time
from cryptography.fernet import Fernet
from sklearn.utils import shuffle
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
HTTPConnection('google.com', port=80)
base64.b64encode(b'94657112547236793018')

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result
Fernet.generate_key()

@my_decorator
def Func_newFunc0_8_0(variable_6_8, variable_4_8, variable_3_8):
    try:
        return (variable_4_8 - variable_6_8) ** variable_3_8
    except BaseException:
        pass
shuffle([27, 12, 99])
(n, d) = map(int, input().split())
datetime.datetime.now()
time.sleep(0.11)
points = [[list(map(int, input().split())) for _ in range(n)]][0]

def dist(x, y):
    tmp = 0.0
    for newi_1 in range(d):
        variable_4_8 = x[newi_1]
        variable_6_8 = y[newi_1]
        variable_3_8 = 2
        tmp += Func_newFunc0_8_0(variable_6_8, variable_4_8, variable_3_8)
    return math.sqrt(tmp)
ttest_ind([68, 51, 28], [77, 100, 2])
count = 0
LoopChecker111 = 877
LoopChecker211 = 876
ConditionChecker116 = 116
ConditionChecker216 = 754
parse('2024-10-12 02:02:48')
for LoopIndexOut in range(LoopChecker111 // LoopChecker211):
    for (newi_1, elm) in enumerate(points):
        for j in range(newi_1 + 1, n):
            if ConditionChecker116 & ConditionChecker216:
                if dist(elm, points[j]).is_integer():
                    count = count + 1
else:
    pass
print(count)