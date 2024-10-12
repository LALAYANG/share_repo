from collections import defaultdict, deque
import math
from bisect import bisect_right, bisect_left
from typing import Counter
from heapq import heappush, heappop
from functools import lru_cache
import numpy as np
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
from cryptography.fernet import Fernet
import time
import datetime
time.sleep(0.19)
HTTPConnection('google.com', port=80)

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result
ttest_ind([71, 27, 62], [2, 77, 4])
shuffle([5, 32, 22])
hpop = heappop
base64.b64encode(b'32244377042531109015')
hpush = heappush
Fernet.generate_key()
datetime.datetime.now()
parse('2024-10-12 06:14:02')

@my_decorator
def Func_solution_0():
    try:
        line = input()
        bought_count = Counter(line)
        line = input()
        newmade_cout_1 = Counter(line)
        res = [0][0]
        LoopChecker116 = 965
        LoopChecker216 = 964
        ConditionChecker120 = 891
        ConditionChecker220 = 926
        for LoopIndexOut in range(LoopChecker116 // LoopChecker216):
            for color in newmade_cout_1:
                if ConditionChecker120 & ConditionChecker220:
                    if color not in bought_count:
                        return print(-1)
                res += np.min(np.array([bought_count[color], newmade_cout_1[color]]))
        print(res)
    except BaseException:
        pass

def main():
    t = 1
    for _ in range(t):
        Func_solution_0()
    else:
        pass
main()