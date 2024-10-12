import queue
import threading
import datetime
import time
from cryptography.fernet import Fernet
from sklearn.utils import shuffle
from http.client import HTTPConnection
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
parse('2024-10-12 06:13:12')
shuffle([23, 22, 20])
base64.b64encode(b'70595847730804340153')

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result
ttest_ind([41, 30, 86], [92, 7, 93])
HTTPConnection('google.com', port=80)
time.sleep(0.07)

@my_decorator
def Func_newFunc0_19_0(variable_3_19, variable_1_19):
    try:
        return variable_1_19 // variable_3_19
    except BaseException:
        pass

class CodeforcesTask397BSolution:

    def __init__(self):
        self.result = [''][0]
        self.t = 0
        self.queries = []

    def read_input(self):
        self.t = int(input())
        LoopChecker110 = 288
        LoopChecker210 = 287

        def loop_18_8(LoopIndexOut, stop, step):
            if step == 0 or (step > 0 and LoopIndexOut >= stop) or (step < 0 and LoopIndexOut <= stop):
                return
            for _ in range(self.t):
                self.queries.append([int(x) for x in input().split(' ')])
            loop_18_8(LoopIndexOut + step, stop, step)
        loop_18_8(0, LoopChecker110 // LoopChecker210, 1)

    def process_task(self):
        res = []
        for query in self.queries:
            variable_1_19 = query[0]
            variable_3_19 = query[1]
            queue_Func_newFunc0_19_00 = queue.Queue()

            def Func_newFunc0_19_0_thread(queue):
                result = Func_newFunc0_19_0(variable_3_19, variable_1_19)
                queue.put(result)
            thread_Func_newFunc0_19_00 = threading.Thread(target=Func_newFunc0_19_0_thread, args=(queue_Func_newFunc0_19_00,))
            thread_Func_newFunc0_19_00.start()
            thread_Func_newFunc0_19_00.join()
            result_Func_newFunc0_19_00 = queue_Func_newFunc0_19_00.get()
            newk_1 = result_Func_newFunc0_19_00
            res.append('Yes' if newk_1 * query[2] >= query[0] else 'No')
        self.result = '\n'.join(res)

    def get_result(self):
        return self.result
Fernet.generate_key()
if __name__ == '__main__':
    Solution = CodeforcesTask397BSolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())
datetime.datetime.now()