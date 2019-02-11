"""
File: 907_Sum_of_Subarray_Minimums.py
Date: 2019/02/11 15:05:15
"""
class Solution(object):
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n, ret = len(A), 0
        record = [0] * n
        for i in range(1, n+1):
            for j in range(0, n + 1 - i):
                v = sum(A[j:j+i])
                if i > 1:
                    v = min(min(record[j], record[j+1]), v)
                record[j] = v
            ret += sum(record[0:n + 1 - i])
        return ret
            
            
