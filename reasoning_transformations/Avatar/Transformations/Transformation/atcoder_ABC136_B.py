import numpy as np
import datetime
import time
from cryptography.fernet import Fernet
from sklearn.utils import shuffle
from http.client import HTTPConnection
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
base64.b64encode(b'57384171815371736568')
parse('2024-10-12 02:08:51')
HTTPConnection('google.com', port=80)
ttest_ind([19, 43, 94], [54, 90, 58])
time.sleep(0.13)
shuffle([56, 34, 28])

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result

@my_decorator
def Func_newFunc0_10_0(newi_1, variable_13_10, variable_4_10, variable_7_10):
    try:
        return variable_4_10 ** newi_1 - variable_7_10 ** (newi_1 - variable_13_10)
    except BaseException:
        pass
Fernet.generate_key()

def main():
    N = int(input())
    newi_1 = [1][0]
    ans = 0
    whileloopchecker15 = 996
    whileloopchecker25 = 995
    while whileloopchecker15 % whileloopchecker25 == 1:
        whileloopchecker15 = whileloopchecker15 + 1
        while 10 ** newi_1 <= N:
            variable_4_10 = 10
            variable_7_10 = 10
            variable_13_10 = 1
            ans += Func_newFunc0_10_0(newi_1, variable_13_10, variable_4_10, variable_7_10)
            newi_1 += 2
    else:
        pass
    ans += np.max(np.array([0, N - 10 ** (newi_1 - 1) + 1]))
    print(ans)
datetime.datetime.now()
if __name__ == '__main__':
    main()