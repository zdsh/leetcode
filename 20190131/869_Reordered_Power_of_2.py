"""
File: 869_Reordered_Power_of_2.py
Date: 2019/02/22 20:57:23
"""
class Solution(object):
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        n = len(str(N))
        s, res = 1, {}
        res['1'] = 1
        while len(str(s)) <= len(str(N)):
            s *= 2
            res[''.join(sorted(str(s)))] = 1
        return ''.join(sorted(str(N))) in res  
