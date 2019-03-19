"""
File: 712_Minimum_ASCII_Delete_Sum_for_Two_Strings.py
Date: 2019/03/19 19:14:40
"""
class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        m, n = len(s1), len(s2)
        dp1, dp2 = [0] * (n + 1), [0] * (n + 1)
        for j in range(n):
            dp1[j+1] = dp1[j] + ord(s2[j])
        for i in range(m):
            dp2 = [0] * (n + 1)
            dp2[0] = dp1[0] + ord(s1[i])
            for j in range(n):
                if s1[i] == s2[j]:
                    dp2[j+1] = dp1[j]
                else:
                    dp2[j+1] = min(dp1[j] + ord(s1[i]) + ord(s2[j]), dp1[j+1] + ord(s1[i]))
                    dp2[j+1] = min(dp2[j+1], dp2[j] + ord(s2[j]))
            dp1 = dp2
        return dp2[n]        
