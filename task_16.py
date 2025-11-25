def ten_to_n(x: int, n: int) -> str:
    """Convert a natural decimal number x to its representation in base n.

    :param x: natural number (positive integer)
    :param n: base (integer from 2 to 16)
    :return: string containing the representation of x in base n
    :raises TypeError: if x or n is not an integer
    :raises ValueError: if x < 0 or n not in range 2..16
    """
    if not isinstance(x, int) or not isinstance(n, int):
        raise TypeError("x and n must be integers")
    if x < 0:
        raise ValueError("x must be a non-negative integer")
    if n < 2 or n > 16:
        raise ValueError("base n must be in range 2..16")

    digits = "0123456789ABCDEF"
    
    if x == 0:
        return ""
    return ten_to_n(x // n, n) + digits[x % n]

