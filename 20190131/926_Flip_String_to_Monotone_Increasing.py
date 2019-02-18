"""
File: 926_Flip_String_to_Monotone_Increasing.py
Date: 2019/02/17 20:29:19
"""
class Solution(object):
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        n = len(S)
        dp = [0] * n
        i, c = 0, 0
        while i < n:
            if S[i] == '1':
                dp[i] = dp[i - 1]
                c += 1
            else:
                dp[i] = min(dp[i - 1] + 1, c)
        return dp[-1]     
        
