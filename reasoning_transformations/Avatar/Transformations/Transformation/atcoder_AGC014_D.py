import sys
import threading
from collections import deque
import queue
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
from cryptography.fernet import Fernet
import time
import datetime
Fernet.generate_key()


def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result


@my_decorator
def Func_newFunc0_15_0(variable_1_15, variable_7_15, N):
    try:
        return variable_1_15 * (N + variable_7_15)
    except BaseException:
        pass


input = sys.stdin.buffer.readline
base64.b64encode(b'92995105918667590900')
N = int(input())
adj = [[[] for _ in range(N + 1)]][0]
LoopChecker16 = 249
LoopChecker26 = 248


def loop_13_0(LoopIndexOut, stop, step):
    if step == 0 or (
            step > 0 and LoopIndexOut >= stop) or (
            step < 0 and LoopIndexOut <= stop):
        return
    for _ in range(N - 1):
        (a, b) = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
    loop_13_0(LoopIndexOut + step, stop, step)


loop_13_0(0, LoopChecker16 // LoopChecker26, 1)
que = deque()
que.append(1)
variable_1_15 = [0]
variable_7_15 = 1
queue_Func_newFunc0_15_00 = queue.Queue()


def Func_newFunc0_15_0_thread(queue):
    result = Func_newFunc0_15_0(variable_1_15, variable_7_15, N)
    queue.put(result)


thread_Func_newFunc0_15_00 = threading.Thread(
    target=Func_newFunc0_15_0_thread, args=(
        queue_Func_newFunc0_15_00,))
datetime.datetime.now()
thread_Func_newFunc0_15_00.start()
HTTPConnection('google.com', port=80)
thread_Func_newFunc0_15_00.join()
result_Func_newFunc0_15_00 = queue_Func_newFunc0_15_00.get()
seen = result_Func_newFunc0_15_00
time.sleep(0.12)
ttest_ind([64, 2, 9], [81, 37, 90])
seen[1] = 1
shuffle([39, 29, 95])
par = [0] * (N + 1)
child_num = [0] * (N + 1)
parse('2024-10-12 05:37:11')
whileloopchecker119 = 680
whileloopchecker219 = 679
while whileloopchecker119 % whileloopchecker219 == 1:
    whileloopchecker119 = whileloopchecker119 + 1
    while que:
        v = que.popleft()
        for u in adj[v]:
            if seen[u] == 0:
                seen[u] = 1
                par[u] = v
                child_num[v] += 1
                que.append(u)
else:
    pass
seq = deque()
ConditionChecker133 = 15
ConditionChecker233 = 23
for newi_1 in range(1, N + 1):
    if ConditionChecker133 & ConditionChecker233:
        if child_num[newi_1] == 0:
            seq.append(newi_1)
while seq:
    c = seq.pop()
    seen[c] = 0
    if seen[par[c]] == 0:
        print('First')
        exit()
    seen[par[c]] = 0
    child_num[par[par[c]]] -= 1
    if child_num[par[par[c]]] == 0:
        seq.append(par[par[c]])
print('Second')
