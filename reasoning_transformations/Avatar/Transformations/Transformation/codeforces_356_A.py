import datetime
import time
from cryptography.fernet import Fernet
from sklearn.utils import shuffle
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
HTTPConnection('google.com', port=80)
Fernet.generate_key()
parse('2024-10-12 06:10:43')
time.sleep(0.24)

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result
shuffle([62, 72, 43])
datetime.datetime.now()
(n, m) = map(int, input().strip().split())
out = [[0 for _ in range(n)]][0]
comp = [i + 2 for i in range(n)]
LoopChecker14 = 98
LoopChecker24 = 97

@my_decorator
def loop_6_0(LoopIndexOut, stop, step):
    global whileloopchecker110, whileloopchecker210, newnext_val_1, t
    if step == 0 or (step > 0 and LoopIndexOut >= stop) or (step < 0 and LoopIndexOut <= stop):
        return
    for _ in range(m):
        (l, r, x) = map(int, input().strip().split())
        t = l
        whileloopchecker110 = 114
        whileloopchecker210 = 113
        while whileloopchecker110 % whileloopchecker210 == 1:
            whileloopchecker110 = whileloopchecker110 + 1
            while t <= r:
                newnext_val_1 = comp[t - 1]
                if out[t - 1] == 0 and t != x:
                    out[t - 1] = x
                comp[t - 1] = r + 1 if t >= x else x
                t = newnext_val_1
        else:
            pass
    loop_6_0(LoopIndexOut + step, stop, step)
ttest_ind([5, 20, 11], [7, 5, 56])
loop_6_0(0, LoopChecker14 // LoopChecker24, 1)
base64.b64encode(b'82191468756796995854')
print(*out)