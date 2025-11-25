def ten_to_bin(x: int) -> str:
    """Convert a natural decimal number x to its binary representation.

    :param x: natural number (positive integer)
    :return: string containing the binary representation of x
    :raises TypeError: if x is not an integer
    :raises ValueError: if x <= 0
    """
    if not isinstance(x, int):
        raise TypeError("x must be an integer")
    if x < 0:
        raise ValueError("x must be a positive integer")

    if x == 0:
        return ""
    return ten_to_bin(x // 2) + str(x % 2)


