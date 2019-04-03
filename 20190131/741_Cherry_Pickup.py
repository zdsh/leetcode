"""
File: 741_Cherry_Pickup.py
Date: 2019/04/03 16:06:27
"""
class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        dp =[[-1] * n for i in range(m)]
        dp[0][0] = grid[0][0]
        for s in range(1, m+n-1):
            for r1 in range(min(m-1,s), max(0,s-n+1)-1, -1):
                for r2 in range(min(m-1,s), max(0,s-n+1)-1, -1):
                    c1, c2 = s - r1, s - r2
                    if grid[r1][c1] == -1 or grid[r2][c2] == -1:
                        dp[r1][r2] = -1
                        continue
                    v = -1
                    if c1 <= n-1 and c2 <= n-1:
                        v = max(dp[r1][r2], v)
                    if r1 > 0 and r2 > 0:
                        v = max(dp[r1-1][r2-1], v)
                    if r1 > 0 and c2 <= n-1:
                        v = max(dp[r1-1][r2], v)
                    if c1 <= n-1 and r2 > 0:
                        v = max(dp[r1][r2-1], v)
                    if v == -1:
                        dp[r1][r2] = -1
                        continue
                    if r1 == r2:
                        v += 1 if grid[r1][c1] == 1 else 0
                    else:
                        v += 1 if grid[r1][c1] == 1 else 0
                        v += 1 if grid[r2][c2] == 1 else 0
                    dp[r1][r2] = v
        return max(dp[m-1][n-1], 0)        
