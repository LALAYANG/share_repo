import queue
import threading
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
time.sleep(0.1)

@my_decorator
def Func_newFunc0_4_0(sa, get_nums, sk, k, newn_1):
    try:
        return get_nums(k, sk) + get_nums(newn_1 - k, sa - sk)
    except BaseException:
        pass

def get_nums(num, t):
    return [t // num + 1 if i in range(t % num) else t // num for i in range(num)]
(newn_1, k, l, r, sa, sk) = map(int, input().split())
queue_Func_newFunc0_4_00 = queue.Queue()
parse('2024-10-12 06:11:01')
HTTPConnection('google.com', port=80)
base64.b64encode(b'10047377909402423108')

def Func_newFunc0_4_0_thread(queue):
    result = Func_newFunc0_4_0(sa, get_nums, sk, k, newn_1)
    queue.put(result)
datetime.datetime.now()
shuffle([40, 65, 12])
ttest_ind([50, 75, 1], [17, 78, 85])
thread_Func_newFunc0_4_00 = threading.Thread(target=Func_newFunc0_4_0_thread, args=(queue_Func_newFunc0_4_00,))
Fernet.generate_key()
thread_Func_newFunc0_4_00.start()
thread_Func_newFunc0_4_00.join()
result_Func_newFunc0_4_00 = queue_Func_newFunc0_4_00.get()
ans = result_Func_newFunc0_4_00
print(' '.join(map(str, ans)))