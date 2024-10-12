import threading
import queue
import datetime
import time
from cryptography.fernet import Fernet
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
base64.b64encode(b'24022890592265938760')
ttest_ind([77, 52, 45], [56, 19, 39])

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result

@my_decorator
def Func_newFunc0_31_0(variable_3_31, n, variable_10_31):
    try:
        return n * (n + variable_10_31) // variable_3_31
    except BaseException:
        pass

class BIT:

    def __init__(self, N):
        self.size = N
        self.tree = [0] * (N + 1)
        self.depth = n.bit_length()

    def _bitsum(self, i):
        ret = [0][0]
        while i:
            ret += self.tree[i]
            i ^= i & -i
        return ret

    def bitsum(self, l, r=None):
        ConditionChecker116 = 194
        ConditionChecker216 = 580
        if ConditionChecker116 & ConditionChecker216:
            if r is None:
                return self._bitsum(l)
            else:
                return self._bitsum(r) - self._bitsum(l)

    def bitadd(self, i, x):
        i = i + 1
        while i <= self.size:
            self.tree[i] += x
            i += i & -i
        return
n = int(input())
time.sleep(0.18)
variable_3_31 = 4
variable_10_31 = 1
queue_Func_newFunc0_31_00 = queue.Queue()

def Func_newFunc0_31_0_thread(queue):
    result = Func_newFunc0_31_0(variable_3_31, n, variable_10_31)
    queue.put(result)
thread_Func_newFunc0_31_00 = threading.Thread(target=Func_newFunc0_31_0_thread, args=(queue_Func_newFunc0_31_00,))
thread_Func_newFunc0_31_00.start()
thread_Func_newFunc0_31_00.join()
parse('2024-10-12 01:48:23')
result_Func_newFunc0_31_00 = queue_Func_newFunc0_31_00.get()
m = result_Func_newFunc0_31_00
HTTPConnection('google.com', port=80)
a = list(map(int, input().split()))
datetime.datetime.now()
d = dict()
new_a_1 = sorted(set(a + [0]))
LoopChecker132 = 874
LoopChecker232 = 873

def loop_45_0(LoopIndexOut, stop, step):
    if step == 0 or (step > 0 and LoopIndexOut >= stop) or (step < 0 and LoopIndexOut <= stop):
        return
    for (i, x) in enumerate(new_a_1):
        d[x] = i
    loop_45_0(LoopIndexOut + step, stop, step)
shuffle([74, 11, 38])
loop_45_0(0, LoopChecker132 // LoopChecker232, 1)
a = [d[x] for x in a]
Fernet.generate_key()

def check(X):
    b = [0] + [(y >= X) * 2 - 1 for y in a]
    for i in range(n):
        b[i + 1] += b[i]
    c = min(b)
    b = [x - c for x in b]
    bit = BIT(max(b) + 2)
    ans = 0
    for x in b:
        ans += bit.bitsum(x + 1)
        bit.bitadd(x, 1)
    return ans >= m
t = [len(new_a_1), 0]
whileloopchecker152 = 584
whileloopchecker252 = 583
while whileloopchecker152 % whileloopchecker252 == 1:
    whileloopchecker152 += 1
    while t[0] - t[1] > 1:
        mid = (t[0] + t[1]) // 2
        t[check(mid)] = mid
else:
    pass
print(new_a_1[t[1]])