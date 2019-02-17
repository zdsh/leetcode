"""
File: 940_Distinct_Subsequences_II.py
Date: 2019/02/17 11:56:55
"""
class Solution(object):
    def distinctSubseqII(self, S):
        """
        :type S: str
        :rtype: int
        """
        n = len(S)
        dp = [0] * n
        dp[0] = 1
        for i in range(1, n):
            j = i - 1
            while j >= 0 and S[i] != S[j]:
                j -= 1
            if j >= 0:
                dp[i] = 2 * dp[i - 1] - dp[j - 1]
            else:
                dp[i] = dp[i - 1] * 2 + 1
        return dp[-1] % (10**9 + 7) 
