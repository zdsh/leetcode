"""
File: 906_Super_Palindromes.py
Date: 2019/02/11 10:24:10
"""
class Solution(object):
    def superpalindromesInRange(self, L, R):
        """
        :type L: str
        :type R: str
        :rtype: int
        """
        def checkPalindrome(num):
            num = str(num)
            l, r = 0, len(num) - 1
            while l < r:
                if num[l] != num[r]:
                    break
                l += 1
                r -= 1
            if r <= l:
                return True

        l = int(L)
        r = int(R)
        ret = 0
        while l * l <= r:
            if checkPalindrome(l) and checkPalindrome(l * l):
                ret += 1            
            l += 1 
        return ret
