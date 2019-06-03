def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    return len(s.rstrip().split(' ')[-1])#默认rstrip删除末尾空格

print(lengthOfLastWord("   "))