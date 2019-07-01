class Solution(object):
    def numDecodings(self, s):
        if not s: return 0
        dp = [0 for i in range(len(s) + 1)]
        dp[0] = 1
        dp[1] = 1 if int(s[0]) != 0 else 0

        for i in range(2, len(s) + 1):
            if int(s[i - 1:i]) != 0:
                dp[i] += dp[i - 1]
            if int(s[i - 2:i]) < 27 and s[i - 2:i][0] != '0':
                dp[i] += dp[i - 2]
        return dp[len(s)]


S = Solution()
print(S.numDecodings('023'))

