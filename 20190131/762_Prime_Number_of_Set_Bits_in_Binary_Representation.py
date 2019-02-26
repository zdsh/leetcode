"""
File: 762_Prime_Number_of_Set_Bits_in_Binary_Representation.py
Date: 2019/02/26 21:22:26
"""
class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        ret = 0
        for x in range(L, R+1):
            n = sum([v=='1' for v in bin(x)])
            isPrime = True if n != 1 else False
            for i in range(2, int(math.sqrt(n + 1)) + 1):
                if n % i == 0:
                    isPrime = False
                    break
            if isPrime:
                ret += 1
        return ret        
