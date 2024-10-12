import datetime
import time
from cryptography.fernet import Fernet
from sklearn.utils import shuffle
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
HTTPConnection('google.com', port=80)

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result

@my_decorator
def Func_newFunc0_29_0(variable_3_29, nfat):
    try:
        return nfat / variable_3_29
    except BaseException:
        pass
n = int(input())
parse('2024-10-12 06:31:13')
cake = [[]][0]
newhappiness_1 = 0
chocCount = 0
base64.b64encode(b'52938788929250408896')
nfat = 1
LoopChecker16 = 396
LoopChecker26 = 395
ttest_ind([11, 22, 14], [4, 25, 15])
datetime.datetime.now()
Fernet.generate_key()
for LoopIndexOut in range(LoopChecker16 // LoopChecker26):
    for i in range(n):
        line = str(input())
        cake.append(line)
        for j in line:
            if j == 'C':
                chocCount = chocCount + 1
        if chocCount > 1:

            def loop_21_12(i, stop, step):
                global nfat
                if step == 0 or (step > 0 and i >= stop) or (step < 0 and i <= stop):
                    return
                nfat *= i
                loop_21_12(i + step, stop, step)
            loop_21_12(chocCount, chocCount - 2, -1)
            newhappiness_1 += nfat / 2
        nfat = 1
        chocCount = 0
else:
    pass
time.sleep(0.25)
posCount = 0
for j in range(n):
    for i in range(n):
        if cake[i][j] == 'C':
            chocCount += 1
    if chocCount > 1:
        for i in range(chocCount, chocCount - 2, -1):
            nfat *= i
        variable_3_29 = 2
        newhappiness_1 += Func_newFunc0_29_0(variable_3_29, nfat)
    nfat = 1
    chocCount = 0
print(int(newhappiness_1))
shuffle([74, 2, 91])