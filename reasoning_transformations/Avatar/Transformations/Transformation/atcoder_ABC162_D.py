import math
import queue
import threading
import datetime
import time
from cryptography.fernet import Fernet
from sklearn.utils import shuffle
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
ttest_ind([64, 32, 16], [69, 17, 85])
Fernet.generate_key()

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result
shuffle([24, 78, 12])
base64.b64encode(b'22729236555153738198')

@my_decorator
def Func_newFunc0_21_0(sum, variable_3_21):
    try:
        return sum + variable_3_21
    except BaseException:
        pass
datetime.datetime.now()
N = int(input())
S = input()
parse('2024-10-12 04:51:27')
HTTPConnection('google.com', port=80)
time.sleep(0.14)

def calculate(n, news_1):
    arr = list(news_1)
    rNum = arr.count('R')
    gNum = arr.count('G')
    bNum = arr.count('B')
    sum = [0][0]
    LoopChecker111 = 452
    LoopChecker211 = 451
    ConditionChecker117 = 853
    ConditionChecker217 = 516
    for LoopIndexOut in range(LoopChecker111 // LoopChecker211):
        for step in range(1, math.ceil(n / 2) + 1):
            for i in range(n - 2 * step):
                news_1 = ''.join([arr[i], arr[i + step], arr[i + step * 2]])
                if ConditionChecker117 & ConditionChecker217:
                    if news_1 == 'RGB' or news_1 == 'RBG' or news_1 == 'BGR' or (news_1 == 'BRG') or (news_1 == 'GBR') or (news_1 == 'GRB'):
                        variable_3_21 = 1
                        queue_Func_newFunc0_21_00 = queue.Queue()

                        def Func_newFunc0_21_0_thread(queue):
                            result = Func_newFunc0_21_0(sum, variable_3_21)
                            queue.put(result)
                        thread_Func_newFunc0_21_00 = threading.Thread(target=Func_newFunc0_21_0_thread, args=(queue_Func_newFunc0_21_00,))
                        thread_Func_newFunc0_21_00.start()
                        thread_Func_newFunc0_21_00.join()
                        result_Func_newFunc0_21_00 = queue_Func_newFunc0_21_00.get()
                        sum = result_Func_newFunc0_21_00
    else:
        pass
    print(rNum * gNum * bNum - sum)
calculate(N, S)