def add(a: int, b: int) -> int:
    """
    Day la ham tinh tong hai so nguyen
    :param a:
    :param b:
    :return: a+b
    """
    result = a + b
    return result


def add_float(c: float, d: float) -> float:
    return c + d


def compare_two_number_int(a: int, b: int) -> None:
    if a > b:
        print(f'{a} is greater than {b}')
    elif a < b:
        print(f'{b} is greater than {b}')
    else:
        print(f'{a} equals {b}')
