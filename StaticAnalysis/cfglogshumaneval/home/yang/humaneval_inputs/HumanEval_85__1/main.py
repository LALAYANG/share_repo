from typing import *


def add(lst):
    return sum([lst[i] for i in range(1, len(lst), 2) if lst[i] % 2 == 0])

add([4, 4, 6, 8])