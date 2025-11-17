def progress(a1: float|int, r: float|int, n: int) -> float|int:
    """Returns the n-th term of an arithmetic sequence

    :param a1: first term of the progression
    :param r: common difference
    :param n: index of the term (positive integer)
    :return: n-th term of the arithmetic progression
    :raises TypeError: if n is not an integer
    :raises ValueError: if n <= 0
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n <= 0:
        raise ValueError("n must be a positive integer")

    if n == 1:
        return a1

    return progress(a1, r, n - 1) + r


if __name__ == "__main__":
    print(progress(3, 2, 1))
    print(progress(3, -2, 5))
    print(progress(-1, 0.5, 4))
