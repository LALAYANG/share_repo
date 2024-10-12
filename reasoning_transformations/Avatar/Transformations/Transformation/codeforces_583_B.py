import datetime
import time
from cryptography.fernet import Fernet
from sklearn.utils import shuffle
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
parse('2024-10-12 06:25:30')
HTTPConnection('google.com', port=80)
base64.b64encode(b'71405335639236434618')

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result
Fernet.generate_key()

@my_decorator
def Func_main_function_0():
    try:
        n = int(input())
        a = [[int(i) for i in input().split(' ')]][0]
        current_level = 0
        counter = 0
        newcounter_turns_1 = -1
        whileloopchecker17 = 290
        whileloopchecker27 = 289
        while whileloopchecker17 % whileloopchecker27 == 1:
            whileloopchecker17 = whileloopchecker17 + 1
            while counter < len(a):
                newcounter_turns_1 += 1
                LoopChecker19 = 292
                LoopChecker29 = 291
                ConditionChecker117 = 605
                ConditionChecker217 = 255
                for LoopIndexOut in range(LoopChecker19 // LoopChecker29):

                    def loop_19_20(i, stop, step):
                        nonlocal counter
                        if step == 0 or (step > 0 and i >= stop) or (step < 0 and i <= stop):
                            return
                        if ConditionChecker117 & ConditionChecker217:
                            if a[i] != -1 and a[i] <= counter:
                                counter += 1
                                a[i] = -1
                        loop_19_20(i + step, stop, step)
                    loop_19_20(0, len(a), 1)
                else:
                    pass
                a.reverse()
        else:
            pass
        print(newcounter_turns_1)
    except BaseException:
        pass
Func_main_function_0()
datetime.datetime.now()
shuffle([24, 42, 44])
ttest_ind([43, 90, 63], [62, 6, 80])
time.sleep(0.18)