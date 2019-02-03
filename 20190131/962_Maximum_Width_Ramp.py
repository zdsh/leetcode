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
        res = [0] * len(A)
        for i in range(1, len(A)):
            value = res[i]
            for j in range(0, i):
                if A[i] >= A[j]:
                    value = max(value, i - j)
            res[i] = value
        return max(res)
