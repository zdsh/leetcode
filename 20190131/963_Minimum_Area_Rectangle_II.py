"""
File: 963_Minimum_Area_Rectangle_II.py
Date: 2019/02/04 10:02:46
"""
class Solution(object):
    def minAreaFreeRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        n = len(N)
        points = set(map(tuple, points))
        ret = 0
        for i in range(0, n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    x = points[k][0] + points[j][0] - points[i][0]
                    y = points[k][1] + points[j][1] - points[i][1]
                    if (x, y) in points:
                        length1 = (points[j][0] - points[i][0])**2 + (points[j][1] - points[i][1])**2
                        length2 = (points[k][0] - points[i][0])**2 + (points[k][1] - points[i][1])**2
                        area = length1**0.5 * length2**0.5
                        ret = max(ret, area)

        return ret        
