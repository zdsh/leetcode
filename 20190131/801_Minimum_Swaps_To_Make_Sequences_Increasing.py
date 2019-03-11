"""
File: 801_Minimum_Swaps_To_Make_Sequences_Increasing.py
Date: 2019/03/11 20:55:30
"""
class Solution(object):
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        n = len(A)
        dp1, dp2 = [0] * n, [1] * n
        for i in range(1, n):
            dp1[i], dp2[i] = n + 1, n + 1
            if A[i] > A[i-1] and B[i] > B[i-1]:
                dp1[i] = dp1[i-1]
                dp2[i] = dp2[i-1] + 1
            if A[i] > B[i-1] and B[i] > A[i-1]:
                dp1[i] = min(dp1[i], dp2[i-1])
                dp2[i] = min(dp2[i], dp1[i-1] + 1)
        return min(dp1[-1], dp2[-1]) 
