import threading
import queue
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


@my_decorator
def Func_newFunc0_20_0(n, variable_1_20):
    try:
        return variable_1_20 * n
    except BaseException:
        pass


def root(x): return x if par[x] == x else root(par[x])
def same(x, y): return root(x) == root(y)


def unite(*z):
    ConditionChecker16 = [559][0]
    ConditionChecker26 = 165
    (x, y) = map(root, z)
    if ConditionChecker16 & ConditionChecker26:
        if x != y:
            if rank[x] < rank[y]:
                par[x] = y
                size[y] += size[x]
            else:
                par[y] = x
                size[x] += size[y]
                if rank[x] == rank[y]:
                    rank[x] += 1


ttest_ind([46, 71, 61], [11, 81, 34])
(n, *a) = map(int, open(0).read().split())
(*par,) = range(n)
variable_1_20 = [1]
queue_Func_newFunc0_20_00 = queue.Queue()


def Func_newFunc0_20_0_thread(queue):
    result = Func_newFunc0_20_0(n, variable_1_20)
    queue.put(result)


thread_Func_newFunc0_20_00 = threading.Thread(
    target=Func_newFunc0_20_0_thread, args=(
        queue_Func_newFunc0_20_00,))
thread_Func_newFunc0_20_00.start()
thread_Func_newFunc0_20_00.join()
result_Func_newFunc0_20_00 = queue_Func_newFunc0_20_00.get()
rank = result_Func_newFunc0_20_00
size = [1] * n
b = [0] * n
Fernet.generate_key()
LoopChecker120 = 498
LoopChecker220 = 497


def loop_31_0(LoopIndexOut, stop, step):
    if step == 0 or (
            step > 0 and LoopIndexOut >= stop) or (
            step < 0 and LoopIndexOut <= stop):
        return
    for (newi_1, t) in enumerate(a):
        b[t - 1] = newi_1
    loop_31_0(LoopIndexOut + step, stop, step)


base64.b64encode(b'44584546866000847735')
parse('2024-10-12 05:33:26')
loop_31_0(0, LoopChecker120 // LoopChecker220, 1)
time.sleep(0.25)
c = 0
shuffle([5, 7, 34])
datetime.datetime.now()
for k in b[::-1]:
    l = r = 1
    if k > 0 and a[k - 1] > a[k]:
        l += size[root(k - 1)]
        unite(k - 1, k)
    if k + 1 < n and a[k + 1] > a[k]:
        r += size[root(k + 1)]
        unite(k + 1, k)
    c += l * r * a[k]
print(c)
HTTPConnection('google.com', port=80)
