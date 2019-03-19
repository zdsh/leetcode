"""
File: 713_Subarray_Product_Less_Than_K.py
Date: 2019/03/19 20:19:57
"""
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pre, s, ret, = -1, 1, 0
        for i in range(len(nums)):
            s = s * nums[i]
            while s >= k and pre < i:
                ret += i - 1 - pre
                pre += 1
                s = s / nums[pre]
        return ret + (len(nums) - 1 - pre) * (len(nums) - pre) / 2
