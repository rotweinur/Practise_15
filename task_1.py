def pownum(a: float|int, n: int) -> float|int:
    """Elevates the real number a to the natural power n.

    :param a: base (float or int)
    :param n: exponent (natural number or 0)
    :return: a ** n
    :raises TypeError: if n is not an int
    :raises ValueError: if n is negative
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    if n == 0:
        return 1
    if n == 1:
        return a

    if n % 2 == 0:
        half = pownum(a, n // 2)
        return half * half

    return a * pownum(a, n - 1)


if __name__ == "__main__":
    print(pownum(2, 10))  
    print(pownum(5, 0))     
    print(pownum(2.5, 3))   
