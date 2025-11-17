def maxlist(a: list) -> int:
    """Return the maximum element of a list of integers.

    :param a: list of integers (must be non-empty)
    :return: maximum integer in the list
    :raises TypeError: if a is not a list or elements are not integers
    :raises ValueError: if the list is empty
    """
    if not isinstance(a, list):
        raise TypeError("a must be a list")
    if len(a) == 0:
        raise ValueError("list must not be empty")

    for num in a:
        if not isinstance(num, int):
            raise TypeError("all elements must be integers")

    if len(a) == 1:
        return a[0]

    tail_max = maxlist(a[1:])
    return a[0] if a[0] > tail_max else tail_max


if __name__ == "__main__":
    print(maxlist([1, 5, 3, 9, 2]))
    print(maxlist([-4, -1, -7]))
