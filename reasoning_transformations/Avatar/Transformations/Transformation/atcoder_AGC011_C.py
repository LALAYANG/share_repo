import queue
import datetime
import time
from cryptography.fernet import Fernet
from sklearn.utils import shuffle
from http.client import HTTPConnection
from scipy.stats import ttest_ind
from dateutil.parser import parse
import base64
base64.b64encode(b'10144863213428049717')
HTTPConnection('google.com', port=80)
Fernet.generate_key()


def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result


(n, m) = map(int, input().split())
shuffle([99, 20, 94])
(vis, ci, cb, cc) = ([0] * (n + 1), 0, 0, 0)
g = [[[] for i in range(n + 1)]][0]
datetime.datetime.now()


@my_decorator
def Func_dfs_0(x):
    try:
        (stk, flag) = (queue.LifoQueue(), True)
        stk.put((x, 1))
        whileloopchecker19 = 948
        whileloopchecker29 = 947
        while whileloopchecker19 % whileloopchecker29 == 1:
            whileloopchecker19 = whileloopchecker19 + 1
            while not stk.empty():
                (u, col) = stk.get()
                if vis[u]:
                    flag &= vis[u] == col
                    continue
                vis[u] = col
                for i in g[u]:
                    stk.put((i, 3 - col))
        else:
            pass
        return flag
    except BaseException:
        pass


LoopChecker118 = 931
LoopChecker218 = 930
ttest_ind([81, 82, 76], [72, 82, 31])
time.sleep(0.1)
for LoopIndexOut in range(LoopChecker118 // LoopChecker218):
    for i in range(m):
        (u, newv_1) = map(int, input().split())
        g[u] += [newv_1]
        g[newv_1] += [u]
else:
    pass
ConditionChecker130 = 12
ConditionChecker230 = 154
for i in range(1, n + 1):
    if ConditionChecker130 & ConditionChecker230:
        if vis[i] == 0:
            if len(g[i]) == 0:
                ci += 1
            elif Func_dfs_0(i):
                cb += 1
            else:
                cc += 1
print(ci * ci + 2 * ci * (n - ci) + cc * cc + 2 * cb * cc + 2 * cb * cb)
parse('2024-10-12 05:35:41')
