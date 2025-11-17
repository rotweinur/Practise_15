def mod_number(a: int, b: int) -> int:
    """Return the remainder of dividing a by b.

    :param a: dividend (positive integer)
    :param b: divisor (positive integer)
    :return: remainder of a divided by b
    :raises TypeError: if a or b is not an integer
    :raises ValueError: if a or b are negative
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("a and b must be integers")
    if a < 0 or b < 0:
        raise ValueError("a and b must be non-negative integers")

    if a < b:
        return a

    return mod_number(a - b, b)


if __name__ == "__main__":
    print(mod_number(17, 5))
    print(mod_number(10, 3))
    print(mod_number(25, 25))
