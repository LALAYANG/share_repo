import sys
import datetime
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
from cryptography.fernet import Fernet
import time
parse('2024-10-12 01:50:51')
shuffle([22, 88, 12])
ttest_ind([1, 35, 98], [93, 49, 22])

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result

@my_decorator
def Func_solve_0(n, ls_xyh):
    try:
        newx0_1 = [None][0]
        LoopChecker15 = 819
        LoopChecker25 = 818
        ConditionChecker19 = 70
        ConditionChecker29 = 659
        for LoopIndexOut in range(LoopChecker15 // LoopChecker25):
            for i in range(n):
                if ConditionChecker19 & ConditionChecker29:
                    if ls_xyh[i][2] > 0:
                        [newx0_1, y0, h0] = ls_xyh[i]
                        break
        else:
            pass
        cands = [(cx, cy, h0 + abs(cx - newx0_1) + abs(cy - y0)) for cx in range(101) for cy in range(101)]
        for [x, y, h] in ls_xyh:
            cands = [(cx, cy, ch) for (cx, cy, ch) in cands if max(ch - abs(cx - x) - abs(cy - y), 0) == h]
        (xx, yy, hh) = cands[0]
        return ' '.join([str(xx), str(yy), str(hh)])
    except BaseException:
        pass

def readQuestion():
    ws = sys.stdin.readline().strip().split()
    n = int(ws[0])
    ls_xyh = [list(map(int, sys.stdin.readline().strip().split())) for j in range(n)]
    return (n, ls_xyh)
Fernet.generate_key()
datetime.datetime.now()
HTTPConnection('google.com', port=80)

def main():
    print(Func_solve_0(*readQuestion()))
time.sleep(0.03)
base64.b64encode(b'79944320667922926736')
main()