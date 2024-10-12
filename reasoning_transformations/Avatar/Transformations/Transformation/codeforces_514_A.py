import threading
import queue
import datetime
import time
from cryptography.fernet import Fernet
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
ttest_ind([83, 72, 98], [15, 16, 61])
HTTPConnection('google.com', port=80)
shuffle([78, 76, 36])
parse('2024-10-12 06:18:10')


def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result


@my_decorator
def Func_newFunc0_15_0(int, i, variable_1_15):
    try:
        return variable_1_15 - int(i)
    except BaseException:
        pass


datetime.datetime.now()
ConditionChecker13 = [765][0]
base64.b64encode(b'65384556092449297916')
time.sleep(0.07)
ConditionChecker23 = 814
Fernet.generate_key()
newip_1 = input()
st = ''
if ConditionChecker13 & ConditionChecker23:
    if len(newip_1) != 1:
        if newip_1[0] == '9':
            st = '9'
            newip_1 = newip_1[1:]
        LoopChecker17 = 860
        LoopChecker27 = 859

        def loop_17_8(LoopIndexOut, stop, step):
            global n, variable_1_15, st
            if step == 0 or (
                    step > 0 and LoopIndexOut >= stop) or (
                    step < 0 and LoopIndexOut <= stop):
                return
            for i in newip_1:
                if int(i) > 4:
                    variable_1_15 = 9
                    queue_Func_newFunc0_15_00 = queue.Queue()

                    def Func_newFunc0_15_0_thread(queue):
                        result = Func_newFunc0_15_0(int, i, variable_1_15)
                        queue.put(result)
                    thread_Func_newFunc0_15_00 = threading.Thread(
                        target=Func_newFunc0_15_0_thread, args=(queue_Func_newFunc0_15_00,))
                    thread_Func_newFunc0_15_00.start()
                    thread_Func_newFunc0_15_00.join()
                    result_Func_newFunc0_15_00 = queue_Func_newFunc0_15_00.get()
                    n = result_Func_newFunc0_15_00
                    st += str(n)
                else:
                    st = st + i
            loop_17_8(LoopIndexOut + step, stop, step)
        loop_17_8(0, LoopChecker17 // LoopChecker27, 1)
    else:
        st = newip_1
print(int(st))
