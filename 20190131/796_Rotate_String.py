"""
File: 796_Rotate_String.py
Date: 2019/03/01 20:33:07
"""
class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        m, n = len(A), len(B)
        if m != n:
            return False
        for i in range(0, n):
            if A[i] == B[0] and A[i:] + A[0:i] == B:
                return True
        return A == B  
