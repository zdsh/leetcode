"""
File: 867_Transpose_Matrix.py
Date: 2019/02/22 14:35:21
"""
class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return [[A[r][c] for r in xrange(len(A))] for c in xrange(len(A[0]))]
