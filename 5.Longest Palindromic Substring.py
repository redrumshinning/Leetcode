class Solution(object):
    def longestPalindrome(self, s):
        """
        分两种情况，循环字符串，求该字符串的前后字符是否相等，得到回文字符串，再判断长度
        :type s: str
        :rtype: str
        """
        res = ""
        for i in range(len(s)):
            # 奇数情况, 如 "aba"
            tmp = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            # 偶数情况, 如 "abba"
            tmp = self.helper(s, i, i + 1)
            if len(tmp) > len(res):
                res = tmp
        return res


    # get the longest palindrome, l, r are the middle indexes
    # from inner to outer
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]

S = Solution()
print(S.longestPalindrome('babad'))