"""
File: 931_Minimum_Falling_Path_Sum.py
Date: 2019/02/17 13:17:01
"""
class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        m, n = len(A), len(A[0])
        dp = [a for a in A[0]] * n

        for r in range(1, m):
            cur_dp = [0] * n
            for c in range(0, n):
                v = dp[c]
                if c > 0:
                    v = min(v, dp[c - 1])
                if c < n - 1:
                    v = min(v, dp[c + 1])
                cur_dp[c] = v + A[r][c]
            dp = cur_dp
        return min(dp)        
