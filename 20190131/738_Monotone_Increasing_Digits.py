"""
File: 738_Monotone_Increasing_Digits.py
Date: 2019/04/03 22:12:32
"""
class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        strN = list(str(N))
        n = len(strN)
        if all([strN[j] <= strN[j+1] for j in xrange(n-1)]):
            return N
        i = 0
        for i in range(n-1):
            if strN[i] > strN[i+1]:
                j = i
                while j > 0 and ord(strN[j]) == ord(strN[j-1]):
                    j -= 1
                strN[j+1:] = ['9'] * (n-j-1)
                strN[j] = chr(ord(strN[j])-1)
                break
        return int(''.join(strN)) 
