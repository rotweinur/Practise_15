def count(a: int, b: int) -> int:
    """Return the number of squares that can be cut from a rectangle of size a x b,
    always cutting the largest possible square.

    :param a: length of the rectangle (positive integer)
    :param b: width of the rectangle (positive integer)
    :return: total number of squares cut
    :raises TypeError: if a or b are not integers
    :raises ValueError: if a < 0 or b < 0
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("a and b must be integers")
    if a < 0 or b < 0:
        raise ValueError("a and b must be non-negative integers")

    if a < b:
        a, b = b, a

    if b == 0:
        return 0

    num_squares = a // b
    remainder = a % b 

    return num_squares + count(b, remainder)


if __name__ == "__main__":
    print(count(5, 3))
    print(count(20, 5))
    print(count(13, 8))