"""
File: 902_Numbers_At_Most_N_Given_Digit_Set.py
Date: 2019/02/19 11:52:50
"""
class Solution(object):
    def atMostNGivenDigitSet(self, D, N):
        """
        :type D: List[str]
        :type N: int
        :rtype: int
        """
        m, ret  = len(D), 0
        list_N = list(str(N))
        for i in range(1, len(list_N)):
            ret += m ** i
        i, n = 0, len(list_N)
        while i < len(list_N) and list_N[i] in D:
            low_n = sum([d < list_N[i] for d in D])
            ret += low_n * (m ** (n - 1 - i))
            i += 1
        if i < len(list_N):
            low_n = sum([d < list_N[i] for d in D])
            ret += low_n * (m ** (n - 1 - i))
        else:
            ret += 1

        return ret        
