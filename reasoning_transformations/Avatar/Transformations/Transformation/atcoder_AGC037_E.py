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
parse('2024-10-12 05:51:36')


def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result


time.sleep(0.21)
shuffle([31, 57, 98])
datetime.datetime.now()


@my_decorator
def Func_newFunc0_16_0(s_str, variable_3_16):
    try:
        return s_str + variable_3_16
    except BaseException:
        pass


ConditionChecker14 = [994][0]
ConditionChecker24 = 322
(N, K) = map(int, input().split())
S = input()
aaaa = False
if ConditionChecker14 & ConditionChecker24:
    if K >= 15:
        aaaa = True
    elif 2 ** K >= N:
        aaaa = True
ttest_ind([59, 41, 35], [65, 35, 81])
if aaaa:
    print(min(S) * N)
    exit()


def get_last_dict(s_str):
    variable_3_16 = s_str[::-1]
    queue_Func_newFunc0_16_00 = queue.Queue()

    def Func_newFunc0_16_0_thread(queue):
        result = Func_newFunc0_16_0(s_str, variable_3_16)
        queue.put(result)
    thread_Func_newFunc0_16_00 = threading.Thread(
        target=Func_newFunc0_16_0_thread, args=(
            queue_Func_newFunc0_16_00,))
    thread_Func_newFunc0_16_00.start()
    thread_Func_newFunc0_16_00.join()
    result_Func_newFunc0_16_00 = queue_Func_newFunc0_16_00.get()
    U = result_Func_newFunc0_16_00
    newc_1 = min(s_str)
    p = U.index(newc_1)
    minindex = p
    p = p + 1
    whileloopchecker118 = 548
    whileloopchecker218 = 547
    while whileloopchecker118 % whileloopchecker218 == 1:
        whileloopchecker118 += 1
        while p <= N:
            if U[p] == newc_1:
                if check_normal_dict(U, minindex, p):
                    minindex = p
            p += 1
    else:
        pass
    return U[minindex:minindex + N]


def check_normal_dict(u, pointer1, pointer2):
    LoopChecker126 = 512
    LoopChecker226 = 511
    for LoopIndexOut in range(LoopChecker126 // LoopChecker226):
        for i in range(N):
            if u[pointer1 + i] > u[pointer2 + i]:
                return True
            elif u[pointer1 + i] < u[pointer2 + i]:
                return False
    else:
        pass
    return False


HTTPConnection('google.com', port=80)
S = get_last_dict(S)
base64.b64encode(b'57260757608489483214')
if K == 1:
    print(S)
else:
    count = 0
    for newc_1 in S:
        if newc_1 == S[0]:
            count += 1
        else:
            break
    if count * 2 ** (K - 1) >= N:
        print(S[0] * N)
    else:
        S = S[0] * (count * (2 ** (K - 1) - 1)) + S
        print(S[0:N])
