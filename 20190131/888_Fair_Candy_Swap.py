"""
File: 888_Fair_Candy_Swap.py
Date: 2019/02/20 21:30:18
"""
class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sum_A = sum(A)
        sum_B = sum(B)
        sub = sum_B - sum_A
        for a in A:
            if a + sub / 2 in set(B):
                return [a, a + sub / 2]
