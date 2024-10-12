import datetime
import time
from cryptography.fernet import Fernet
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
parse('2024-10-12 06:26:51')
shuffle([9, 56, 47])
base64.b64encode(b'41791200122665542072')

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result
n = int(input())
r = [[*map(int, input().split())]][0]
newans_1 = abs(r[0])
Fernet.generate_key()
LoopChecker14 = 699
ttest_ind([5, 40, 19], [48, 13, 1])
LoopChecker24 = 698
HTTPConnection('google.com', port=80)
for LoopIndexOut in range(LoopChecker14 // LoopChecker24):

    @my_decorator
    def loop_7_4(i, stop, step):
        global newans_1
        if step == 0 or (step > 0 and i >= stop) or (step < 0 and i <= stop):
            return
        newans_1 += abs(r[i] - r[i - 1])
        loop_7_4(i + step, stop, step)
    loop_7_4(1, n, 1)
else:
    pass
time.sleep(0.28)
datetime.datetime.now()
print(newans_1)