"""
File: 773_Sliding_Puzzle.py
Date: 2019/03/04 22:37:22
"""
class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        queue, visited = collections.deque(), {}
        queue.append((tuple(board[0] + board[1]), 0))
        visited[tuple(board[0] + board[1])] = 1

        while queue:
            cur, s = queue.popleft()
            if cur[0:6] == tuple([1, 2, 3, 4, 5, 0]):
                return s
            state = [v for v in cur]
            pos = state.index(0)
            next_states = []
            if pos <= 2:
                state[pos], state[pos+3] = state[pos+3], 0
                next_states.append([v for v in state])
            else:
                state[pos], state[pos-3] = state[pos-3], 0
                next_states.append([v for v in state])
            if pos != 2 and pos != 5:
                state = [v for v in cur]
                state[pos], state[pos+1] = state[pos+1], 0
                next_states.append([v for v in state])
                
            if pos != 0 and pos != 3:
                state = [v for v in cur]
                state[pos], state[pos-1] = state[pos-1], 0
                next_states.append([v for v in state])
            for n_s in next_states:
                if tuple(n_s) not in visited:
                    queue.append((tuple(n_s), s + 1))
                    visited[tuple(n_s)] = 1
        return -1
