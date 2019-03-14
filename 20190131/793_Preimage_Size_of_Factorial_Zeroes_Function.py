"""
File: 793_Preimage_Size_of_Factorial_Zeroes_Function.py
Date: 2019/03/13 21:52:17
"""
class Solution(object):
    def preimageSizeFZF(self, K):
        """
        :type K: int
        :rtype: int
        """
        base, n, coff = 6, K, [1]
        while K > base:
            coff.append(base)
            base = 5 * base + 1

        for base in coff[::-1]:
            if n % base == 0 and n / base == 5:
                return 0
            n = n % base
        return 5 
        
if __name__ =='__main__':
    sol = Solution()
    print sol.preimageSizeFZF(100)
    print sol.preimageSizeFZF(1001)
    print sol.preimageSizeFZF(10003)
