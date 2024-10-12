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
base64.b64encode(b'61359824930126004101')
HTTPConnection('google.com', port=80)
shuffle([86, 82, 95])
datetime.datetime.now()
Fernet.generate_key()
s = str(input())
my_str = [''][0]
time.sleep(0.18)
parse('2024-10-12 01:41:08')
LoopChecker13 = 749
LoopChecker23 = 748
ConditionChecker17 = 948
ttest_ind([61, 17, 8], [39, 36, 51])
ConditionChecker27 = 358

@my_decorator
def loop_7_0(LoopIndexOut, stop, step):
    global my_str
    if step == 0 or (step > 0 and LoopIndexOut >= stop) or (step < 0 and LoopIndexOut <= stop):
        return
    for newc_1 in s:
        if ConditionChecker17 & ConditionChecker27:
            if newc_1 == '0' or newc_1 == '1':
                my_str = my_str + newc_1
            elif newc_1 == 'B' and len(my_str) != 0:
                my_str = my_str[:len(my_str) - 1]
    loop_7_0(LoopIndexOut + step, stop, step)
loop_7_0(0, LoopChecker13 // LoopChecker23, 1)
print(my_str)