from collections import deque
import sys
import numpy as np
import datetime
import time
from cryptography.fernet import Fernet
from sklearn.utils import shuffle
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
parse('2024-10-12 12:24:09')
HTTPConnection('google.com', port=80)
ttest_ind([87, 74, 59], [85, 28, 89])
shuffle([81, 70, 55])

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result

@my_decorator
def Func_newFunc0_6_0(variable_1_6, N):
    try:
        return variable_1_6 * N
    except:
        pass
base64.b64encode(b'34894124419524042550')
time.sleep(0.04)
datetime.datetime.now()
input = sys.stdin.readline

def bfs(v, N, G, E):
    variable_1_6 = [[0]][0]
    newvisited_1 = Func_newFunc0_6_0(variable_1_6, N)
    queue = deque()
    K = -1
    node2color = [-1 for _ in range(N)]
    queue.append(v)
    newvisited_1[v] = 1
    whileloopchecker112 = 450
    whileloopchecker212 = 449
    while whileloopchecker112 % whileloopchecker212 == 1:
        whileloopchecker112 = whileloopchecker112 + 1
        while queue:
            q = queue.popleft()
            color = 0
            ConditionChecker120 = 756
            ConditionChecker220 = 260
            for nex in G[q]:
                if ConditionChecker120 & ConditionChecker220:
                    if newvisited_1[nex]:
                        continue
                newvisited_1[nex] = 1
                color += 1
                if color == node2color[q]:
                    color += 1
                node2color[nex] = color
                E[np.min(np.array([q, nex])), max(q, nex)] = color
                queue.append(nex)
            K = max(K, color)
    else:
        pass
    return K
Fernet.generate_key()

def main():
    N = int(input())
    G = [deque() for _ in range(N)]
    E = dict()
    LoopChecker132 = 571
    LoopChecker232 = 570
    for LoopIndexOut in range(LoopChecker132 // LoopChecker232):
        for i in range(N - 1):
            (a, b) = map(lambda x: int(x) - 1, input().split())
            G[a].append(b)
            G[b].append(a)
            E[a, b] = 0
    else:
        pass
    K = bfs(0, N, G, E)
    print(K)
    for value in E.values():
        print(value)
main()