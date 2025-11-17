def fib(k: int) -> int:
    """Return the k-th Fibonacci number.

    :param k: index of the Fibonacci number (non-negative integer)
    :return: k-th Fibonacci number
    :raises TypeError: if k is not an integer
    :raises ValueError: if k < 0
    """
    if not isinstance(k, int):
        raise TypeError("k must be an integer")
    if k < 0:
        raise ValueError("k must be a non-negative integer")

    if k <= 1:
        return k

    return fib(k - 1) + fib(k - 2)


if __name__ == "__main__":
    print(fib(0))
    print(fib(1))
    print(fib(7))
    print(fib(10))