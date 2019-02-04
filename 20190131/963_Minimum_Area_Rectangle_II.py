"""
File: 963_Minimum_Area_Rectangle_II.py
Date: 2019/02/04 10:02:46
"""
import itertools

class Solution(object):
    def minAreaFreeRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        points = set(map(tuple, points))
        ret = float('inf')
        for p1, p2, p3 in itertools.permutations(points, 3):
            p4 = (p3[0] + p2[0]- p1[0], p3[1] + p2[1]- p1[1])
            if p4 in points:
                if not (p2[0] - p1[0]) * (p3[0] - p1[0]) + (p2[1] - p1[1]) * (p3[1] - p1[1]) : 
                    v1 = (p2[0] - p1[0])**2 + (p2[1] - p1[1])**2
                    v2 = (p3[0] - p1[0])**2 + (p3[1] - p1[1])**2
                    
                    area = v1**0.5 * v2**0.5
                    ret = min(ret, area)
        return ret if ret < float('inf') else 0

if __name__ == '__main__':
    solution = Solution()
    points = [[0,1],[2,1],[1,1],[1,0],[2,0]] 
    points = [[3,1],[1,1],[0,1],[2,1],[3,3],[3,2],[0,2],[2,3]]
    print solution.minAreaFreeRect(points)

