"""
File: 942_DI_String_Match.py
Date: 2019/02/15 11:49:11
"""
class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        ret = []
        low, high = 0, len(S)
        for s in S:
            if s == 'I':
                ret.append(low)
                low += 1
            if s == 'D':
                ret.append(high)
                high -= 1
        ret.append(low)
        return ret 
