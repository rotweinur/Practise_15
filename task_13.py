def odd_list(a: list, n: int) -> list:
    """Return a list of even integers from the first n elements of a list.

    :param a: list of integers
    :param n: number of elements to consider from the list
    :return: list of even integers
    :raises TypeError: if a is not a list or contains non-integers, or n is not an int
    :raises ValueError: if n < 0 or n > len(a)
    """
    if not isinstance(a, list):
        raise TypeError("a must be a list")
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0 or n > len(a):
        raise ValueError("n must be in range 0..len(a)")

    for i in range(n):
        if not isinstance(a[i], int):
            raise TypeError("all elements must be integers")

    if n == 0:
        return []

    rest = odd_list(a, n - 1)
    if a[n - 1] % 2 == 0:
        rest.append(a[n - 1])

    return rest


if __name__ == "__main__":
    print(odd_list([1, 2, 3, 4, 5, 6], 6))
    print(odd_list([7, 11, 14, 20], 4))
    print(odd_list([1, 3, 5], 3))
