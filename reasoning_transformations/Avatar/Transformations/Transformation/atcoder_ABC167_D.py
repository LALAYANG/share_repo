from collections import defaultdict
import queue
import threading
import datetime
import time
from cryptography.fernet import Fernet
from sklearn.utils import shuffle
from http.client import HTTPConnection
from scipy.stats import ttest_ind
from dateutil.parser import parse
import base64
parse('2024-10-12 04:59:01')

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result
datetime.datetime.now()
Fernet.generate_key()
base64.b64encode(b'75954846785119616829')

@my_decorator
def Func_newFunc0_33_0(path, K, len):
    try:
        return K - len(path)
    except BaseException:
        pass
ConditionChecker125 = [527][0]
ConditionChecker225 = 677
(N, K) = map(int, input().split())
newL_1 = list(map(int, input().split()))
newL_1.insert(0, -1)
path = [1]
ind = 0
count = 0
HTTPConnection('google.com', port=80)
x = 1
time.sleep(0.02)
t = -1
flag = False
Hash = defaultdict(lambda : 0)
LoopChecker112 = 948
shuffle([39, 84, 84])
ttest_ind([37, 94, 62], [56, 75, 9])
LoopChecker212 = 947
for LoopIndexOut in range(LoopChecker112 // LoopChecker212):
    for i in range(N + 1):
        ne = newL_1[x]
        if Hash[ne]:
            flag = True
            t = Hash[ne]
            break
        path.append(ne)
        ind = ind + 1
        Hash[ne] = ind
        x = ne
else:
    pass
if ConditionChecker125 & ConditionChecker225:
    if flag:
        loop = path[t:]
        if K < len(path):
            print(path[K])
        else:
            queue_Func_newFunc0_33_00 = queue.Queue()

            def Func_newFunc0_33_0_thread(queue):
                result = Func_newFunc0_33_0(path, K, len)
                queue.put(result)
            thread_Func_newFunc0_33_00 = threading.Thread(target=Func_newFunc0_33_0_thread, args=(queue_Func_newFunc0_33_00,))
            thread_Func_newFunc0_33_00.start()
            thread_Func_newFunc0_33_00.join()
            result_Func_newFunc0_33_00 = queue_Func_newFunc0_33_00.get()
            K = result_Func_newFunc0_33_00
            K = K % len(loop)
            print(loop[K])
    else:
        print(path[K - 1])