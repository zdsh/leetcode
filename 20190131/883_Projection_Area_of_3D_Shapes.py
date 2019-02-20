"""
File: 883_Projection_Area_of_3D_Shapes.py
Date: 2019/02/20 20:58:11
"""
class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ret, N = 0, len(grid)
        for i in xrange(N):
            ret += max(grid[i]) + max([v[i] for v in grid])
            for j in xrange(N):
                ret += 1 if grid[i][j] != 0 else 0
        return ret  
