"""
File: 779_K-th_Symbol_in_Grammar.py
Date: 2019/03/07 15:35:53
"""
class Solution(object):
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        if N == 1 and K == 1:
            return 0
        ret = 1 if K % 2 == 0 else 0
        while N > 2:
            ret = 1 - ret if K > 2**(N-2) else ret
            K = (K-1) % 2**(N-2) + 1
            N -= 1
        return ret
