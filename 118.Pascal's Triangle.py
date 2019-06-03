class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        total = [[1], [1, 1]]
        if numRows == 0:return 0
        if numRows == 1:return total[:1]
        if numRows == 2:return total

        n = 2
        while n < numRows:
            level = [1, 1]
            for i in range(1,n):
                level.insert(i,total[n-1][i-1]+total[n-1][i])
            total.append(level)
            n += 1
        return total
    def generate2(self,numRows):
        pascal = [[1]*(i+1) for i in range(numRows)]
        for i in range(numRows):
            for j in range(1,i):
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
        return pascal

    def generate3(self, numRows):
        res = [[1]]
        for i in range(1, numRows):
            level = list(map(lambda x, y: x + y, res[-1] + [0], [0] + res[-1]))
            res.append(level)
        return res[:numRows]


S = Solution()
print(S.generate3(5))

