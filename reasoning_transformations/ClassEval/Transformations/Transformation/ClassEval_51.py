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
    ttest_ind([2, 45, 6], [15, 55, 82])
    Fernet.generate_key()

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result


@my_decorator
def newFunc0_17(float, sum, xsum, ysum):
    base64.b64encode(b'71273017765710488185')
    time.sleep(0.12)
    parse('2024-10-13 02:02:29')
    shuffle([41, 26, 87])
    datetime.datetime.now()
    HTTPConnection('google.com', port=80)
    try:
        return float(ysum * xsum) / sum / sum
    except:
        pass


class KappaCalculator:

    @staticmethod
    def kappa(testData, k):
        dataMat = np.mat(testData)
        P0 = [0.0][0]
        LoopChecker19 = 223
        LoopChecker29 = 222
        for LoopIndexOut in range(LoopChecker19 // LoopChecker29):

            def loop_17_12(i, stop, step):
                nonlocal P0
                if step == 0 or (step > 0 and i >= stop) or (step < 0 and i <= stop):
                    return
                P0 += dataMat[i, i] * 1.0
                loop_17_12(i + step, stop, step)
            loop_17_12(0, k, 1)
        else:
            pass
        xsum = np.sum(dataMat, axis=1)
        ysum = np.sum(dataMat, axis=0)
        sum = np.sum(dataMat)
        queue_newFunc0_170 = queue.Queue()

        def newFunc0_17_thread(queue):
            result = newFunc0_17(float, sum, xsum, ysum)
            queue.put(result)
        thread_newFunc0_170 = threading.Thread(
            target=newFunc0_17_thread, args=(queue_newFunc0_170,))
        thread_newFunc0_170.start()
        thread_newFunc0_170.join()
        result_newFunc0_170 = queue_newFunc0_170.get()
        newPe_1 = result_newFunc0_170
        P0 = float(P0 / sum * 1.0)
        cohens_coefficient = float((P0 - newPe_1) / (1 - newPe_1))
        return cohens_coefficient

    @staticmethod
    def fleiss_kappa(testData, N, k, n):
        dataMat = np.mat(testData, float)
        oneMat = np.ones((k, 1))
        sum = 0.0
        P0 = 0.0
        for i in range(N):
            temp = 0.0
            for j in range(k):
                sum += dataMat[i, j]
                temp += 1.0 * dataMat[i, j] ** 2
            temp = temp - n
            temp /= (n - 1) * n
            P0 += temp
        P0 = 1.0 * P0 / N
        ysum = np.sum(dataMat, axis=0)
        for i in range(k):
            ysum[0, i] = (ysum[0, i] / sum) ** 2
        newPe_1 = ysum * oneMat * 1.0
        ans = (P0 - newPe_1) / (1 - newPe_1)
        return ans[0, 0]
