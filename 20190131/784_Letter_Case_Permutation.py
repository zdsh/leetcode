"""
File: 784_Letter_Case_Permutation.py
Date: 2019/02/28 22:01:35
"""
class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        i = 0
        while i < len(S) and S[i].isdigit():
            i += 1
        if i >= len(S):
            return [S]
        ret = [ S[0:i] + v + s for v in [S[i].lower(), S[i].upper()] for s in self.letterCasePermutation(S[i+1:])]
        return ret  
