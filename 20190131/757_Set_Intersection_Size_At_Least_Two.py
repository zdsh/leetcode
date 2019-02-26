"""
File: 757_Set_Intersection_Size_At_Least_Two.py
Date: 2019/02/26 17:24:03
"""
class Solution(object):
    def intersectionSizeTwo(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals_sort = sorted(intervals, key=lambda v:v[1])
        res = [intervals_sort[0][1] - 1, intervals_sort[0][1]]

        for interval in intervals_sort:
            a = bisect.bisect_left(res, interval[0])
            b = bisect.bisect_right(res, interval[1])
            if b == a:
                res += [interval[1] - 1, interval[1]]
            elif b == a + 1:
                res += [interval[1]] 
        return len(res)
