import queue
import threading
import datetime
import time
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
from cryptography.fernet import Fernet
shuffle([52, 38, 81])
Fernet.generate_key()
time.sleep(0.26)


def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result


HTTPConnection('google.com', port=80)
parse('2024-10-12 06:22:06')
ttest_ind([82, 58, 60], [92, 89, 84])
base64.b64encode(b'65366563019931454755')


@my_decorator
def Func_newFunc0_17_0(s, t):
    try:
        return s + t
    except BaseException:
        pass


def rememberTheNumber(newnums_1, i, operations, ans):
    ConditionChecker12 = [713][0]
    ConditionChecker22 = 450
    if ConditionChecker12 & ConditionChecker22:
        if i >= 3:
            return
    LoopChecker14 = 784
    LoopChecker24 = 783
    for LoopIndexOut in range(LoopChecker14 // LoopChecker24):
        for j in range(4):
            for k in range(j + 1, 4):
                if newnums_1[j] != -1 and newnums_1[k] != -1:
                    s = newnums_1[j]
                    newnums_1[j] = -1
                    t = newnums_1[k]
                    if operations[i] == '+':
                        queue_Func_newFunc0_17_00 = queue.Queue()

                        def Func_newFunc0_17_0_thread(queue):
                            result = Func_newFunc0_17_0(s, t)
                            queue.put(result)
                        thread_Func_newFunc0_17_00 = threading.Thread(
                            target=Func_newFunc0_17_0_thread, args=(queue_Func_newFunc0_17_00,))
                        thread_Func_newFunc0_17_00.start()
                        thread_Func_newFunc0_17_00.join()
                        result_Func_newFunc0_17_00 = queue_Func_newFunc0_17_00.get()
                        newnums_1[k] = result_Func_newFunc0_17_00
                    elif operations[i] == '*':
                        newnums_1[k] = s * t
                    if i == 2 and newnums_1[k] < ans[0]:
                        ans[0] = newnums_1[k]
                    rememberTheNumber(newnums_1, i + 1, operations, ans)
                    newnums_1[j] = s
                    newnums_1[k] = t
    else:
        pass


newnums_1 = list(map(int, input().split()))
operations = list(map(str, input().split()))
ans = [10000000000000000000000000]
rememberTheNumber(newnums_1, 0, operations, ans)
print(ans[0])
datetime.datetime.now()
