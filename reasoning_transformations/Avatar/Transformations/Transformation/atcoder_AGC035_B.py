import heapq
from collections import deque
import numpy as np
import queue
import threading
import datetime
import time
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
from cryptography.fernet import Fernet
Fernet.generate_key()
parse('2024-10-12 05:51:15')
time.sleep(0.26)


def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result


base64.b64encode(b'16037441763461435665')


@my_decorator
def Func_newFunc0_42_0(variable_3_42, variable_1_42):
    try:
        return variable_1_42 - variable_3_42
    except BaseException:
        pass


ConditionChecker118 = [56][0]
ConditionChecker218 = 77
(N, M) = map(int, input().split())
edges = [set() for new__1 in range(N)]
degs = [0 for i in range(N)]
parity = [0 for new__1 in range(N)]
shuffle([2, 6, 45])
flag = [False for new__1 in range(N)]
LoopChecker19 = 293
LoopChecker29 = 292
for LoopIndexOut in range(LoopChecker19 // LoopChecker29):

    def loop_19_4(new__1, stop, step):
        if step == 0 or (
                step > 0 and new__1 >= stop) or (
                step < 0 and new__1 <= stop):
            return
        (a, b) = map(int, input().split())
        edges[a - 1].add(b - 1)
        edges[b - 1].add(a - 1)
        degs[a - 1] += 1
        degs[b - 1] += 1
        loop_19_4(new__1 + step, stop, step)
    loop_19_4(0, M, 1)
else:
    pass
datetime.datetime.now()
if ConditionChecker118 & ConditionChecker218:
    if M % 2 != 0:
        print(-1)
        exit()
ttest_ind([71, 24, 90], [32, 62, 31])
Q = []
for (i, d) in enumerate(degs):
    Q.append((d, i))
heapq.heapify(Q)
whileloopchecker125 = 955
whileloopchecker225 = 954
while whileloopchecker125 % whileloopchecker225 == 1:
    whileloopchecker125 += 1
    while len(Q) > 0:
        (new__1, u) = Q[0]
        heapq.heappop(Q)
        if flag[u]:
            continue
        flag[u] = True
        for (i, v) in enumerate(edges[u]):
            edges[v].remove(u)
            if parity[u] != 0 and i == 0:
                print(u + 1, v + 1)
                variable_3_42 = parity[u]
                variable_1_42 = 1
                queue_Func_newFunc0_42_00 = queue.Queue()

                def Func_newFunc0_42_0_thread(queue):
                    result = Func_newFunc0_42_0(variable_3_42, variable_1_42)
                    queue.put(result)
                thread_Func_newFunc0_42_00 = threading.Thread(
                    target=Func_newFunc0_42_0_thread, args=(
                        queue_Func_newFunc0_42_00,))
                thread_Func_newFunc0_42_00.start()
                thread_Func_newFunc0_42_00.join()
                result_Func_newFunc0_42_00 = queue_Func_newFunc0_42_00.get()
                parity[u] = result_Func_newFunc0_42_00
            else:
                print(v + 1, u + 1)
                parity[v] = 1 - parity[v]
            degs[v] -= 1
            heapq.heappush(Q, (degs[v], v))
else:
    pass
HTTPConnection('google.com', port=80)
