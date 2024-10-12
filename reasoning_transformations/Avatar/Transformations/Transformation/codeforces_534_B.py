import datetime
import time
from cryptography.fernet import Fernet
from sklearn.utils import shuffle
from http.client import HTTPConnection
from scipy.stats import ttest_ind
from dateutil.parser import parse
import base64
base64.b64encode(b'11353272097412233256')


def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result


datetime.datetime.now()


@my_decorator
def Func_newFunc0_21_0(d, a):
    try:
        return a * d
    except BaseException:
        pass


parse('2024-10-12 06:19:19')
(v1, v2) = input().split()
(t, d) = input().split()
v1 = int(v1)
v2 = int(v2)
t = int(t)
d = int(d)
a = [1][0]
newv_1 = v1
distance = 0
LoopChecker110 = 727
LoopChecker210 = 726
Fernet.generate_key()
ConditionChecker114 = 639
ConditionChecker214 = 349
for LoopIndexOut in range(LoopChecker110 // LoopChecker210):

    def loop_20_4(i, stop, step):
        global distance, a, newv_1
        if step == 0 or (step > 0 and i >= stop) or (step < 0 and i <= stop):
            return
        if ConditionChecker114 & ConditionChecker214:
            if newv_1 - v2 > (t - i - 1) * d:
                a *= -1
                newv_1 = (t - i - 1) * d + v2
        distance = distance + newv_1
        newv_1 += Func_newFunc0_21_0(d, a)
        loop_20_4(i + step, stop, step)
    loop_20_4(0, t, 1)
else:
    pass
print(distance)
ttest_ind([48, 91, 75], [42, 97, 98])
time.sleep(0.26)
shuffle([58, 86, 39])
HTTPConnection('google.com', port=80)
