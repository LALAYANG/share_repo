from typing import *


def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_number = min(numbers)
    max_number = max(numbers)
    return [(x - min_number) / (max_number - min_number) for x in numbers]

rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])