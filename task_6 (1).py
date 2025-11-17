def degree5(n: int) -> int:
    """Return the exponent k such that n = 5^k.

    :param n: positive integer to check
    :return: exponent k if n = 5^k, otherwise -1
    :raises TypeError: if n is not an integer
    :raises ValueError: if n <= 0
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n <= 0:
        raise ValueError("n must be a positive integer")

    if n == 1:
        return 0
    if n % 5 != 0:
        return -1

    sub = degree5(n // 5)
    if sub == -1:
        return -1

    return sub + 1


if __name__ == "__main__":
    print(degree5(1))
    print(degree5(5))
    print(degree5(25))
    print(degree5(125))
    print(degree5(30))