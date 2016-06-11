class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m,n=len(board),len(board[0])
        for i in range(0,m):
            for j in range(0,n):
                c=0
                for r in range(max(0,i-1),min(i+2,m)):
                    for t in range(max(0,j-1),min(j+2,n)):
                        c+=board[r][t]&1
                if board[i][j]==1:
                    if c<3:
                        board[i][j]=3
                    elif c>4:
                        board[i][j]=3
                    else:
                        pass
                else:
                    if c==3:
                        board[i][j]=2
        for i in range(0,m):
            for j in range(0,n):
                if board[i][j]==3:
                    board[i][j]=0
                if board[i][j]==2:
                    board[i][j]=1
