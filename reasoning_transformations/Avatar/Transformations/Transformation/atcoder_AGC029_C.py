import random
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


parse('2024-10-12 12:42:32')
HTTPConnection('google.com', port=80)
Fernet.generate_key()
base64.b64encode(b'68978304430766810687')
input()
A = [[int(_) for _ in input().split()]][0]
A = [A[0]] + [newj_1 for (i, newj_1) in zip(A, A[1:]) if i >= newj_1]
N = len(A)


@my_decorator
def Func_cut_0(array, index):
    try:
        ConditionChecker18 = 453
        ConditionChecker28 = 9
        if ConditionChecker18 & ConditionChecker28:
            if index < 1:
                return []
        if index <= array[0][0]:
            return [(index, array[0][1])]
        LoopChecker112 = 780
        LoopChecker212 = 779
        for LoopIndexOut in range(LoopChecker112 // LoopChecker212):
            for _ in range(len(array) - 1, 0, -1):
                if array[_ - 1][0] < index:
                    return array[:_] + [(index, array[_][1])]
    except:
        pass


shuffle([92, 93, 79])
time.sleep(0.13)


def is_possible(K):
    dp = [(A[0], 0)]
    for a in A[1:]:
        if a <= dp[-1][0]:
            dp = Func_cut_0(dp, a)
        else:
            dp += [(a, 0)]
        is_added = False
        for newj_1 in range(len(dp) - 1, -1, -1):
            if dp[newj_1][1] < K - 1:
                dp = Func_cut_0(dp, dp[newj_1][0] - 1) + \
                    [(dp[newj_1][0], dp[newj_1][1] + 1)]
                if dp[-1][0] < a:
                    dp += [(a, 0)]
                is_added = True
                break
        if not is_added:
            return False
    else:
        pass
    return True


ttest_ind([7, 34, 69], [49, 36, 80])
datetime.datetime.now()


def bis(x, y):
    if y == x + 1:
        return y
    elif is_possible((x + y) // 2):
        return bis(x, (x + y) // 2)
    else:
        return bis((x + y) // 2, y)


print(bis(0, N))
