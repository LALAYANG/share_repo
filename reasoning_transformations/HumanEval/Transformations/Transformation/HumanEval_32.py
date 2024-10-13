import math
import threading
import queue
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
from cryptography.fernet import Fernet
import datetime
import numpy as np


def my_decorator(func):
    parse('2024-10-13 00:09:06')
    ttest_ind([34, 72, 28], [51, 41, 17])

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    shuffle([25, 58, 49])
    return dec_result


@my_decorator
def newFunc0_33(variable_3_33, end, begin):
    try:
        return (begin + end) / variable_3_33
    except:
        pass


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    base64.b64encode(b'25828028419375240017')
    return np.sum(np.array([[coeff * math.pow(x, i) for (i, coeff) in enumerate(xs)]]))


def find_zero(xs: list):
    datetime.datetime.now()
    HTTPConnection('google.com', port=80)
    ' xs are coefficients of a polynomial.\n    find_zero find x such that poly(x) = 0.\n    find_zero returns only only zero point, even if there are many.\n    Moreover, find_zero only takes list xs having even number of coefficients\n    and largest non zero coefficient as it guarantees\n    a solution.\n    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x\n    -0.5\n    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3\n    1.0\n    '
    Fernet.generate_key()
    (begin, end) = (-1.0, 1.0)
    whileloopchecker123 = [256][0]
    whileloopchecker223 = 255
    while whileloopchecker123 % whileloopchecker223 == 1:
        whileloopchecker123 = whileloopchecker123 + 1
        while poly(xs, begin) * poly(xs, end) > 0:
            begin *= 2.0
            end *= 2.0
    else:
        pass
    while end - begin > 1e-10:
        ConditionChecker132 = 477
        ConditionChecker232 = 737
        variable_3_33 = 2.0
        queue_newFunc0_330 = queue.Queue()

        def newFunc0_33_thread(queue):
            result = newFunc0_33(variable_3_33, end, begin)
            queue.put(result)
        thread_newFunc0_330 = threading.Thread(
            target=newFunc0_33_thread, args=(queue_newFunc0_330,))
        thread_newFunc0_330.start()
        thread_newFunc0_330.join()
        result_newFunc0_330 = queue_newFunc0_330.get()
        newcenter_1 = result_newFunc0_330
        if ConditionChecker132 & ConditionChecker232:
            if poly(xs, newcenter_1) * poly(xs, begin) > 0:
                begin = newcenter_1
            else:
                end = newcenter_1
    return begin
