class Solution(object):
    def uniquePaths(self, m, n):#存储到达每个点的路径个数
        """
        91. Decode Ways
        70. Climbing Stairs
        509. Fibonacci Number
        :type m: int
        :type n: int
        :rtype: int
        """
        aux = [[1 for x in range(n)] for x in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                aux[i][j] = aux[i][j-1]+aux[i-1][j]
                for k in aux:
                    print(k)
                print('#############')
        return aux[-1][-1]

    def uniquePaths2(self, m, n):
        # Approach:
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j - 1] + dp[j]
        return dp[-1] if m and n else 0
    
S = Solution()
print(S.uniquePaths(3,7))