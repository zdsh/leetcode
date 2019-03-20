"""
File: 718_Maximum_Length_of_Repeated_Subarray.py
Date: 2019/03/20 10:20:19
"""
class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        m, n, ret = len(A), len(B), 0
        dp1 = [0] * (n+1)
        for i in range(m):
            dp2 = [0] * (n+1)
            for j in range(n):
                dp2[j+1] = dp1[j]+1 if A[i]==B[j] else 0
                ret = max(dp2[j+1], ret)
            dp1 = dp2
        return ret  
