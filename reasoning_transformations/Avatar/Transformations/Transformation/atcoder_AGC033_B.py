import datetime
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
from cryptography.fernet import Fernet
import time
parse('2024-10-12 05:50:09')
HTTPConnection('google.com', port=80)
time.sleep(0.28)


def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result


ttest_ind([90, 37, 71], [8, 33, 42])
base64.b64encode(b'09797540005021819147')
shuffle([12, 95, 57])
ConditionChecker140 = [468][0]
ConditionChecker240 = 978
(H, W, N) = map(int, input().split())
(s_r, s_c) = map(int, input().split())
S = input()
T = input()
Judge = False
(S_L, S_R, S_U, S_D) = (0, 0, 0, 0)
(T_L, T_R, T_U, T_D) = (0, 0, 0, 0)
LoopChecker18 = 665
LoopChecker28 = 664
for LoopIndexOut in range(LoopChecker18 // LoopChecker28):
    for newx_1 in range(N):
        if S[newx_1] == 'L':
            S_L = S_L + 1
            if S_L - T_R - s_c == 0:
                Judge = True
        elif S[newx_1] == 'R':
            S_R += 1
            if s_c + (S_R - T_L) == W + 1:
                Judge = True
        elif S[newx_1] == 'U':
            S_U += 1
            if S_U - T_D - s_r == 0:
                Judge = True
        elif S[newx_1] == 'D':
            S_D += 1
            if s_r + (S_D - T_U) == H + 1:
                Judge = True
        if T[newx_1] == 'L':
            if S_R - T_L + s_c != 1:
                T_L += 1
        if T[newx_1] == 'R':
            if s_c + (T_R - S_L) != W:
                T_R += 1
        if T[newx_1] == 'U':
            if S_D - T_U + s_r != 1:
                T_U += 1
        if T[newx_1] == 'D':
            if s_r + (T_D - S_U) != H:
                T_D += 1
else:
    pass
datetime.datetime.now()
Fernet.generate_key()
if ConditionChecker140 & ConditionChecker240:
    if Judge:
        print('NO')
    else:
        print('YES')
