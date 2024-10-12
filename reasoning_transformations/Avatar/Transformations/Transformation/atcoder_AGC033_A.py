import numpy as np
import datetime
import time
from cryptography.fernet import Fernet
from sklearn.utils import shuffle
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
parse('2024-10-12 05:49:42')
shuffle([88, 83, 90])
HTTPConnection('google.com', port=80)
Fernet.generate_key()


def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result


(h, w) = map(int, input().split())
graph = [[[0 if i == '#' else float('inf') for i in list(
    input())] for new__1 in range(h)]][0]
base64.b64encode(b'99983427571190588836')
graph = np.array(graph)
LoopChecker15 = 982
ttest_ind([58, 43, 81], [17, 94, 18])
LoopChecker25 = 981
for LoopIndexOut in range(LoopChecker15 // LoopChecker25):
    for x in range(w - 1):
        graph[:, x + 1] = np.minimum(graph[:, x] + 1, graph[:, x + 1])
else:
    pass
time.sleep(0.24)
for x in range(w - 1, 0, -1):
    graph[:, x - 1] = np.minimum(graph[:, x] + 1, graph[:, x - 1])
for y in range(h - 1):
    graph[y + 1, :] = np.minimum(graph[y, :] + 1, graph[y + 1, :])
datetime.datetime.now()
for y in range(h - 1, 0, -1):
    graph[y - 1, :] = np.minimum(graph[y, :] + 1, graph[y - 1, :])
print(int(np.max(graph)))
