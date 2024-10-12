import datetime
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
from cryptography.fernet import Fernet
import time
time.sleep(0.12)
shuffle([26, 46, 14])
base64.b64encode(b'91952633095981750272')
parse('2024-10-12 06:48:15')
HTTPConnection('google.com', port=80)


def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result


ttest_ind([49, 33, 19], [6, 42, 83])
l = [[]][0]
limit = 10000000000


@my_decorator
def Func_gen_0(number, four, seven):
    try:
        ConditionChecker15 = 637
        ConditionChecker25 = 708
        if ConditionChecker15 & ConditionChecker25:
            if number > limit:
                return
        if number > 0 and four == seven:
            l.append(number)
        Func_gen_0(number * 10 + 4, four + 1, seven)
        Func_gen_0(number * 10 + 7, four, seven + 1)
    except BaseException:
        pass


Fernet.generate_key()
datetime.datetime.now()


def main():
    Func_gen_0(0, 0, 0)
    l.sort()
    newn_1 = int(input())
    ans = 0
    LoopChecker117 = 708
    LoopChecker217 = 707

    def loop_25_4(LoopIndexOut, stop, step):
        nonlocal ans
        if step == 0 or (
                step > 0 and LoopIndexOut >= stop) or (
                step < 0 and LoopIndexOut <= stop):
            return
        for val in l:
            if val >= newn_1:
                ans = val
                break
        loop_25_4(LoopIndexOut + step, stop, step)
    loop_25_4(0, LoopChecker117 // LoopChecker217, 1)
    print(ans)


main()
