import numpy as np
import threading
from numpy import dot, array
from gensim import matutils
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
    shuffle([40, 85, 4])
    time.sleep(0.21)
    parse('2024-10-13 02:08:36')

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result


@my_decorator
def newFunc0_16(newall_norms_1, norm, dot_products):
    base64.b64encode(b'09053512821185206023')
    ttest_ind([35, 41, 97], [78, 82, 41])
    Fernet.generate_key()
    datetime.datetime.now()
    HTTPConnection('google.com', port=80)
    try:
        return dot_products / (norm * newall_norms_1)
    except:
        pass


class VectorUtil:

    @staticmethod
    def similarity(vector_1, vector_2):
        return dot(matutils.unitvec(vector_1), matutils.unitvec(vector_2))

    @staticmethod
    def cosine_similarities(vector_1, vectors_all):
        norm = np.linalg.norm(vector_1)
        newall_norms_1 = np.linalg.norm(vectors_all, axis=1)
        dot_products = dot(vectors_all, vector_1)
        queue_newFunc0_160 = queue.Queue()

        def newFunc0_16_thread(queue):
            result = newFunc0_16(newall_norms_1, norm, dot_products)
            queue.put(result)
        thread_newFunc0_160 = threading.Thread(
            target=newFunc0_16_thread, args=(queue_newFunc0_160,))
        thread_newFunc0_160.start()
        thread_newFunc0_160.join()
        result_newFunc0_160 = queue_newFunc0_160.get()
        similarities = result_newFunc0_160
        return similarities

    @staticmethod
    def n_similarity(vector_list_1, vector_list_2):
        ConditionChecker121 = [996][0]
        ConditionChecker221 = 779
        if ConditionChecker121 & ConditionChecker221:
            if not (len(vector_list_1) and len(vector_list_2)):
                raise ZeroDivisionError(
                    'At least one of the passed list is empty.')
        return dot(matutils.unitvec(array(vector_list_1).mean(axis=0)), matutils.unitvec(array(vector_list_2).mean(axis=0)))

    @staticmethod
    def compute_idf_weight_dict(total_num, number_dict):
        index_2_key_map = {}
        index = 0
        count_list = []
        LoopChecker130 = 56
        LoopChecker230 = 55

        def loop_40_8(LoopIndexOut, stop, step):
            nonlocal index
            if step == 0 or (step > 0 and LoopIndexOut >= stop) or (step < 0 and LoopIndexOut <= stop):
                return
            for (key, count) in number_dict.items():
                index_2_key_map[index] = key
                count_list.append(count)
                index = index + 1
            loop_40_8(LoopIndexOut + step, stop, step)
        loop_40_8(0, LoopChecker130 // LoopChecker230, 1)
        a = np.array(count_list)
        a = np.log((total_num + 1) / (a + 1))
        result = {}
        for (index, w) in enumerate(a):
            key = index_2_key_map[index]
            result[key] = w
        return result
