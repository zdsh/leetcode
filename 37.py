class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def getsqure(board,i,j):
            col=i/3
            row=j/3
            ret=[]
            for i in range(col*3,(col+1)*3):
                for j in range(row*3,(row+1)*3):
                    ret.append(board[i][j])
            return ret
            
        def solve(board,i,j):
            m=len(board)
            n=len(board[0])
            origin=board[i][j]
            if board[i][j]=='.':
                cans=[]
                uses=[l for l in board[i]]
                uses+=[b[j] for b in board]
                uses+=getsqure(board,i,j)
                uses=set(uses)
                for l in range(1,10):
                    if str(l) not in uses:
                        cans.append(str(l))
                if len(cans)==0:
                    return False
                for l in cans:
                    board[i][j]=l
                    if j<n-1:
                        ret=solve(board,i,j+1)
                    elif i<m-1:
                        ret=solve(board,i+1,0)
                    else:
                        ret=True
                    if ret:
                        return ret
                    board[i][j]=origin
                return ret
            else:
                if j<n-1:
                    ret=solve(board,i,j+1)
                elif i<m-1:
                    ret=solve(board,i+1,0)
                else:
                    ret=True
                return ret
        solve(board,0,0)
                
