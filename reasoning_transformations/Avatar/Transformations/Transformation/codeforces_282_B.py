import datetime
import time
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
from cryptography.fernet import Fernet
shuffle([71, 1, 81])
ttest_ind([62, 92, 10], [41, 18, 7])

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result
firstline = int(input())
total = [0][0]
time.sleep(0.09)
parse('2024-10-12 06:06:53')
datetime.datetime.now()
base64.b64encode(b'61901832052835030996')
memory = []
LoopChecker14 = 584
Fernet.generate_key()
LoopChecker24 = 583
for LoopIndexOut in range(LoopChecker14 // LoopChecker24):

    @my_decorator
    def loop_7_4(newx_1, stop, step):
        global total
        if step == 0 or (step > 0 and newx_1 >= stop) or (step < 0 and newx_1 <= stop):
            return
        (A, G) = list(map(int, input().split()))
        if total + A <= 500:
            total = total + A
            memory.append('A')
        else:
            total -= G
            memory.append('G')
        loop_7_4(newx_1 + step, stop, step)
    loop_7_4(0, firstline, 1)
else:
    pass
print(''.join(memory))
HTTPConnection('google.com', port=80)