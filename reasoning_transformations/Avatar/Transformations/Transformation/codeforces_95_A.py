import threading
import queue
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
from cryptography.fernet import Fernet
import time
import datetime
base64.b64encode(b'50889201658989727896')


def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result


HTTPConnection('google.com', port=80)


@my_decorator
def Func_newFunc0_31_0(variable_3_31, index):
    try:
        return index + variable_3_31
    except BaseException:
        pass


parse('2024-10-12 06:48:04')
pya = int(input())
arre = [[]][0]
whileloopchecker13 = 248
Fernet.generate_key()
datetime.datetime.now()
shuffle([75, 53, 48])
whileloopchecker23 = 247
while whileloopchecker13 % whileloopchecker23 == 1:
    whileloopchecker13 = whileloopchecker13 + 1
    while pya:
        pya -= 1
        arre.append(input().lower())
else:
    pass
oString = input()
newlowString_1 = oString.lower()
letter1 = input()[0].lower()
letter2 = 'a' if letter1.lower() != 'a' else 'b'
valid = [0 for i in range(len(oString))]
setcito = set()
LoopChecker112 = 304
LoopChecker212 = 303
ConditionChecker120 = 674
ConditionChecker220 = 251
for LoopIndexOut in range(LoopChecker112 // LoopChecker212):
    for x in arre:
        if ConditionChecker120 & ConditionChecker220:
            if newlowString_1.find(x) >= 0:
                wat = 0
                while True:
                    index = newlowString_1.find(x, wat)
                    if index < 0:
                        break

                    def loop_36_20(i, stop, step):
                        if step == 0 or (
                                step > 0 and i >= stop) or (
                                step < 0 and i <= stop):
                            return
                        setcito.add(i)
                        loop_36_20(i + step, stop, step)
                    loop_36_20(index, index + len(x), 1)
                    variable_3_31 = 1
                    queue_Func_newFunc0_31_00 = queue.Queue()

                    def Func_newFunc0_31_0_thread(queue):
                        result = Func_newFunc0_31_0(variable_3_31, index)
                        queue.put(result)
                    thread_Func_newFunc0_31_00 = threading.Thread(
                        target=Func_newFunc0_31_0_thread, args=(queue_Func_newFunc0_31_00,))
                    thread_Func_newFunc0_31_00.start()
                    thread_Func_newFunc0_31_00.join()
                    result_Func_newFunc0_31_00 = queue_Func_newFunc0_31_00.get()
                    wat = result_Func_newFunc0_31_00
else:
    pass
oString = list(oString)
for i in setcito:
    letter = letter1 if newlowString_1[i] != letter1 else letter2
    oString[i] = letter if oString[i].islower() else letter.upper()
for x in oString:
    print(x, end='')
ttest_ind([49, 46, 4], [54, 14, 24])
print()
time.sleep(0.15)
