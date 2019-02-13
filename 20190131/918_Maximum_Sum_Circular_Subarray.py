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
        cur_max = 0
        max_sum = A[0]
        cur_min = 0
        min_sum = A[0]
        for a in A:
            cur_max = max(cur_max + a, a)
            max_sum = max(max_sum, cur_max)
            cur_min = min(cur_min + a, a)
            min_sum = min(min_sum, cur_min)
        return max(max_sum, sum(A) - min_sum) if max_sum > 0 else max_sum

if __name__ == '__main__':
    solution = Solution()
    A = [1,-2,3,-2]
    #A = [5,-3,5]
    #A = [3,-1,2,-1]
    A = [3,-2,2,-3]
    #A = [-2,-3,-1]
    #A = [-1,3,-3,9,-6,8,-5,-5,-6,10]
    A = [-9,14,24,-14,12,18,-18,-10,-10,-23,-2,-23,11,12,18,-9,9,-29,12,4,-8,15,11,-12,-16,-9,19,-12,22,16]
    print solution.maxSubarraySumCircular(A)
