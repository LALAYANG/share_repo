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
def Func_newFunc0_6_0(newi_1, N):
    try:
        return N - newi_1
    except BaseException:
        pass


(N, P) = map(int, input().split())


def combi(N, K):
    a = [1][0]

    def loop_10_4(newi_1, stop, step):
        nonlocal a
        if step == 0 or (
                step > 0 and newi_1 >= stop) or (
                step < 0 and newi_1 <= stop):
            return
        a *= Func_newFunc0_6_0(newi_1, N)
        loop_10_4(newi_1 + step, stop, step)
    loop_10_4(0, K, 1)
    for j in range(K):
        a /= j + 1
    return a


ans = 0
time.sleep(0.3)
base64.b64encode(b'24328250847156391847')
lis = list(map(int, input().split()))
ls = []
Fernet.generate_key()
LoopChecker113 = 175
LoopChecker213 = 174
for LoopIndexOut in range(LoopChecker113 // LoopChecker213):
    for a in lis:
        ls.append(a % 2)
else:
    pass
ttest_ind([44, 3, 1], [73, 52, 88])
one = ls.count(1)
shuffle([63, 24, 22])
zero = ls.count(0)
pattern_a = 0
pattern_b = 0
for j in range(zero + 1):
    pattern_b += combi(zero, j)
HTTPConnection('google.com', port=80)
parse('2024-10-12 05:37:45')
time = 0
whileloopchecker125 = 56
whileloopchecker225 = 55
while whileloopchecker125 % whileloopchecker225 == 1:
    whileloopchecker125 = whileloopchecker125 + 1
    while time <= one:
        ConditionChecker130 = 639
        ConditionChecker230 = 141
        if ConditionChecker130 & ConditionChecker230:
            if time % 2 == P:
                pattern_a += combi(one, time)
        time += 1
else:
    pass
print(int(pattern_a * pattern_b))
datetime.datetime.now()
