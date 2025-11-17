def comp(a: str, b: str, m: int, n: int) -> int:
    """Return the length of the longest common subsequence (LCS) of strings a and b.

    :param a: first string
    :param b: second string
    :param m: length of the first string
    :param n: length of the second string
    :return: length of the LCS
    :raises TypeError: if a or b is not a string, or m/n not integers
    :raises ValueError: if m or n are negative or inconsistent with string lengths
    """
    if not isinstance(a, str) or not isinstance(b, str):
        raise TypeError("a and b must be strings")
    if not isinstance(m, int) or not isinstance(n, int):
        raise TypeError("m and n must be integers")
    if m < 0 or n < 0 or m > len(a) or n > len(b):
        raise ValueError("invalid lengths m or n")

    if m == 0 or n == 0:
        return 0
    if a[m - 1] == b[n - 1]:
        return 1 + comp(a, b, m - 1, n - 1)
    else:
        return max(comp(a, b, m - 1, n), comp(a, b, m, n - 1))


if __name__ == "__main__":
    print(comp("AGGTAB", "GXTXAYB", 6, 7))
    print(comp("ABC", "AC", 3, 2))
    print(comp("ABCD", "EFGH", 4, 4))
