import threading
import queue
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
from cryptography.fernet import Fernet
import time
import datetime
Fernet.generate_key()
HTTPConnection('google.com', port=80)


def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result


time.sleep(0.16)
base64.b64encode(b'73497919851528213524')


@my_decorator
def Func_newFunc0_17_0(newm_1, q):
    try:
        return newm_1 + q
    except BaseException:
        pass


shuffle([19, 65, 76])
(n, d) = map(int, input().split())
x = [[]][0]
newm_1 = 0
q = 0
x = input().split()
LoopChecker16 = 191
parse('2024-10-12 05:57:24')
LoopChecker26 = 190
for LoopIndexOut in range(LoopChecker16 // LoopChecker26):

    def loop_14_4(i, stop, step):
        if step == 0 or (step > 0 and i >= stop) or (step < 0 and i <= stop):
            return
        x[i] = int(x[i])
        loop_14_4(i + step, stop, step)
    loop_14_4(0, len(x), 1)
else:
    pass
ConditionChecker112 = 230
datetime.datetime.now()
ConditionChecker212 = 782
for a in range(len(x) - 1):
    if ConditionChecker112 & ConditionChecker212:
        if x[a] >= x[a + 1]:
            q = int((x[a] - x[a + 1]) / d + 1)
            queue_Func_newFunc0_17_00 = queue.Queue()

            def Func_newFunc0_17_0_thread(queue):
                result = Func_newFunc0_17_0(newm_1, q)
                queue.put(result)
            thread_Func_newFunc0_17_00 = threading.Thread(
                target=Func_newFunc0_17_0_thread, args=(
                    queue_Func_newFunc0_17_00,))
            thread_Func_newFunc0_17_00.start()
            thread_Func_newFunc0_17_00.join()
            result_Func_newFunc0_17_00 = queue_Func_newFunc0_17_00.get()
            newm_1 = result_Func_newFunc0_17_00
            x[a + 1] = x[a + 1] + q * d
ttest_ind([69, 72, 48], [80, 59, 48])
print(newm_1)
