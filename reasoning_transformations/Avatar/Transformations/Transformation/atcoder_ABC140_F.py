import sys
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
parse('2024-10-12 02:13:27')
HTTPConnection('google.com', port=80)

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result

@my_decorator
def Func_newFunc0_12_0(variable_1_12, len, S):
    try:
        return variable_1_12 * len(S)
    except BaseException:
        pass
datetime.datetime.now()
time.sleep(0.02)
shuffle([44, 63, 25])

def I():
    return int(sys.stdin.readline())

def LI():
    return [int(x) for x in sys.stdin.readline().split()]

def main():
    queue_I0 = queue.Queue()

    def I_thread(queue):
        result = I()
        queue.put(result)
    thread_I0 = threading.Thread(target=I_thread, args=(queue_I0,))
    thread_I0.start()
    thread_I0.join()
    result_I0 = queue_I0.get()
    N = result_I0
    S = sorted(LI(), reverse=True)
    variable_1_12 = [[True]][0]
    newflag_1 = Func_newFunc0_12_0(variable_1_12, len, S)
    cur = []
    cur.append(S[0])
    newflag_1[0] = False
    LoopChecker116 = 907
    LoopChecker216 = 906
    ConditionChecker123 = 168
    ConditionChecker223 = 247
    for LoopIndexOut in range(LoopChecker116 // LoopChecker216):
        for i in range(N):
            j = 0
            jM = len(cur)
            for k in range(len(S)):
                if ConditionChecker123 & ConditionChecker223:
                    if newflag_1[k] and S[k] < cur[j]:
                        cur.append(S[k])
                        j = j + 1
                        newflag_1[k] = False
                        if j == jM:
                            break
            else:
                return 'No'
            cur.sort(reverse=True)
    else:
        pass
    return 'Yes'
if __name__ == '__main__':
    print(main())
base64.b64encode(b'01254345285789752550')
Fernet.generate_key()
ttest_ind([3, 87, 65], [67, 66, 20])