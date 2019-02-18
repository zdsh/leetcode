"""
File: 896_Monotonic_Array.py
Date: 2019/02/18 17:03:18
"""
class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        i, n = 0, len(A)
        while i < n - 1 and A[i] <= A[i + 1]:
            i += 1
        if i >= n - 1:
            return True
        i = 0
        while i < n - 1 and A[i] >= A[i + 1]:
            i += 1
        if i >= n - 1:
            return True
        return False
