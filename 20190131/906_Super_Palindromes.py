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

        l, r = int(L), int(R)
        i, ret = 1, 0
        while i <= r:
            pali1 = int(str(i) + str(i)[::-1][1:]) 
            res = pali1 * pali1
            if res <= r:
                if res >= l and checkPalindrome(res):
                    ret += 1
            else:
                break
            i += 1 
        i = 1
        while i <= r:
            pali1 = int(str(i) + str(i)[::-1]) 
            res = pali1 * pali1
            if res <= r:
                if res >= l and checkPalindrome(res):
                    ret += 1
            else:
                break
            i += 1 

        return ret 
