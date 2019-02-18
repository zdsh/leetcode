"""
File: 927_Three_Equal_Parts.py
Date: 2019/02/18 16:26:53
"""
class Solution(object):
    def threeEqualParts(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        ret = [-1, -1]
        n = sum([a == 1 for a in A])
        if n % 3 != 0:
            return ret
        if n == 0:
            return [0, len(A) - 1]

        p1, p2, p3, s = 0, 0, 0, 0
        print n
        for i in range(len(A)):
            if A[i] == 1:
                s += 1
                if s == n/3:
                    p1 = i
                elif s == n/3 * 2:
                    p2 = i
                elif s == n:
                    p3 = i
        n = len(A)
        if n - p3 > p2 - p1 or n - p3 > p3 - p2:
            return ret

        a1 = ''.join([str(a) for a in A[0:p1 + n - p3]])
        a2 = ''.join([str(a) for a in A[p1 + n - p3:p2 + n - p3]])
        a3 = ''.join([str(a) for a in A[p2 + n - p3:]])
        if a1[a1.index('1'):] == a2[a2.index('1'):] and a2[a2.index('1'):] == a3[a3.index('1'):]:
            return [p1 + n - p3 - 1, p2 + n - p3]
        return ret        
