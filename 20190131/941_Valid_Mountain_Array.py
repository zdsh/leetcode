"""
File: 941_Valid_Mountain_Array.py
Date: 2019/02/15 11:33:16
"""
class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        
        i, n = 0, len(A)
        if n < 3:
            return False
        while i < n - 1 and A[i] < A[i + 1]:
            i += 1
        if i == 0 or i == n - 1:
            return False
        while i < n - 1 and A[i] > A[i + 1]:
            i += 1
        return i == n - 1
