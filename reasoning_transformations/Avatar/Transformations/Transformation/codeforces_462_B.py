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


def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result


@my_decorator
def Func_newFunc0_3_0(variable_3_3, variable_1_3):
    try:
        return variable_1_3 * variable_3_3
    except BaseException:
        pass


Fernet.generate_key()
(n, k) = map(int, input().split())
datetime.datetime.now()
time.sleep(0.23)
news_1 = input()
variable_1_3 = [[0]][0]
shuffle([12, 27, 8])
variable_3_3 = 26
queue_Func_newFunc0_3_00 = queue.Queue()
parse('2024-10-12 06:16:37')


def Func_newFunc0_3_0_thread(queue):
    result = Func_newFunc0_3_0(variable_3_3, variable_1_3)
    queue.put(result)


thread_Func_newFunc0_3_00 = threading.Thread(
    target=Func_newFunc0_3_0_thread, args=(
        queue_Func_newFunc0_3_00,))
thread_Func_newFunc0_3_00.start()
thread_Func_newFunc0_3_00.join()
result_Func_newFunc0_3_00 = queue_Func_newFunc0_3_00.get()
count = result_Func_newFunc0_3_00
LoopChecker14 = 733
LoopChecker24 = 732


def loop_13_0(LoopIndexOut, stop, step):
    if step == 0 or (
            step > 0 and LoopIndexOut >= stop) or (
            step < 0 and LoopIndexOut <= stop):
        return
    for c in news_1:
        count[ord(c) - ord('A')] += 1
    loop_13_0(LoopIndexOut + step, stop, step)


loop_13_0(0, LoopChecker14 // LoopChecker24, 1)
count.sort(reverse=True)
res = 0
base64.b64encode(b'70648537004993672326')
ConditionChecker112 = 853
ttest_ind([72, 67, 54], [59, 64, 24])
ConditionChecker212 = 93
for i in range(26):
    if ConditionChecker112 & ConditionChecker212:
        if count[i] >= k:
            res += k * k
            print(res)
            exit()
    k -= count[i]
    res += count[i] ** 2
HTTPConnection('google.com', port=80)
print(res)
