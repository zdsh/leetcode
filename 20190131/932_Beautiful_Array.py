"""
File: 932_Beautiful_Array.py
Date: 2019/02/14 14:19:49
"""
class Solution(object):
    def beautifulArray(self, N):
        """
        :type N: int
        :rtype: List[int]
        """
        res = [1]
        while len(res) < N:
            res = [2 * i - 1 for i in res] + [2 * i for i in res]
        return [i for i in res if i <= N]
