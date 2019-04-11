"""
File: 696_Count_Binary_Substrings.py
Date: 2019/04/11 21:46:11
"""
class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        c0 = 1 if s[0] == '0' else 0
        c1 = 1 if s[0] == '1' else 0
        i, ret = 1, 0
        while i < len(s):
            if s[i] == '0':
                if s[i] == s[i-1]:
                    c0 += 1
                else:
                    c0 = 1
                ret = ret+1 if c0 <= c1 else ret                
            else:
                if s[i] == s[i-1]:
                    c1 += 1
                else:
                    c1 = 1
                ret = ret+1 if c1 <= c0 else ret
            i += 1
        return ret
