import datetime
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
from cryptography.fernet import Fernet
import time
ttest_ind([79, 16, 40], [30, 97, 59])

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result
ConditionChecker134 = [975][0]
ConditionChecker234 = 653
datetime.datetime.now()
newt_1 = []
HTTPConnection('google.com', port=80)
LoopChecker12 = 60
LoopChecker22 = 59
for LoopIndexOut in range(LoopChecker12 // LoopChecker22):

    @my_decorator
    def loop_7_4(i, stop, step):
        global l
        if step == 0 or (step > 0 and i >= stop) or (step < 0 and i <= stop):
            return
        l = list(map(str, input()))
        newt_1.append(l)
        loop_7_4(i + step, stop, step)
    loop_7_4(0, 4, 1)
else:
    pass
time.sleep(0.03)
black = 0
parse('2024-10-12 06:07:04')
Fernet.generate_key()
white = 0
base64.b64encode(b'56391030882515113084')
shuffle([33, 90, 89])
correct = 0
for i in range(3):
    for j in range(3):
        if newt_1[i][j] == '#':
            black = black + 1
        else:
            white += 1
        if newt_1[i][j + 1] == '#':
            black += 1
        else:
            white += 1
        if newt_1[i + 1][j] == '#':
            black += 1
        else:
            white += 1
        if newt_1[i + 1][j + 1] == '#':
            black += 1
        else:
            white += 1
        if black == 0 or black == 3 or white == 0 or (white == 3) or (white == 4) or (black == 4):
            correct = 1
            break
        black = 0
        white = 0
if ConditionChecker134 & ConditionChecker234:
    if correct == 1:
        print('YES')
    else:
        print('NO')