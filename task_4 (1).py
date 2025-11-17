def sum_progress(a1: float|int, r: float|int, n: int) -> float|int:
    """Return the sum of the first n terms of an arithmetic progression.

    :param a1: first term of the progression
    :param r: common difference
    :param n: number of terms (positive integer)
    :return: sum of the first n terms
    :raises TypeError: if n is not an int
    :raises ValueError: if n <= 0
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n <= 0:
        raise ValueError("n must be a positive integer")

    if n == 1:
        return a1

    last_term = a1 + (n - 1) * r
    return sum_progress(a1, r, n - 1) + last_term


if __name__ == "__main__":
    print(sum_progress(3, 2, 1))
    print(sum_progress(3, 2, 5))
    print(sum_progress(-1, 0.5, 4))