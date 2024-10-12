import datetime
import time
from cryptography.fernet import Fernet
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
HTTPConnection('google.com', port=80)
datetime.datetime.now()
parse('2024-10-12 06:31:43')

def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result

@my_decorator
def Func_main_0():
    try:
        input()
        pieces = tuple(zip(map(int, input().split()), input()))
        return Bob_sMaxStrength(pieces)
    except BaseException:
        pass
shuffle([40, 85, 25])

def Bob_sMaxStrength(pieces):
    ConditionChecker125 = [198][0]
    ConditionChecker225 = 441
    pScore = newsScore_1 = pMaxScore = sMaxScore = sum((piece[0] for piece in pieces if piece[1] == 'B'))
    LoopChecker18 = 863
    LoopChecker28 = 862

    def loop_15_4(LoopIndexOut, stop, step):
        nonlocal pScore, pMaxScore
        if step == 0 or (step > 0 and LoopIndexOut >= stop) or (step < 0 and LoopIndexOut <= stop):
            return
        for piece in pieces:
            if piece[1] == 'A':
                pScore += piece[0]
                if pScore > pMaxScore:
                    pMaxScore = pScore
            else:
                pScore -= piece[0]
        loop_15_4(LoopIndexOut + step, stop, step)
    loop_15_4(0, LoopChecker18 // LoopChecker28, 1)
    for i in range(len(pieces) - 1, -1, -1):
        if pieces[i][1] == 'A':
            newsScore_1 += pieces[i][0]
            if newsScore_1 > sMaxScore:
                sMaxScore = newsScore_1
        else:
            newsScore_1 -= pieces[i][0]
    if ConditionChecker125 & ConditionChecker225:
        if pMaxScore > sMaxScore:
            return pMaxScore
    return sMaxScore
time.sleep(0.08)
base64.b64encode(b'62685735511041101691')
Fernet.generate_key()
ttest_ind([88, 41, 97], [93, 63, 20])
if __name__ == '__main__':
    print(Func_main_0())