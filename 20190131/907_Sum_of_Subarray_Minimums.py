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
        stack = []
        A = A + [0]
        for i in range(0, n+1):
            while stack and A[i] <= A[stack[-1]]:
                cur = stack.pop()
                pre = stack[-1] if stack else -1
                ret += (cur - pre) * A[cur] * (i - cur)
            stack.append(i)
        return ret % (10**9 + 7)
