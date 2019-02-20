"""
File: 892_Surface_Area_of_3D_Shapes.py
Date: 2019/02/20 19:57:26
"""
class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ret = 0
        N = len(grid)
        for i in xrange(N):
            for j in xrange(N):
                if grid[i][j] != 0:
                    ret += 2
                if j > 0:
                    ret += abs(grid[i][j] - grid[i][j - 1])
                if i > 0:
                    ret += abs(grid[i][j] - grid[i - 1][j])
                if i == 0:
                    ret += grid[i][j]
                if i == N - 1:
                    ret += grid[i][j]
            ret += grid[i][0] + grid[i][-1]
        return ret        
