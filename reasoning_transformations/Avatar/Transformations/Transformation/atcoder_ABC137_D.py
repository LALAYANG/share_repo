import heapq
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
shuffle([24, 93, 66])
Fernet.generate_key()
ttest_ind([72, 75, 83], [56, 33, 72])

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result
base64.b64encode(b'93619627851277912742')

@my_decorator
def Func_newFunc0_19_0(len, m, y):
    try:
        return m - len(y)
    except BaseException:
        pass
parse('2024-10-12 02:09:28')
(newn_1, m) = map(int, input().split())
x = [[]][0]
y = []
LoopChecker15 = 521
time.sleep(0.24)
LoopChecker25 = 520
for LoopIndexOut in range(LoopChecker15 // LoopChecker25):
    for i in range(newn_1):
        (day, salary) = map(int, input().split())
        heapq.heappush(x, (-day, -salary))
else:
    pass
whileloopchecker111 = 784
whileloopchecker211 = 783
datetime.datetime.now()
HTTPConnection('google.com', port=80)
while whileloopchecker111 % whileloopchecker211 == 1:
    whileloopchecker111 = whileloopchecker111 + 1
    while x:
        ConditionChecker118 = 629
        ConditionChecker218 = 489
        (d, s) = heapq.heappop(x)
        queue_Func_newFunc0_19_00 = queue.Queue()

        def Func_newFunc0_19_0_thread(queue):
            result = Func_newFunc0_19_0(len, m, y)
            queue.put(result)
        thread_Func_newFunc0_19_00 = threading.Thread(target=Func_newFunc0_19_0_thread, args=(queue_Func_newFunc0_19_00,))
        thread_Func_newFunc0_19_00.start()
        thread_Func_newFunc0_19_00.join()
        result_Func_newFunc0_19_00 = queue_Func_newFunc0_19_00.get()
        r = result_Func_newFunc0_19_00
        if ConditionChecker118 & ConditionChecker218:
            if r >= -d:
                heapq.heappush(y, -s)
            else:
                heapq.heappush(y, -s)
                heapq.heappop(y)
else:
    pass
print(sum(y))