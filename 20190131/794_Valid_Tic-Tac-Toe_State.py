"""
File: 794_Valid_Tic-Tac-Toe_State.py
Date: 2019/03/13 19:42:47
"""
class Solution(object):
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        def win(board, p):
            ret = 0
            for i in range(3):
                if board[i] == p * 3:
                    ret += 1
        
            for i in range(3):
                if [row[i] for row in board] == [p] * 3:
                    ret += 1
            if [board[i][i] for i in range(3)] == [p] * 3:
                ret += 1
            if [board[i][2-i] for i in range(3)] == [p] * 3:
                ret += 1
            return ret

        num = collections.defaultdict(int)
        for row in board:
            for l in row:
                num[l] += 1
        if not (num['X'] == num['O'] or num['X'] == num['O'] + 1):
            return False

        if win(board, 'O') >= 1 and win(board, 'X') >= 1:
            return False
        if win(board, 'X') >= 1 and num['X'] == num['O']:
            return False
        if win(board, 'O') >= 1 and num['X'] > num['O']: 
            return False
        return True

if __name__ == '__main__':
    solu = Solution()
    board =  ["XOX", "O O", "XOX"]
    board = ["XXX","OOX","OOX"]
    print solu.validTicTacToe(board)
