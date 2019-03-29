"""
File: Cracking_the_Safe.py
Date: 2019/03/29 14:42:01
"""
class Solution(object):
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        ret = '0' * n
        visited = set()
        visited.add(ret)
        while len(visited) < k ** n:
            cur = ret[-n+1:] if n > 1 else ''
            for y in range(k-1, -1, -1):
                cur += str(y)
                if cur not in visited:
                    visited.add(cur)
                    ret += str(y)
                    break
        return ret  
