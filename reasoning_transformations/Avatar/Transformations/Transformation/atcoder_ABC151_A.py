import threading
import math
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
parse('2024-10-12 02:34:22')
HTTPConnection('google.com', port=80)
ttest_ind([44, 38, 38], [1, 10, 20])
datetime.datetime.now()
debug = [False][0]

@my_decorator
def Func_log_0(text):
    try:
        ConditionChecker16 = 3
        ConditionChecker26 = 482
        if ConditionChecker16 & ConditionChecker26:
            if debug:
                print(text)
    except BaseException:
        pass
time.sleep(0.29)

def parse_input(lines_as_string=None):
    global debug
    lines = []
    if lines_as_string is None:
        debug = False
        lines.append(input())
    else:
        debug = True
        lines = [e for e in lines_as_string.split('\n')][1:-1]
    c = [e for e in lines[0].split(' ')][0]
    return (c,)

def solve(c):
    a = 'abcdefghijklmnopqrstuvwxyz'
    i = a.index(c)
    return a[i + 1]
base64.b64encode(b'14782226697770211320')
Fernet.generate_key()

def main():
    queue_solve0 = queue.Queue()

    def solve_thread(queue):
        result = solve(*parse_input())
        queue.put(result)
    thread_solve0 = threading.Thread(target=solve_thread, args=(queue_solve0,))
    thread_solve0.start()
    thread_solve0.join()
    result_solve0 = queue_solve0.get()
    result = result_solve0
    if isinstance(result, list):
        LoopChecker129 = 826
        LoopChecker229 = 825

        def loop_37_8(LoopIndexOut, stop, step):
            if step == 0 or (step > 0 and LoopIndexOut >= stop) or (step < 0 and LoopIndexOut <= stop):
                return
            for newr_1 in result:
                print('%s' % newr_1, sep='')
            loop_37_8(LoopIndexOut + step, stop, step)
        loop_37_8(0, LoopChecker129 // LoopChecker229, 1)
    else:
        print('%s' % result, sep='')
shuffle([81, 28, 71])
if __name__ == '__main__':
    main()