from typing import *


def largest_divisor(n: int) -> int:
    for i in reversed(range(n)):
        if n % i == 0:
            return i

largest_divisor(100)