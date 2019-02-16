"""
File: 955_Delete_Columns_to_Make_Sorted_II.py
Date: 2019/02/16 03:33:44
"""
class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        m, n = len(A), len(A[0])
        is_sorted = [0] * n
        ret = 0
        for i in xrange(n):
            for j in range(0, m - 1):
                if A[j][i] > A[j + 1][i] and is_sorted[j] == 0:
                    ret += 1
                    break
                elif is_sorted[j] == 0:
                    is_sorted[j] = 1 if A[j][i] < A[j + 1][i]
        return ret
