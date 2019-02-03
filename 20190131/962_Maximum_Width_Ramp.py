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
        for i in range(1, len(A)):
            for j in range(0, i - res):
                if A[i] >= A[j]:
                    res = max(res, i - j)
        return res
