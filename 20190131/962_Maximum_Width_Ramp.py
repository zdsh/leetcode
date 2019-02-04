"""
File: 962_Maximum_Width_Ramp.py
Date: 2019/02/03 16:06:22
"""
class Solution(object):
    def maxWidthRamp(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res = 0
        sorted_index = sorted(range(0, len(A)), key=A.__getitem__)        
        min_index = len(A)
        for i in sorted_index:
            res = max(res, i - min_index)
            min_index = min(min_index, i)
        return res
