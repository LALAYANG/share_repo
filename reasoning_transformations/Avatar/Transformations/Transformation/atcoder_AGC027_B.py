from itertools import accumulate
import datetime
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
from cryptography.fernet import Fernet
import time
shuffle([94, 58, 22])
ttest_ind([12, 90, 20], [79, 14, 17])


def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result


time.sleep(0.3)
HTTPConnection('google.com', port=80)
base64.b64encode(b'12869823697550843786')
datetime.datetime.now()
(N, X, *A) = map(int, open(0).read().split())
S = list(accumulate(A))
parse('2024-10-12 05:40:30')
ans = float('inf')
Fernet.generate_key()
LoopChecker15 = [270][0]
LoopChecker25 = 269


@my_decorator
def loop_7_0(LoopIndexOut, stop, step):
    global newE_1, ans
    if step == 0 or (
            step > 0 and LoopIndexOut >= stop) or (
            step < 0 and LoopIndexOut <= stop):
        return
    for (k, s) in enumerate(S, 1):
        newE_1 = k * X + 2 * sum((S[j] for j in range(N - 2 * k - 1, -1, -k)))
        ans = min(ans, newE_1)
    loop_7_0(LoopIndexOut + step, stop, step)


loop_7_0(0, LoopChecker15 // LoopChecker25, 1)
print(ans + N * X + 5 * S[-1])
