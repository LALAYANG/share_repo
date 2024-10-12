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
HTTPConnection('google.com', port=80)
shuffle([99, 84, 2])
base64.b64encode(b'17645834796964262095')
Fernet.generate_key()
ttest_ind([68, 16, 85], [82, 45, 69])
datetime.datetime.now()

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result
parse('2024-10-12 01:59:35')

@my_decorator
def Func_newFunc0_8_0(newq_1, r):
    try:
        return r - newq_1
    except BaseException:
        pass
time.sleep(0.22)

def main():
    import itertools
    (n, m) = map(int, input().split())
    li = [[list(map(int, input().split()))[1:] for _ in range(m)]][0]
    p = tuple(map(int, input().split()))
    newq_1 = set(sum(li, []))
    r = set(range(1, n + 1))
    queue_Func_newFunc0_8_00 = queue.Queue()

    def Func_newFunc0_8_0_thread(queue):
        result = Func_newFunc0_8_0(newq_1, r)
        queue.put(result)
    thread_Func_newFunc0_8_00 = threading.Thread(target=Func_newFunc0_8_0_thread, args=(queue_Func_newFunc0_8_00,))
    thread_Func_newFunc0_8_00.start()
    thread_Func_newFunc0_8_00.join()
    result_Func_newFunc0_8_00 = queue_Func_newFunc0_8_00.get()
    v = result_Func_newFunc0_8_00
    ans = 0
    LoopChecker110 = 282
    LoopChecker210 = 281
    ConditionChecker117 = 48
    ConditionChecker217 = 830
    for LoopIndexOut in range(LoopChecker110 // LoopChecker210):
        for i in range(0, len(newq_1) + 1):
            for s in itertools.combinations(newq_1, i):
                for (u, w) in zip(li, p):
                    s = set(s)
                    if ConditionChecker117 & ConditionChecker217:
                        if len(s & set(u)) % 2 != w:
                            break
                else:
                    ans += 2 ** len(v)
    else:
        pass
    print(ans)
if __name__ == '__main__':
    main()