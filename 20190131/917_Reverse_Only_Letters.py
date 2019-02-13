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
        n = len(S)
        ret = [''] * n
        i, j = 0, n-1
        while i < n:
            if S[i].isalpha():
                while not S[j].isalpha():
                    j -= 1
                ret[j] = S[i]
                j -= 1
            else:
                ret[i] = S[i]
            i += 1
        return ''.join(ret)

