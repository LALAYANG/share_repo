from typing import *


def anti_shuffle(s):
    return ' '.join([''.join(sorted(list(i))) for i in s.split(' ')])

anti_shuffle('Hello World!!!')