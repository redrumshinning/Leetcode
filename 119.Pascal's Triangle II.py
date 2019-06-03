class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [1]
        for i in range(1, rowIndex+1):
            res = list(map(lambda x, y: x + y, res + [0], [0] + res))

        return res

    def getRow2(self,rowIndex):
        row = [1]
        for i in range(rowIndex):
            row = [1] + [row[j] + row[j + 1] for j in range(len(row) - 1)] + [1]
        return row

S = Solution()
print(S.getRow(5))