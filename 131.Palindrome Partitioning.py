class Solution(object):
    def partition(self, s):
        """
        需要一个path来保存当前循环的回文数
        例如[a,a,b] i = 1 判断a是否是回文，是的话path+[a],再递归[a,b]
                    i = 2 判断aa是否是回文，是的话path+[aa],再递归[b]
                    i = 3 判断aab是否是回文，是的话path+[aab],到此循环结束
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s, path, res):
        if not s:
            res.append(path)
            return
        for i in range(1, len(s) + 1):
            if self.is_Pal(s[:i]):
                self.dfs(s[i:], path + [s[:i]], res)

    def is_Pal(self, s):
        return s == s[::-1]

    def partition2(self, s):
        if not s:
            return [[]]
        dp = {0: [[]], 1: [[s[0]]]}
        for ii in range(1, len(s)):
            dp[ii + 1] = []
            for jj in range(0, ii + 1):
                if self.isPalindrome(s[jj:ii + 1]):
                    for sol in dp[jj]:
                        dp[ii + 1].append(sol + [s[jj:ii + 1]])
        print(dp)
        return dp[len(s)]

    def isPalindrome(self, string):
        return string == string[::-1]
######################################
    def partition3(self, s):#dp
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []

        dp = [[None] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
            else:
                dp[i][i + 1] = False
        for i in range(len(s) - 2, -1, -1):
            for j in range(i + 2, len(s)):
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True

        self.dfs(s, 0, [], res, dp)
        return res

    def dfs(self, s, start_index, partition, res, dp):
        if start_index == len(s):
            res.append(list(partition))
            return

        for i in range(start_index, len(s)):
            if dp[start_index][i]:
                partition.append(s[start_index: i + 1])
                self.dfs(s, i + 1, partition, res, dp)
                partition.pop()

S = Solution()
print(S.partition2('aab'))
