from typing import *


def unique(l: list):
    return sorted(list(set(l)))

unique(['a', 'b', 'b', 'c', 'd', 'd'])