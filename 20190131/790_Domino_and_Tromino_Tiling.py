"""
File: 790_Domino_and_Tromino_Tiling.py
Date: 2019/03/14 13:28:20
"""
class Solution(object):
    def numTilings(self, N):
        """
        :type N: int
        :rtype: int
        """
        pre3_n, pre2_n, pre1_n = 1, 1, 2
        if N <= 2:
            return N
        n = 2
        for i in range(3, N+1):
            pre1_n = n 
            n = (2 * n + pre3_n) % (10**9+7)
            pre3_n, pre2_n = pre2_n, pre1_n
        return n
