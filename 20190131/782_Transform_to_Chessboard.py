"""
File: 782_Transform_to_Chessboard.py
Date: 2019/03/15 17:10:56
"""
class Solution(object):
    def movesToChessboard(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        import collections
        n, first, second = len(board), board[0], None
        n_first, n_second, ret_row, ret_col= 0, 0, 0, 0
        for b in board:
            if b == first:
                n_first += 1
            elif second == None:
                second = b
                n_second += 1
            elif b == second:
                n_second += 1
            else:
                return -1
        if abs(n_first - n_second) > 1:
            return -1
        f_counter = collections.Counter(first)
        s_counter = collections.Counter(second)
        if not (f_counter[0] == s_counter[1] and f_counter[0] == s_counter[1] and abs(f_counter[0] - f_counter[1]) <= 1):
            return -1
        for i in range(0, len(first)):
            ret_row += 1 if board[i][0] != i % 2 else 0
            ret_col += 1 if first[i] != i % 2 else 0
        if n_first == n_second:
            ret_row, ret_col = min(ret_row, n - ret_row), min(ret_col, n - ret_col)
        else:
            ret_row = n - ret_row if ret_row % 2 else ret_row
            ret_col = n - ret_col if ret_col % 2 else ret_col
        return (ret_row + ret_col) / 2

if __name__ == '__main__':
    sol = Solution()
    board = [[1,0,1,0,1,0,0,0,1,1,0],[1,0,1,0,1,0,0,0,1,1,0],[0,1,0,1,0,1,1,1,0,0,1],[0,1,0,1,0,1,1,1,0,0,1],[1,0,1,0,1,0,0,0,1,1,0],[0,1,0,1,0,1,1,1,0,0,1],[0,1,0,1,0,1,1,1,0,0,1],[1,0,1,0,1,0,0,0,1,1,0],[1,0,1,0,1,0,0,0,1,1,0],[1,0,1,0,1,0,0,0,1,1,0],[0,1,0,1,0,1,1,1,0,0,1]]
    board = [[0,1,1,0,1,1,1,0,0],[0,1,1,0,1,1,1,0,0],[0,1,1,0,1,1,1,0,0],[1,0,0,1,0,0,0,1,1],[0,1,1,0,1,1,1,0,0],[1,0,0,1,0,0,0,1,1],[0,1,1,0,1,1,1,0,0],[1,0,0,1,0,0,0,1,1],[1,0,0,1,0,0,0,1,1]]
    board = [[0,0,1,0,1,1],[1,1,0,1,0,0],[1,1,0,1,0,0],[0,0,1,0,1,1],[1,1,0,1,0,0],[0,0,1,0,1,1]]
    board = [[0,1,0,1],[1,0,1,0],[1,0,1,0],[0,1,0,1]]
    board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]
    board = [[1,0,0,1,1],[0,1,1,0,0],[1,0,0,1,1],[0,1,1,0,0],[0,1,1,0,0]]
    board = [[1,1,1,1],[1,1,1,1],[0,0,0,0],[0,0,0,0]]
    print sol.movesToChessboard(board)
