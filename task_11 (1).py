def ind_maxlist(a: list) -> int:
    """Return the index of the maximum element in a list of integers.

    :param a: list of integers (must be non-empty)
    :return: index of the maximum element
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
        return 0

    idx_tail = ind_maxlist(a[1:])
    idx_tail += 1

    return 0 if a[0] >= a[idx_tail] else idx_tail


if __name__ == "__main__":
    print(ind_maxlist([1, 5, 3, 9, 2]))
    print(ind_maxlist([-4, -1, -7]))
    print(ind_maxlist([10]))
