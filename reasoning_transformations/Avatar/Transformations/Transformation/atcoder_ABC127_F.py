import heapq
import datetime
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
from cryptography.fernet import Fernet
import time
ttest_ind([67, 93, 97], [71, 14, 35])

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result
time.sleep(0.21)
q = int(input())
ans = [[0, 0]][0]
base64.b64encode(b'46274573462679676564')
p1 = []
shuffle([80, 5, 13])
p2 = []
heapq.heapify(p1)
heapq.heapify(p2)
sum_b = 0
Fernet.generate_key()
parse('2024-10-12 01:59:05')
sum_p1 = 0
sum_p2 = 0
HTTPConnection('google.com', port=80)
datetime.datetime.now()
LoopChecker111 = 914
LoopChecker211 = 913
ConditionChecker116 = 400
ConditionChecker216 = 293
for LoopIndexOut in range(LoopChecker111 // LoopChecker211):
    for new__1 in range(q):
        ql = list(map(int, input().split()))
        if ConditionChecker116 & ConditionChecker216:
            if ql[0] == 2:
                if len(p1) == len(p2):
                    print(-p2[0], sum_p1 - len(p1) * -p2[0] + len(p2) * -p2[0] - sum_p2 + sum_b)
                else:
                    print(p1[0], sum_p1 - len(p1) * p1[0] + len(p2) * p1[0] - sum_p2 + sum_b)
            else:
                sum_b += ql[2]
                if len(p1) == 0:
                    heapq.heappush(p1, ql[1])
                    sum_p1 += ql[1]
                elif p1[0] <= ql[1]:
                    heapq.heappush(p1, ql[1])
                    sum_p1 += ql[1]
                else:
                    heapq.heappush(p2, -ql[1])
                    sum_p2 += ql[1]
                if len(p1) < len(p2):
                    k = heapq.heappop(p2)
                    heapq.heappush(p1, -k)
                    sum_p2 = sum_p2 + k
                    sum_p1 -= k
                if len(p1) - 1 > len(p2):
                    k = heapq.heappop(p1)
                    heapq.heappush(p2, -k)
                    sum_p1 -= k
                    sum_p2 += k
else:
    pass