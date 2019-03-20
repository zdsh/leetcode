"""
File: 724_Find_Pivot_Index.py
Date: 2019/03/20 11:29:24
"""
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s, sl, n = sum(nums), 0, len(nums)
        for i in range(0, n):
            if s - nums[i] - sl == sl:
                return i
            sl += nums[i]
        return -1 
