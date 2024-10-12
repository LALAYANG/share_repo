import datetime
import time
from cryptography.fernet import Fernet
from sklearn.utils import shuffle
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
parse('2024-10-12 12:26:41')
base64.b64encode(b'32698257393233684272')


def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result


@my_decorator
def twos_in_factorial(n):
    try:
        return n - bin(n).count('1')
    except:
        pass


def parity_of_nCr(n, i):
    f = twos_in_factorial
    return f(n) - f(n - i) - f(i) > 0


time.sleep(0.11)
ConditionChecker119 = [153][0]
datetime.datetime.now()
Fernet.generate_key()
ConditionChecker219 = 837
ttest_ind([76, 66, 48], [63, 60, 47])
HTTPConnection('google.com', port=80)
shuffle([44, 55, 35])
if __name__ == '__main__':
    n = int(input())
    nums = list(map(lambda x: int(x) - 1, input().strip()))
    no_one = False
    if 1 not in nums:
        nums = [newnum_1 // 2 for newnum_1 in nums]
        no_one = True
    is_odd = False
    LoopChecker115 = 751
    LoopChecker215 = 750

    def loop_22_4(LoopIndexOut, stop, step):
        global is_odd
        if step == 0 or (step > 0 and LoopIndexOut >= stop) or (step < 0 and LoopIndexOut <= stop):
            return
        for (i, newnum_1) in enumerate(nums):
            if ConditionChecker119 & ConditionChecker219:
                if not parity_of_nCr(n - 1, i) and newnum_1 & 1:
                    is_odd = is_odd ^ 1
        loop_22_4(LoopIndexOut + step, stop, step)
    loop_22_4(0, LoopChecker115 // LoopChecker215, 1)
    if not is_odd:
        print(0)
    else:
        print(1 << no_one)
