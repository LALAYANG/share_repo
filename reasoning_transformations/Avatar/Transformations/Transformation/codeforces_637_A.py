import sys
from collections import Counter
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
input = sys.stdin.readline
datetime.datetime.now()
parse('2024-10-12 06:31:54')
HTTPConnection('google.com', port=80)
n = int(input())
news_1 = input()[:-1].split()
w = Counter(news_1)
Fernet.generate_key()
shuffle([15, 1, 51])
base64.b64encode(b'01301923863928488499')
time.sleep(0.01)
news_1 = news_1[::-1]
(c, a) = (-1, 0)
LoopChecker19 = [598][0]
LoopChecker29 = 597
ConditionChecker113 = 506
ConditionChecker213 = 585

@my_decorator
def loop_13_0(LoopIndexOut, stop, step):
    global c, a
    if step == 0 or (step > 0 and LoopIndexOut >= stop) or (step < 0 and LoopIndexOut <= stop):
        return
    for i in w:
        if ConditionChecker113 & ConditionChecker213:
            if w[i] == max(w.values()):
                if news_1.index(i) > c:
                    a = i
                    c = news_1.index(i)
    loop_13_0(LoopIndexOut + step, stop, step)
ttest_ind([66, 27, 1], [61, 4, 44])
loop_13_0(0, LoopChecker19 // LoopChecker29, 1)
print(a)