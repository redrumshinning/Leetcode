class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:return []
        row,col = len(matrix),len(matrix[0])
        repeat = [[False] * col for _ in range(row)]
        step_row = [0,1,0,-1]
        step_col = [1,0,-1,0]
        ans = []
        r = c = d = 0
        for _ in range(row*col):
            ans.append(matrix[r][c])
            repeat[r][c] = True
            rr,cc = r+step_row[d],c+step_col[d]
            if 0<=rr<row and 0<=cc<col and not repeat[rr][cc]:
                r,c = rr,cc
            else:
                d = (d+1)%4
                r,c = r+step_row[d],c+step_col[d]
        return ans

    def spiralOrder2(self, matrix):
        return matrix and [*matrix.pop(0)] + self.spiralOrder2([*zip(*matrix)][::-1])

a = [[1,2,3],
     [4,5,6],
     [7,8,9]]
S = Solution()
print(S.spiralOrder2(a))