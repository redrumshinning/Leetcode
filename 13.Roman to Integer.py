def romanToInt(s):#正序
    """
    :type s: str
    :rtype: int
    """
    d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    ans = 0
    for i in range(len(s)-1):
        first = s[i]
        second = s[i+1]
        if d[first] < d[second]:
            ans = ans - d[first]
        else:
            ans = ans + d[first]

    ans = ans + d[s[-1]]
    return ans

def romanToInt2(self, s):#倒序
    d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    res, p = 0, 'I'
    for c in s[::-1]:
        res, p = res - d[c] if d[c] < d[p] else res + d[c], c
    return res

print(romanToInt("MCMXCIV"))