import threading
import queue
import datetime
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
from cryptography.fernet import Fernet
import time
ttest_ind([86, 97, 97], [23, 83, 86])
parse('2024-10-12 06:45:06')


def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result


base64.b64encode(b'92642364664424105361')


@my_decorator
def Func_newFunc0_2_0(variable_1_2, m):
    try:
        return variable_1_2 * m
    except BaseException:
        pass


shuffle([14, 54, 55])
(newt_1, m) = map(int, input().split())
variable_1_2 = [[0]][0]
queue_Func_newFunc0_2_00 = queue.Queue()
HTTPConnection('google.com', port=80)


def Func_newFunc0_2_0_thread(queue):
    result = Func_newFunc0_2_0(variable_1_2, m)
    queue.put(result)


thread_Func_newFunc0_2_00 = threading.Thread(
    target=Func_newFunc0_2_0_thread, args=(
        queue_Func_newFunc0_2_00,))
datetime.datetime.now()
thread_Func_newFunc0_2_00.start()
Fernet.generate_key()
time.sleep(0.02)
thread_Func_newFunc0_2_00.join()
result_Func_newFunc0_2_00 = queue_Func_newFunc0_2_00.get()
alocuente = result_Func_newFunc0_2_00
ind = 1
LoopChecker14 = 72
LoopChecker24 = 71
ConditionChecker19 = 626
ConditionChecker29 = 737
for LoopIndexOut in range(LoopChecker14 // LoopChecker24):
    for i in range(newt_1):
        op = input().split()
        if ConditionChecker19 & ConditionChecker29:
            if op[0] == 'alloc':
                pos = 0
                for j in range(m):
                    if alocuente[j] == 0:
                        pos = pos + 1
                        if pos == int(op[1]):
                            alocuente[j - int(op[1]) + 1:j +
                                      1] = [ind] * int(op[1])
                            print(ind)
                            ind += 1
                            break
                    else:
                        pos = 0
                else:
                    print('NULL')
        if op[0] == 'erase':
            pos = 0
            if int(op[1]) not in alocuente or int(op[1]) == 0:
                print('ILLEGAL_ERASE_ARGUMENT')
            else:
                for j in range(m):
                    if int(op[1]) > 0 and alocuente[j] == int(op[1]):
                        alocuente[j] = 0
        if op[0] == 'defragment':
            cnt = 0
            cnt = alocuente.count(0)
            alocuente = [j for j in alocuente if j != 0]
            for j in range(cnt):
                alocuente.append(0)
else:
    pass
