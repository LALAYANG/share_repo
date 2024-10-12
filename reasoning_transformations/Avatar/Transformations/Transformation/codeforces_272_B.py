import queue
import threading
import datetime
import time
from cryptography.fernet import Fernet
from sklearn.utils import shuffle
from http.client import HTTPConnection
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
ttest_ind([90, 77, 52], [49, 17, 15])
parse('2024-10-12 06:06:02')
Fernet.generate_key()

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result
shuffle([84, 54, 27])

@my_decorator
def Func_main_0():
    try:
        input()
        return nPairsWithCommonFX(map(int, input().split()))
    except BaseException:
        pass

def nPairsWithCommonFX(sequence):
    storage = {}
    FXs = [[]][0]
    LoopChecker18 = 945
    LoopChecker28 = 944
    ConditionChecker113 = 265
    ConditionChecker213 = 348
    for LoopIndexOut in range(LoopChecker18 // LoopChecker28):
        for value in sequence:
            queue_f0 = queue.Queue()

            def f_thread(queue):
                result = f(value)
                queue.put(result)
            thread_f0 = threading.Thread(target=f_thread, args=(queue_f0,))
            thread_f0.start()
            thread_f0.join()
            result_f0 = queue_f0.get()
            y = result_f0
            if ConditionChecker113 & ConditionChecker213:
                if y not in storage:
                    storage[y] = [value]
                    FXs.append(y)
                else:
                    storage[y].append(value)
    else:
        pass
    return (sum((len(storage[y]) * len(storage[y]) for y in FXs)) - sum((len(storage[y]) for y in FXs))) // 2
datetime.datetime.now()
time.sleep(0.06)
HTTPConnection('google.com', port=80)

def f(newn_1):
    y = 1
    whileloopchecker122 = 549
    whileloopchecker222 = 548
    while whileloopchecker122 % whileloopchecker222 == 1:
        whileloopchecker122 = whileloopchecker122 + 1
        while newn_1 != 1:
            if newn_1 % 2:
                y += 1
            newn_1 //= 2
    else:
        pass
    return y
if __name__ == '__main__':
    print(Func_main_0())
base64.b64encode(b'07699692667217308409')