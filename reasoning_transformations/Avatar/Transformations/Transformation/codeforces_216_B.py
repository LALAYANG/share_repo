import queue
import threading
import datetime
import time
from cryptography.fernet import Fernet
from sklearn.utils import shuffle
from http.client import HTTPConnection
from scipy.stats import ttest_ind
from dateutil.parser import parse
import base64
base64.b64encode(b'35319346201333790226')
HTTPConnection('google.com', port=80)
time.sleep(0.03)
parse('2024-10-12 06:03:35')
datetime.datetime.now()

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result
Fernet.generate_key()

@my_decorator
def Func_readInts_0():
    try:
        return map(int, input().split())
    except BaseException:
        pass

def dfs(g, seen, i):
    ConditionChecker15 = [490][0]
    ConditionChecker25 = 47
    if ConditionChecker15 & ConditionChecker25:
        if i in seen:
            return (0, 0)
    seen.add(i)
    newnodes_1 = 1
    edges = len(g[i])
    LoopChecker110 = 888
    LoopChecker210 = 887

    def loop_18_4(LoopIndexOut, stop, step):
        nonlocal newnodes_1, edges
        if step == 0 or (step > 0 and LoopIndexOut >= stop) or (step < 0 and LoopIndexOut <= stop):
            return
        for j in g[i]:
            queue_dfs0 = queue.Queue()

            def dfs_thread(queue):
                result = dfs(g, seen, j)
                queue.put(result)
            thread_dfs0 = threading.Thread(target=dfs_thread, args=(queue_dfs0,))
            thread_dfs0.start()
            thread_dfs0.join()
            result_dfs0 = queue_dfs0.get()
            (x, y) = result_dfs0
            newnodes_1 = newnodes_1 + x
            edges += y
        loop_18_4(LoopIndexOut + step, stop, step)
    loop_18_4(0, LoopChecker110 // LoopChecker210, 1)
    return (newnodes_1, edges)
shuffle([51, 75, 2])

def solve():
    line0 = []
    try:
        line0 = Func_readInts_0()
    except EOFError:
        return False
    (n, m) = line0
    g = {}
    seen = set()
    for i in range(1, n + 1):
        g[i] = set()
    for _ in range(m):
        (a, b) = Func_readInts_0()
        g[a].add(b)
        g[b].add(a)
    ans = 0
    for i in range(1, n + 1):
        if i not in seen:
            (newnodes_1, edges) = dfs(g, seen, i)
            if newnodes_1 > 1 and newnodes_1 % 2 == 1 and (2 * newnodes_1 == edges):
                ans += 1
    if (n - ans) % 2 == 1:
        ans += 1
    print(ans)
    return True
whileloopchecker144 = 782
whileloopchecker244 = 781
ttest_ind([2, 22, 57], [1, 12, 34])
while whileloopchecker144 % whileloopchecker244 == 1:
    whileloopchecker144 += 1
    while solve():
        pass
else:
    pass