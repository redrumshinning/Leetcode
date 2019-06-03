def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if not strs:
        return ''
    res = ''
    for i in range(len(strs[0])):
        for j in range(1, len(strs)):
            if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                return res#如果断了，则从这里输出
        res += strs[0][i]
    return res#如果三个字符串完全一样，则从这里输出

def longestCommonPrefix2(strs):
    if not strs:
        return ""

    for i, letter_group in enumerate(zip(*strs)):
        if len(set(letter_group)) > 1:
            return strs[0][:i]
    else:
        return min(strs)#如果第一个字符串比较长，其他的字符串都是它的前缀序列，就必须用min
print(longestCommonPrefix2(["abc","ab","ab"]))