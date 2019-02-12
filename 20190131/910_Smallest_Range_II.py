"""
File: 910_Smallest_Range_II.py
Date: 2019/02/12 10:44:48
"""
class Solution(object):
    def smallestRangeII(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A.sort()
        ret = A[-1] - A[0]
        for i in range(0, len(A) - 1):
            mina = min(A[0] + K, A[i+1] - K)
            maxa = max(A[i] + K, A[-1] - K)
            ret = min(ret, maxa - mina)
        return ret
