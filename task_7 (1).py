def nod(a: int, b: int) -> int:
    """Return the greatest common divisor (GCD) of two positive integers.

    :param a: first positive integer
    :param b: second positive integer
    :return: greatest common divisor of a and b
    :raises TypeError: if a or b is not an integer
    :raises ValueError: if a or b are negative
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("a and b must be integers")
    if a < 0 or b < 0:
        raise ValueError("a and b must be non-negative integers")

    if b == 0:
        return a

    return nod(b, a % b)


if __name__ == "__main__":
    print(nod(24, 18))
    print(nod(15, 5))
    print(nod(17, 31))