"""
File: 747_Largest_Number_At_Least_Twice_of_Others.py
Date: 2019/03/28 11:13:12
"""
class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_index, second_value, n = 0, None, len(nums)
        for i in range(1, len(nums)):
            second_value = min(nums[i], nums[max_index]) if second_value == None else max(min(nums[max_index], nums[i]), second_value)
            max_index = i if nums[i] > nums[max_index] else max_index
        return 0 if second_value == None else (max_index if nums[max_index] >= 2*second_value else -1)
