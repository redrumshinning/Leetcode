def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    x = str(x)
    if len(x) == 0 or len(x) == 1:
        return True
    else:
        if x[0] == x[-1]:
            return isPalindrome(x[1:-1])
        else:
            return False


def isPalindrome2(x):#与第七题解法一样，先反转，多了一步判断，速度比递归快
    """
    :type x: int
    :rtype: bool
    """
    z = x
    y = 0
    while x > 0:
        y = y * 10 + x % 10
        x = x // 10
    return z == y


# faster way
def isPalindrome3(x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0 or (x != 0 and x % 10 == 0):
        return False
    half = 0
    while x > half:
        half = half * 10 + x % 10
        x /= 10
    return x == half or half / 10 == x


print(isPalindrome(12321))
print(isPalindrome2(12321))