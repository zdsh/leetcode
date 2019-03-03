"""
File: 761_Special_Binary_String.py
Date: 2019/03/03 13:15:51
"""
class Solution(object):
    def makeLargestSpecial(self, S):
        """
        :type S: str
        :rtype: str
        """
        i, count, res = 0, 0, []
        for k, s in enumerate(S):
            count = count + 1 if s == '1' else count - 1
            if count == 0:
                res.append('1' + self.makeLargestSpecial(S[i+1:k]) + '0')
                i = k + 1
        return ''.join(sorted(res)[::-1]) 
