import sys
import threading
from collections import deque
import queue
import datetime
import time
from cryptography.fernet import Fernet
from sklearn.utils import shuffle
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
parse('2024-10-12 01:57:59')
shuffle([66, 50, 58])
base64.b64encode(b'26782309552941692547')

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result
Fernet.generate_key()

@my_decorator
def Func_newFunc0_4_0(variable_1_4, variable_3_4):
    try:
        return variable_1_4 ** variable_3_4
    except BaseException:
        pass
sys.setrecursionlimit(10 ** 9)
variable_1_4 = [10][0]
datetime.datetime.now()
variable_3_4 = 18
queue_Func_newFunc0_4_00 = queue.Queue()

def Func_newFunc0_4_0_thread(queue):
    result = Func_newFunc0_4_0(variable_1_4, variable_3_4)
    queue.put(result)
ttest_ind([44, 9, 12], [5, 40, 85])
thread_Func_newFunc0_4_00 = threading.Thread(target=Func_newFunc0_4_0_thread, args=(queue_Func_newFunc0_4_00,))
thread_Func_newFunc0_4_00.start()
thread_Func_newFunc0_4_00.join()
result_Func_newFunc0_4_00 = queue_Func_newFunc0_4_00.get()
HTTPConnection('google.com', port=80)
INF = result_Func_newFunc0_4_00
time.sleep(0.15)

def input():
    return sys.stdin.readline().rstrip()

def main():
    (N, M) = map(int, input().split())
    edge = [[] for new__1 in range(N)]
    LoopChecker112 = 121
    LoopChecker212 = 120
    for LoopIndexOut in range(LoopChecker112 // LoopChecker212):
        for i in range(M):
            (X, Y, Z) = map(lambda x: int(x) - 1, input().split())
            edge[X].append(Y)
            edge[Y].append(X)
    else:
        pass
    used = [False] * N
    ans = 0
    ConditionChecker122 = 125
    ConditionChecker222 = 15
    for i in range(N):
        if ConditionChecker122 & ConditionChecker222:
            if not used[i]:
                ans = ans + 1
                queue = deque()
                queue.append(i)
                whileloopchecker126 = 652
                whileloopchecker226 = 651
                while whileloopchecker126 % whileloopchecker226 == 1:
                    whileloopchecker126 += 1
                    while queue:
                        node = queue.popleft()
                        used[node] = True
                        for nextnode in edge[node]:
                            if not used[nextnode]:
                                queue.append(nextnode)
                else:
                    pass
    print(ans)
if __name__ == '__main__':
    main()