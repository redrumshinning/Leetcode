class Solution(object):
    def isValidSudoku(self, board):
        """
        暴力解，分别求行列正方形中的数字是否符合条件
        :type board: List[List[str]]
        :rtype: bool
        """
        return (self.is_row_valid(board) and
                self.is_col_valid(board) and
                self.is_square_valid(board))

    def is_row_valid(self, board):
        for row in board:
            if not self.is_uint_valid(row):
                return False
        return True

    def is_col_valid(self, board):
        for col in zip(*board):
            if not self.is_uint_valid(col):
                return False
        return True

    def is_square_valid(self, board):
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not self.is_uint_valid(square):
                    return False
        return True

    def is_uint_valid(self, nums):
        uint = [i for i in nums if i != '.']
        return len(uint) == len(set(uint))

    ###########下面两种方法一样，都是空间换时间##############
    def isValidSudoku2(self, board):
        dic_row = [{},{},{},{},{},{},{},{},{}]
        dic_col = [{},{},{},{},{},{},{},{},{}]
        dic_cell = [{},{},{},{},{},{},{},{},{}]

        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == '.':
                    continue
                if board[i][j] not in dic_row[i] and board[i][j] not in dic_col[j] and board[i][j] not in dic_cell[3*(i//3)+(j//3)]:
                    dic_row[i][board[i][j]] = 1
                    dic_col[j][board[i][j]] = 1
                    dic_cell[3*(i//3)+(j//3)][board[i][j]] = 1
                else:
                    return False
        return True

#######################################
    def isValidSudoku3(self, board):
        Cell = [[] for i in range(9)]  # 没有必要用dict,我们只某个数字关心有没有出现过
        Col = [[] for i in range(9)]
        Row = [[] for i in range(9)]

        for i, row in enumerate(board):  # 将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中
            for j, num in enumerate(row):
                if num != '.':
                    k = (i // 3) * 3 + j // 3
                    if num in Row[i] + Col[j] + Cell[k]:  # list的骚操作,将三个list顺序的拼接
                        return False
                    Row[i].append(num)
                    Col[j].append(num)
                    Cell[k].append(num)

        return True
