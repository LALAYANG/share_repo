from typing import *


def sum_squares(lst):
    import math
    squared = 0
    for i in lst:
        squared += math.ceil(i)**2
    return squared

sum_squares([-2.4,1,1])