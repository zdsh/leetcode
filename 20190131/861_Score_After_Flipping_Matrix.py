"""
File: 861_Score_After_Flipping_Matrix.py
Date: 2019/02/22 13:55:47
"""
class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        m, n = len(A), len(A[0])

        for i in range(m):
            if A[i][0] == 0:
                A[i] = [int(v==0) for v in A[i]]

        for j in range(1, n):
            if sum([A[i][j] for i in xrange(m)]) >= (m + 1) / 2:
                continue
            for i in xrange(m):
                A[i][j] = int(A[i][j] == 0)
        ret = 0
        for a in A:
            print a
            ret += int(''.join([str(v) for v in a]), 2)
        return ret        
