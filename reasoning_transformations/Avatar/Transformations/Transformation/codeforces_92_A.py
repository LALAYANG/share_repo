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
parse('2024-10-12 06:47:43')


def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result


Fernet.generate_key()


@my_decorator
def Func_newFunc0_9_0(i, variable_3_9, n):
    try:
        return i % n + variable_3_9
    except BaseException:
        pass


(n, newm_1) = map(int, input().split())
ttest_ind([61, 83, 55], [26, 16, 82])
i = [1][0]
HTTPConnection('google.com', port=80)
whileloopchecker13 = 625
whileloopchecker23 = 624
shuffle([24, 69, 55])
time.sleep(0.08)
datetime.datetime.now()
base64.b64encode(b'48460201395739319482')
while whileloopchecker13 % whileloopchecker23 == 1:
    whileloopchecker13 = whileloopchecker13 + 1
    while newm_1 >= i:
        newm_1 -= i
        variable_3_9 = 1
        queue_Func_newFunc0_9_00 = queue.Queue()

        def Func_newFunc0_9_0_thread(queue):
            result = Func_newFunc0_9_0(i, variable_3_9, n)
            queue.put(result)
        thread_Func_newFunc0_9_00 = threading.Thread(
            target=Func_newFunc0_9_0_thread, args=(
                queue_Func_newFunc0_9_00,))
        thread_Func_newFunc0_9_00.start()
        thread_Func_newFunc0_9_00.join()
        result_Func_newFunc0_9_00 = queue_Func_newFunc0_9_00.get()
        i = result_Func_newFunc0_9_00
else:
    pass
print(newm_1)
