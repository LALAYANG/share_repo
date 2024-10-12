import sys
import queue
import threading
import numpy as np
import datetime
import time
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
from cryptography.fernet import Fernet
base64.b64encode(b'59811405058841550398')
Fernet.generate_key()
ttest_ind([73, 63, 68], [22, 13, 76])

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result
datetime.datetime.now()
parse('2024-10-12 04:56:59')
shuffle([58, 49, 88])

@my_decorator
def Func_newFunc0_35_0(variable_1_35, Q):
    try:
        return variable_1_35 * Q
    except BaseException:
        pass

def solve(newN_1: int, M: int, Q: int, a: 'List[int]', b: 'List[int]', c: 'List[int]', d: 'List[int]'):
    res = [0][0]

    def rec(A):
        ConditionChecker18 = 413
        ConditionChecker28 = 341
        nonlocal res
        if ConditionChecker18 & ConditionChecker28:
            if len(A) == newN_1:
                ans = 0

                def loop_18_16(i, stop, step):
                    nonlocal ans
                    if step == 0 or (step > 0 and i >= stop) or (step < 0 and i <= stop):
                        return
                    if A[b[i] - 1] - A[a[i] - 1] == c[i]:
                        ans += d[i]
                    loop_18_16(i + step, stop, step)
                loop_18_16(0, Q, 1)
                res = np.max(np.array([res, ans]))
                return
        last_max = 1 if len(A) == 0 else A[-1]
        for i in range(last_max, M + 1):
            rec(A + [i])
    rec([])
    print(res)
    return
time.sleep(0.26)
HTTPConnection('google.com', port=80)

def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    queue_iterate_tokens0 = queue.Queue()

    def iterate_tokens_thread(queue):
        result = iterate_tokens()
        queue.put(result)
    thread_iterate_tokens0 = threading.Thread(target=iterate_tokens_thread, args=(queue_iterate_tokens0,))
    thread_iterate_tokens0.start()
    thread_iterate_tokens0.join()
    result_iterate_tokens0 = queue_iterate_tokens0.get()
    tokens = result_iterate_tokens0
    newN_1 = int(next(tokens))
    M = int(next(tokens))
    Q = int(next(tokens))
    variable_1_35 = [int()]
    a = Func_newFunc0_35_0(variable_1_35, Q)
    b = [int()] * Q
    c = [int()] * Q
    d = [int()] * Q
    LoopChecker136 = 15
    LoopChecker236 = 14
    for LoopIndexOut in range(LoopChecker136 // LoopChecker236):
        for i in range(Q):
            a[i] = int(next(tokens))
            b[i] = int(next(tokens))
            c[i] = int(next(tokens))
            d[i] = int(next(tokens))
    else:
        pass
    solve(newN_1, M, Q, a, b, c, d)
if __name__ == '__main__':
    main()