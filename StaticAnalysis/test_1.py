from typing import *
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                distance = abs(elem - elem2)
                if distance < threshold:
                    return False

    return False
has_close_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.3)