"""
File: 939_Minimum_Area_Rectangle.py
Date: 2019/02/17 11:31:06
"""
class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        edge_dic = {}
        for p1, p2 in itertools.combinations(points, 2):
            if p1[0] == p2[0] and p1[1] != p2[1]:
                y1, y2 = p1[1], p2[1]
                if y1 > y2:
                    y1, y2 = y2, y1
                if (y1, y2) not in edge_dic:
                    edge_dic[y1, y2] = []
                edge_dic[y1, y2] += [p1[0]]
        ret = float('inf')
        for y1, y2 in edge_dic:
            x_list = sorted(edge_dic[y1, y2])
            for i in xrange(len(x_list) - 1):
                ret = min(ret, (x_list[i + 1] - x_list[i]) * (y2 - y1))
        return 0 if ret == float('inf') else ret
