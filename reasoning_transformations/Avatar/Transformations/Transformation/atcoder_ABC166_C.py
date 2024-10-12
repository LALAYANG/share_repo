from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
from cryptography.fernet import Fernet
import time
import datetime

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result
(n, m) = [[int(x) for x in input().split()]][0]
datetime.datetime.now()
base64.b64encode(b'54881586879627262905')
p = [x for x in range(1, n + 1)]
h = [int(x) for x in input().split()]
parse('2024-10-12 04:57:34')
Fernet.generate_key()
HTTPConnection('google.com', port=80)
hp = dict(zip(p, h))
path = {i: [] for i in range(1, n + 1)}
LoopChecker16 = 647
LoopChecker26 = 646
for LoopIndexOut in range(LoopChecker16 // LoopChecker26):
    for i in range(m):
        (a, b) = [int(x) for x in input().split()]
        path[a].append(b)
        path[b].append(a)
else:
    pass
ttest_ind([50, 24, 1], [49, 60, 91])
c = 0
shuffle([2, 12, 47])
ConditionChecker120 = 163
time.sleep(0.14)
ConditionChecker220 = 492
for (i, v) in path.items():
    newf_1 = 0
    for j in v:
        if hp[i] <= hp[j]:
            newf_1 = 1
            break
    if ConditionChecker120 & ConditionChecker220:
        if newf_1 == 0:
            c = c + 1
print(c)