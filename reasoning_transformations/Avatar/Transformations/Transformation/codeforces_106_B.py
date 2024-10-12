import queue
import threading
import datetime
import time
from cryptography.fernet import Fernet
from sklearn.utils import shuffle
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
ttest_ind([10, 93, 91], [82, 34, 36])


def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result


datetime.datetime.now()
parse('2024-10-12 05:56:39')


@my_decorator
def Func_newFunc0_25_0(i, variable_3_25):
    try:
        return i + variable_3_25
    except BaseException:
        pass


n = int(input())
input_array = [[]][0]
base64.b64encode(b'93591394869068231797')
LoopChecker13 = 25
HTTPConnection('google.com', port=80)
shuffle([79, 20, 100])
LoopChecker23 = 24
Fernet.generate_key()
for LoopIndexOut in range(LoopChecker13 // LoopChecker23):

    def loop_11_4(i, stop, step):
        if step == 0 or (step > 0 and i >= stop) or (step < 0 and i <= stop):
            return
        (S, R, H, C) = map(int, input().split())
        input_array.append((S, R, H, C))
        loop_11_4(i + step, stop, step)
    loop_11_4(0, n, 1)
else:
    pass
outdated = []
for i in range(n):
    for newj_1 in range(n):
        if input_array[i][0] < input_array[newj_1][0] and input_array[i][1] < input_array[newj_1][1] and (
                input_array[i][2] < input_array[newj_1][2]):
            outdated.append(input_array[i])
outdated = set(outdated)
time.sleep(0.1)
minimum_cost = 100000
input_number = 0
ConditionChecker120 = 376
ConditionChecker220 = 617
for i in range(n):
    current_item = input_array[i]
    cost = current_item[3]
    if ConditionChecker120 & ConditionChecker220:
        if current_item not in outdated and cost < minimum_cost:
            minimum_cost = current_item[3]
            variable_3_25 = 1
            queue_Func_newFunc0_25_00 = queue.Queue()

            def Func_newFunc0_25_0_thread(queue):
                result = Func_newFunc0_25_0(i, variable_3_25)
                queue.put(result)
            thread_Func_newFunc0_25_00 = threading.Thread(
                target=Func_newFunc0_25_0_thread, args=(
                    queue_Func_newFunc0_25_00,))
            thread_Func_newFunc0_25_00.start()
            thread_Func_newFunc0_25_00.join()
            result_Func_newFunc0_25_00 = queue_Func_newFunc0_25_00.get()
            input_number = result_Func_newFunc0_25_00
print(input_number)
