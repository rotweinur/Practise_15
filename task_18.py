def simmetr(s: str, i: int, j: int) -> bool:
    """Check if the substring of s from index i to j is symmetric (a palindrome).

    :param s: input string
    :param i: starting index (0-based)
    :param j: ending index (0-based)
    :return: True if the substring s[i..j] is symmetric, False otherwise
    :raises TypeError: if s is not a string or i/j are not integers
    :raises ValueError: if i or j are out of bounds
    """
    if not isinstance(s, str):
        raise TypeError("s must be a string")
    if not isinstance(i, int) or not isinstance(j, int):
        raise TypeError("i and j must be integers")
    if i < 0 or j >= len(s):
        raise ValueError("i and j must be valid indices")
    
    if i >= j:  
        return True
    if s[i] != s[j]:
        return False
    return simmetr(s, i + 1, j - 1)


if __name__ == "__main__":
    print(simmetr("racecar", 0, 6))
    print(simmetr("hello", 1, 3))
    print(simmetr("abba", 0, 3)) 
    print(simmetr("abcba", 1, 3))