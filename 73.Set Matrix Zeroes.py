class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row = []
        col = []
        for _ in range(len(matrix)):
            for _ in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row.append(i)
                    col.append(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in row or j in col:
                    matrix[i][j] = 0

    def setZeroes2(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        MODIFIED = -1000000
        R = len(matrix)
        C = len(matrix[0])
        for r in range(R):
            for c in range(C):
                if matrix[r][c] == 0:
                    # We modify the elements in place. Note, we only change the non zeros to MODIFIED
                    for k in range(C):
                        matrix[r][k] = MODIFIED if matrix[r][k] != 0 else 0#这行除了0都变为MODIFIED，因为0后续还有用
                    for k in range(R):
                        matrix[k][c] = MODIFIED if matrix[k][c] != 0 else 0#这列除了0都变为MODIFIED
        for r in range(R):
            for c in range(C):
                # Make a second pass and change all MODIFIED elements to 0 """
                if matrix[r][c] == MODIFIED:
                    matrix[r][c] = 0
