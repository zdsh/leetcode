"""
File: 944_Delete_Columns_to_Make_Sorted.py
Date: 2019/02/15 11:12:54
"""
class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        m, n = len(A), len(A[0])
        ret = 0
        for j in xrange(n):
            i = 0
            while i < m - 1:
                if A[i][j] > A[i + 1][j]:
                    ret += 1
                    break
                i += 1
            
        return ret
