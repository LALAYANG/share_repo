from typing import *
def iscube(a):
    a = abs(a)
    return int(round(a ** (1. / 3))) ** 3 == a

iscube(1) 