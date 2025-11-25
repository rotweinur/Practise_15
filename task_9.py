def combin(n: int, k: int) -> int:
    """Return the binomial coefficient C(n, k).

    :param n: non-negative integer
    :param k: integer such that 0 <= k <= n
    :return: binomial coefficient C(n, k)
    :raises TypeError: if n or k is not an integer
    :raises ValueError: if n < 0 or k < 0 or k > n
    """
    if not isinstance(n, int) or not isinstance(k, int):
        raise TypeError("n and k must be integers")
    if n < 0 or k < 0 or k > n:
        raise ValueError("require 0 <= k <= n and n >= 0")

    if k == 0 or k == n:
        return 1

    return combin(n - 1, k - 1) + combin(n - 1, k)



