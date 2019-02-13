"""
File: 918_Maximum_Sum_Circular_Subarray.py
Date: 2019/02/13 19:43:17
"""
class Solution(object):
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n, min_a = len(A), min(A)
        if min_a >= 0:
            return sum(A)
        i, b, ret = 0, A.index(min_a), min_a
        while i < n:
            s = 0
            while i < n and s >= 0:
                s += A[(b + i) % n]
                if s >= ret:
                    ret = s
                i += 1
        return ret

if __name__ == '__main__':
    solution = Solution()
    A = [1,-2,3,-2]
    A = [5,-3,5]
    A = [3,-1,2,-1]
    A = [3,-2,2,-3]
    A = [-2,-3,-1]
    print solution.maxSubarraySumCircular(A)
