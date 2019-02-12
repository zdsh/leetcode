"""
File: 909_Snakes_and_Ladders.py
Date: 2019/02/12 00:07:42
"""
class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        def getPosition(N, n):
           
           if ((n - 1) / N) % 2 == 0:
               return N - 1 - (n - 1) / N, (n - 1) % N
           else:
               return N - 1 - (n - 1) / N, N - 1 - (n - 1) % N

        N =  len(board)
        visited = {}
        state_list, index  = [(1, 0)], 0
        visited[1] = 1
        while index < len(state_list):
           state, step = state_list[index]
           index += 1
           row, col = getPosition(N, state)
           for i in range(1, 7):
               if state + i <= N * N:
                   row, col = getPosition(N, state + i)
                   new_state = state + i
                   if board[row][col] != -1:
                       new_state = board[row][col]
                   if new_state not in visited:
                       if new_state == N * N:
                           return step + 1 
                       state_list.append((new_state, step + 1))
                       visited[new_state] = 1
        return -1


if __name__ == '__main__':
    solution = Solution()
    board = [[1,1,-1],[1,1,1],[-1,1,1]]
    board = [[-1,-1],[-1,3]]
    board = [[-1,1,2,-1],[2,13,15,-1],[-1,10,-1,-1],[-1,6,2,8]]
    print solution.snakesAndLadders(board)
