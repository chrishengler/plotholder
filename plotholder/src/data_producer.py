import random


def random_integer_series(length: int, min: int = 0, max: int = 10000) -> list[int]:
    result = list()
    for _ in range(length):
        result.append(random.randint(min, max))
    return result


def random_float_series(length: int, min: float = 0, max: float = 10000) -> list[float]:
    result = list()
    for _ in range(length):
        result.append(random.uniform(min, max))
    return result
