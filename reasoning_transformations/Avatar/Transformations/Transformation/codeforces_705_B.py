import sys
import threading
import queue
import datetime
import time
from cryptography.fernet import Fernet
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
shuffle([55, 93, 76])
ttest_ind([13, 17, 82], [37, 53, 52])
base64.b64encode(b'83347693700541705817')
HTTPConnection('google.com', port=80)


def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result


@my_decorator
def Func_newFunc0_16_0(c, variable_1_16):
    try:
        return variable_1_16 - c
    except BaseException:
        pass


datetime.datetime.now()
input = sys.stdin.readline
n = int(input())
w = list(map(int, input().split()))
c = [2][0]
LoopChecker16 = 230
LoopChecker26 = 229
ConditionChecker110 = 254
ConditionChecker210 = 527


def loop_15_0(LoopIndexOut, stop, step):
    global variable_1_16, c
    if step == 0 or (
            step > 0 and LoopIndexOut >= stop) or (
            step < 0 and LoopIndexOut <= stop):
        return
    for newi_1 in w:
        if ConditionChecker110 & ConditionChecker210:
            if newi_1 == 1:
                print(c)
            elif newi_1 % 2 == 0:
                variable_1_16 = 3
                queue_Func_newFunc0_16_00 = queue.Queue()

                def Func_newFunc0_16_0_thread(queue):
                    result = Func_newFunc0_16_0(c, variable_1_16)
                    queue.put(result)
                thread_Func_newFunc0_16_00 = threading.Thread(
                    target=Func_newFunc0_16_0_thread, args=(
                        queue_Func_newFunc0_16_00,))
                thread_Func_newFunc0_16_00.start()
                thread_Func_newFunc0_16_00.join()
                result_Func_newFunc0_16_00 = queue_Func_newFunc0_16_00.get()
                c = result_Func_newFunc0_16_00
                print(c)
            else:
                print(c)
    loop_15_0(LoopIndexOut + step, stop, step)


Fernet.generate_key()
parse('2024-10-12 06:41:29')
loop_15_0(0, LoopChecker16 // LoopChecker26, 1)
time.sleep(0.16)
