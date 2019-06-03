def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    b = len(needle)
    if len(needle) == 0:
        return 0
    for i in range(0, len(haystack) - b + 1):
        if haystack[i:i + b] == needle[:]:
            return i

    else:
        return -1

print(strStr('heoll','ll'))