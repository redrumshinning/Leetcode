class Solution(object):
    def solve(self, board):
        """
        BFS
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board: return
        R, C = len(board), len(board[0])
        queue = []
        for i in range(R):
            for j in range(C):
                if (i in [0, R - 1] or j in [0, C - 1]) and board[i][j] == 'O':
                    queue.append((i, j))
        while queue:
            r, c = queue.pop(0)
            if 0 <= r < R and 0 <= c < C and board[r][c] == 'O':
                board[r][c] = 'N'
                queue.append((r - 1, c))
                queue.append((r + 1, c))
                queue.append((r, c - 1))
                queue.append((r, c + 1))

        for i in range(R):
            for j in range(C):
                if board[i][j] == 'N':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'

    def solve2(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board:
            return board

        rlen = len(board)
        clen = len(board[0])
        for i in range(rlen):
            self.dfs(board, i, 0)
            self.dfs(board, i, clen - 1)
        for j in range(clen):
            self.dfs(board, 0, j)
            self.dfs(board, rlen - 1, j)

        for i in range(rlen):
            for j in range(clen):
                if board[i][j] == 'Y':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'

    def dfs(self, board, i, j):
        row = len(board)
        col = len(board[0])
        if i < 0 or i >= row or j < 0 or j >= col or board[i][j] != 'O':
            return
        board[i][j] = 'Y'
        self.dfs(board, i - 1, j)
        self.dfs(board, i + 1, j)
        self.dfs(board, i, j - 1)
        self.dfs(board, i, j + 1)

board = [['X' ,'X' ,'X' ,'X'],
['X' ,'O' ,'O' ,'X'],
['X' ,'X' ,'O' ,'X'],
['X' ,'O' ,'X' ,'X']]
S = Solution()
S.solve(board)
print(board)

