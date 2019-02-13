"""
File: 915_Partition_Array_into_Disjoint_Intervals.py
Date: 2019/02/13 16:25:21
"""
class Solution(object):
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ret = 0
        min_a = min(A)
        sep = A.index(min_a)
        max_left, min_right = max(A[0:sep + 1]), min(A[sep + 1:])
        while max_left > min_right:
            new_sep = A[sep + 1:].index(min_right) + sep + 1
            max_left = max(max_left, max(A[sep + 1:new_sep + 1]))
            min_right = min(A[new_sep + 1:])
            sep = new_sep
        return sep + 1

if __name__ == '__main__':
    solution = Solution()
    A = [5,0,3,8,6]
    A = [1,1,1,0,6,12]
    print solution.partitionDisjoint(A)
