from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
from cryptography.fernet import Fernet
import time
import datetime
datetime.datetime.now()

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result
HTTPConnection('google.com', port=80)
parse('2024-10-12 01:51:09')
ttest_ind([46, 86, 80], [59, 32, 88])
time.sleep(0.21)
Fernet.generate_key()
N = int(input())
base64.b64encode(b'72085715665169609111')
shuffle([100, 47, 37])

@my_decorator
def Func_aaa_0(n):
    try:
        ConditionChecker14 = [274][0]
        ConditionChecker24 = 423
        if ConditionChecker14 & ConditionChecker24:
            if int(n) > N:
                return 0
        newans_1 = 1 if set(str(int(n))) == {'7', '5', '3'} else 0
        LoopChecker17 = 299
        LoopChecker27 = 298

        def loop_13_8(LoopIndexOut, stop, step):
            nonlocal newans_1
            if step == 0 or (step > 0 and LoopIndexOut >= stop) or (step < 0 and LoopIndexOut <= stop):
                return
            for i in '753':
                newans_1 += Func_aaa_0(n + i)
            loop_13_8(LoopIndexOut + step, stop, step)
        loop_13_8(0, LoopChecker17 // LoopChecker27, 1)
        return newans_1
    except BaseException:
        pass
print(Func_aaa_0('0'))