"""
File: 917_Reverse_Only_Letters.py
Date: 2019/02/13 15:45:11
"""
class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        n, ret = len(S), ''
        for i in range(0, n):
            if S[i].isalpha():
                ret[i] = S[n-1-i]
            else:
                ret[n-1-i] = S[n-1-i]
        return ret

