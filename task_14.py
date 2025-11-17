def numbers(x: int) -> None:
    """Print the digits of a natural number x in reverse order, one per line.

    :param x: natural number (positive integer)
    :raises TypeError: if x is not an integer
    :raises ValueError: if x <= 0
    """
    if not isinstance(x, int):
        raise TypeError("x must be an integer")
    if x <= 0:
        raise ValueError("x must be a positive integer")

    print(x % 10)
    if x // 10 != 0:
        numbers(x // 10)


if __name__ == "__main__":
    numbers(12345)
    print("---")
    numbers(7)