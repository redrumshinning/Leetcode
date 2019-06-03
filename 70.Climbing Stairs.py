def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    steps = [1, 2]
    s = [0] * (n + 1)
    s[0] = 1
    for i in range(1,n + 1):
        for j in [c for c in steps if c <= i]:
            s[i] += s[i-j]

    return s[n]

def climbStairs2(n):
    if n == 1: return 1
    res = [0 for i in range(n)]
    res[0], res[1] = 1, 2
    for i in range(2, n):
        res[i] = res[i-1] + res[i-2]
    return res[-1]

def climbStairs3(n):

    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a

print(climbStairs3(5))