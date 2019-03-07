"""
File: 778_Swim_in_Rising_Water.py
Date: 2019/03/06 22:22:34
"""
class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        dp = [[-1 for j in range(n)] for i in range(n)]
        queue = Queue.PriorityQueue()
        dp[n-1][n-2] = max(grid[n-1][n-2], grid[n-1][n-1])
        queue.put((dp[n-1][n-2], n-1, n-2))
        dp[n-2][n-1] = max(grid[n-2][n-1], grid[n-1][n-1])
        queue.put((dp[n-2][n-1], n-2, n-1))
        while not queue.empty():
            v, r, c = queue.get()
            if r >= 1 and dp[r-1][c] == -1:
                dp[r-1][c] = max(v, grid[r-1][c])
                queue.put((dp[r-1][c], r-1, c))
            if r < n - 1 and dp[r+1][c] == -1:
                dp[r+1][c] = max(v, grid[r+1][c])
                queue.put((dp[r+1][c], r+1, c))
            if c < n - 1 and dp[r][c+1] == -1:
                dp[r][c+1] = max(v, grid[r][c+1])
                queue.put((dp[r][c+1], r, c+1))
            if c >= 1 and dp[r][c-1] == -1:
                dp[r][c-1] = max(v, grid[r][c-1])
                queue.put((dp[r][c-1], r, c-1))
        return dp[0][0]        
