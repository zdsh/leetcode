"""
File: 908_Smallest_Range_I.py
Date: 2019/02/11 21:24:57
"""
class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        min_a = min(A)
        max_a = max(A)
        if max_a - min_a <= 2 * K:
            return 0
        else:
            return max_a - min_a - 2 * K
