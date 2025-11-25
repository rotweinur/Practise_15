def count(n: int) -> int:
    """Calculates how many digits are in the decimal representation of the non-negative number n

    :param n: non-negative integer
    :return: number of decimal digits in n
    :raises TypeError: if n is not an int
    :raises ValueError: if n is negative
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    if n < 10:
        return 1

    return 1 + count(n // 10)



