def _is_prime(n: int, divisor: int) -> bool:
    """Helper function to determine if n is prime by checking divisibility.

    :param n: natural number to check
    :param divisor: current divisor to test
    :return: True if n is prime, False otherwise
    """
    if divisor == 1:
        return True 
    if n % divisor == 0:
        return False  
    return _is_prime(n, divisor - 1)


def function1(x: int) -> int:
    """Determine if a natural number x is prime.

    :param x: natural number (positive integer)
    :return: 1 if x is prime, 0 otherwise
    :raises TypeError: if x is not an integer
    :raises ValueError: if x <= 0
    """
    if not isinstance(x, int):
        raise TypeError("x must be an integer")
    if x <= 0:
        raise ValueError("x must be a positive integer")

    if x == 1:
        return 0

    return 1 if _is_prime(x, x - 1) else 0

