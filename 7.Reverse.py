def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    sign = 1 if x > 0 else -1
    x = abs(x)
    y = 0
    while x:
        y = y * 10 + x % 10
        x = x // 10

    return y * sign if x <= 0x7fffffff else 0

def reverse2(x):
    x = int(str(x)[::-1]) if x > 0 else -int(str(-x)[::-1])
    return x if x < 2147483648 and x > -2147483648 else 0

x = -321
print(reverse2(x))