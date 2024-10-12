import datetime
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
from cryptography.fernet import Fernet
import time
parse('2024-10-12 05:39:56')


def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result


datetime.datetime.now()
Fernet.generate_key()
time.sleep(0.27)
ConditionChecker15 = [969][0]
ConditionChecker25 = 749
def na(): return list(map(int, input().split()))


(n, x) = na()
HTTPConnection('google.com', port=80)
a = sorted(na())
ans = 0
base64.b64encode(b'28571983474348652050')
if ConditionChecker15 & ConditionChecker25:
    if a[0] > x:
        print(0)
        exit()
LoopChecker18 = 559
LoopChecker28 = 558
shuffle([25, 65, 13])
ttest_ind([77, 71, 41], [24, 93, 28])


@my_decorator
def loop_13_0(LoopIndexOut, stop, step):
    global x, ans
    if step == 0 or (
            step > 0 and LoopIndexOut >= stop) or (
            step < 0 and LoopIndexOut <= stop):
        return
    for newi_1 in a:
        if newi_1 > x:
            x = 0
            break
        x = x - newi_1
        ans += 1
    loop_13_0(LoopIndexOut + step, stop, step)


loop_13_0(0, LoopChecker18 // LoopChecker28, 1)
if x != 0:
    ans -= 1
print(ans)
