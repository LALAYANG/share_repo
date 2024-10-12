import re
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
ttest_ind([75, 26, 18], [95, 65, 59])
shuffle([10, 78, 58])


def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result


@my_decorator
def Func_newFunc0_10_0(variable_3_10, s):
    try:
        return s.strip() + variable_3_10
    except BaseException:
        pass


n = int(input())
base64.b64encode(b'83340622056516666017')
Fernet.generate_key()
time.sleep(0.03)
parse('2024-10-12 06:41:52')
(ans, newsumL_1) = (1, 0)
HTTPConnection('google.com', port=80)
LoopChecker14 = [967][0]
LoopChecker24 = 966
ConditionChecker110 = 988
ConditionChecker210 = 920


def loop_13_0(LoopIndexOut, stop, step):
    global newsumL_1, variable_3_10, L, ans, s
    if step == 0 or (
            step > 0 and LoopIndexOut >= stop) or (
            step < 0 and LoopIndexOut <= stop):
        return
    for s in re.split('[.?!]', input()):
        variable_3_10 = '.'
        queue_Func_newFunc0_10_00 = queue.Queue()

        def Func_newFunc0_10_0_thread(queue):
            result = Func_newFunc0_10_0(variable_3_10, s)
            queue.put(result)
        thread_Func_newFunc0_10_00 = threading.Thread(
            target=Func_newFunc0_10_0_thread, args=(
                queue_Func_newFunc0_10_00,))
        thread_Func_newFunc0_10_00.start()
        thread_Func_newFunc0_10_00.join()
        result_Func_newFunc0_10_00 = queue_Func_newFunc0_10_00.get()
        s = result_Func_newFunc0_10_00
        L = len(s)
        if ConditionChecker110 & ConditionChecker210:
            if L > 1:
                if L > n:
                    print('Impossible')
                    exit()
                if newsumL_1 + L + (newsumL_1 > 0) > n:
                    ans = ans + 1
                    newsumL_1 = L
                else:
                    newsumL_1 = newsumL_1 + L + (newsumL_1 > 0)
    loop_13_0(LoopIndexOut + step, stop, step)


datetime.datetime.now()
loop_13_0(0, LoopChecker14 // LoopChecker24, 1)
print(ans)
