import threading
import sys
import queue
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
base64.b64encode(b'18468231057582356908')
parse('2024-10-12 02:35:13')
HTTPConnection('google.com', port=80)
datetime.datetime.now()

@my_decorator
def Func_solve_0(S: str, T: str, A: int, B: int, U: str):
    try:
        ConditionChecker14 = [339][0]
        ConditionChecker24 = 188
        if ConditionChecker14 & ConditionChecker24:
            if S == U:
                A = A - 1
        if T == U:
            B -= 1
        print(A, B)
        return
    except BaseException:
        pass
ttest_ind([64, 76, 27], [13, 77, 30])

def main():

    def iterate_tokens():
        LoopChecker114 = 707
        LoopChecker214 = 706
        for LoopIndexOut in range(LoopChecker114 // LoopChecker214):
            for newline_1 in sys.stdin:
                for word in newline_1.split():
                    yield word
        else:
            pass
    queue_iterate_tokens0 = queue.Queue()

    def iterate_tokens_thread(queue):
        result = iterate_tokens()
        queue.put(result)
    thread_iterate_tokens0 = threading.Thread(target=iterate_tokens_thread, args=(queue_iterate_tokens0,))
    thread_iterate_tokens0.start()
    thread_iterate_tokens0.join()
    result_iterate_tokens0 = queue_iterate_tokens0.get()
    tokens = result_iterate_tokens0
    S = next(tokens)
    T = next(tokens)
    A = int(next(tokens))
    B = int(next(tokens))
    U = next(tokens)
    Func_solve_0(S, T, A, B, U)
if __name__ == '__main__':
    main()
time.sleep(0.26)
shuffle([46, 85, 77])
Fernet.generate_key()