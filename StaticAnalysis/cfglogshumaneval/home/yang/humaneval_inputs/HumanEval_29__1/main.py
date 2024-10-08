from typing import *


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]

filter_by_prefix(['a', 'ab', 'abc', 'ba', 'bb', 'bc'], 'a')