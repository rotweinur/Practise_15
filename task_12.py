def search(a: list, x: int) -> int:
    """Return 1 if integer x is in the list a, otherwise return 0.

    :param a: list of integers
    :param x: integer to search for
    :return: 1 if x is found, 0 otherwise
    :raises TypeError: if a is not a list or contains non-integers
    """
    if not isinstance(a, list):
        raise TypeError("a must be a list")
    for num in a:
        if not isinstance(num, int):
            raise TypeError("all elements of the list must be integers")
    if not isinstance(x, int):
        raise TypeError("x must be an integer")

    if len(a) == 0:
        return 0

    if a[0] == x:
        return 1

    return search(a[1:], x)



