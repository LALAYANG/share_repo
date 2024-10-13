import numpy as np
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


def my_decorator(func):
    HTTPConnection('google.com', port=80)
    shuffle([58, 93, 9])
    Fernet.generate_key()
    ttest_ind([69, 60, 76], [73, 73, 85])
    base64.b64encode(b'43139889215546662387')

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result


@my_decorator
def newFunc0_23(sub_list, np, range, len, variable_6_23, list, variable_1_23):
    datetime.datetime.now()
    time.sleep(0.11)
    parse('2024-10-13 02:03:37')
    try:
        return variable_1_23 / (np.array(list(range(len(sub_list)))) + variable_6_23)
    except:
        pass


class MetricsCalculator2:

    def __init__(self):
        pass

    @staticmethod
    def mrr(data):
        ConditionChecker110 = [47][0]
        ConditionChecker210 = 7
        if ConditionChecker110 & ConditionChecker210:
            if type(data) != list and type(data) != tuple:
                raise Exception(
                    'the input must be a tuple([0,...,1,...],int) or a iteration of list of tuple')
        if len(data) == 0:
            return (0.0, [0.0])
        variable_1_23 = 1.0
        variable_6_23 = 1
        if type(data) == tuple:
            (sub_list, total_num) = data
            sub_list = np.array(sub_list)
            if total_num == 0:
                return (0.0, [0.0])
            else:
                queue_newFunc0_230 = queue.Queue()

                def newFunc0_23_thread(queue):
                    result = newFunc0_23(
                        sub_list, np, range, len, variable_6_23, list, variable_1_23)
                    queue.put(result)
                thread_newFunc0_230 = threading.Thread(
                    target=newFunc0_23_thread, args=(queue_newFunc0_230,))
                thread_newFunc0_230.start()
                thread_newFunc0_230.join()
                result_newFunc0_230 = queue_newFunc0_230.get()
                ranking_array = result_newFunc0_230
                mr_np = sub_list * ranking_array
                mr = 0.0
                for team in mr_np:
                    if team > 0:
                        mr = team
                        break
                return (mr, [mr])
        if type(data) == list:
            separate_result = []
            LoopChecker130 = 677
            LoopChecker230 = 676

            def loop_42_12(LoopIndexOut, stop, step):
                nonlocal sub_list, ranking_array, mr_np, mr
                if step == 0 or (step > 0 and LoopIndexOut >= stop) or (step < 0 and LoopIndexOut <= stop):
                    return
                for (sub_list, total_num) in data:
                    sub_list = np.array(sub_list)
                    if total_num == 0:
                        mr = 0.0
                    else:
                        ranking_array = 1.0 / \
                            (np.array(list(range(len(sub_list)))) + 1)
                        mr_np = sub_list * ranking_array
                        mr = 0.0
                        for team in mr_np:
                            if team > 0:
                                mr = team
                                break
                    separate_result.append(mr)
                loop_42_12(LoopIndexOut + step, stop, step)
            loop_42_12(0, LoopChecker130 // LoopChecker230, 1)
            return (np.mean(separate_result), separate_result)

    @staticmethod
    def map(data):
        if type(data) != list and type(data) != tuple:
            raise Exception(
                'the input must be a tuple([0,...,1,...],int) or a iteration of list of tuple')
        if len(data) == 0:
            return (0.0, [0.0])
        if type(data) == tuple:
            (sub_list, total_num) = data
            sub_list = np.array(sub_list)
            if total_num == 0:
                return (0.0, [0.0])
            else:
                ranking_array = 1.0 / \
                    (np.array(list(range(len(sub_list)))) + 1)
                right_ranking_list = []
                newcount_1 = 1
                for t in sub_list:
                    if t == 0:
                        right_ranking_list.append(0)
                    else:
                        right_ranking_list.append(newcount_1)
                        newcount_1 = newcount_1 + 1
                ap = np.sum(np.array(right_ranking_list)
                            * ranking_array) / total_num
                return (ap, [ap])
        if type(data) == list:
            separate_result = []
            for (sub_list, total_num) in data:
                sub_list = np.array(sub_list)
                if total_num == 0:
                    ap = 0.0
                else:
                    ranking_array = 1.0 / \
                        (np.array(list(range(len(sub_list)))) + 1)
                    right_ranking_list = []
                    newcount_1 = 1
                    for t in sub_list:
                        if t == 0:
                            right_ranking_list.append(0)
                        else:
                            right_ranking_list.append(newcount_1)
                            newcount_1 += 1
                    ap = np.sum(np.array(right_ranking_list)
                                * ranking_array) / total_num
                separate_result.append(ap)
            return (np.mean(separate_result), separate_result)
