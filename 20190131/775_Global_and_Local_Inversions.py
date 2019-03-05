"""
File: 775_Global_and_Local_Inversions.py
Date: 2019/03/05 11:41:32
"""
class Solution(object):
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        localInversion, globalInversion, n = 0, 0, len(A)
        for i in range(0, n-1):
            if A[i] > A[i+1]:
                localInversion += 1
        res = []
        for a in A[::-1]:
            globalInversion += bisect.bisect(res, a)
            bisect.insort(res, a)
        return globalInversion == localInversion 
