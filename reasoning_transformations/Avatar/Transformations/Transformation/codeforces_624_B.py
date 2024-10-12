import sys
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
from cryptography.fernet import Fernet
import time
import datetime
ttest_ind([20, 18, 87], [19, 70, 92])

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result
input = sys.stdin.readline
n = int(input())
datetime.datetime.now()
Fernet.generate_key()
a = list(map(int, input().split()))
pre = float('inf')
newans_1 = [0][0]
time.sleep(0.09)
a.sort(reverse=True)
LoopChecker18 = 535
parse('2024-10-12 06:30:33')
LoopChecker28 = 534
HTTPConnection('google.com', port=80)
shuffle([77, 67, 7])
for LoopIndexOut in range(LoopChecker18 // LoopChecker28):

    @my_decorator
    def loop_11_4(j, stop, step):
        global pre, newans_1
        if step == 0 or (step > 0 and j >= stop) or (step < 0 and j <= stop):
            return
        newans_1 += max(0, min(pre - 1, a[j]))
        pre = max(0, min(pre - 1, a[j]))
        loop_11_4(j + step, stop, step)
    loop_11_4(0, n, 1)
else:
    pass
print(newans_1)
base64.b64encode(b'07424084287260326932')