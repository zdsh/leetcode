"""
File: 899_Orderly_Queue.py
Date: 2019/02/18 20:02:07
"""
class Solution(object):
    def orderlyQueue(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        if K >= 2:
            return ''.join(sorted(S))
        n, ret = len(S), S
        if K == 1:
            for i in range(0, len(S)):
                ret = min(ret, S[i:n] + S[0:i])
        return ret  
