"""
File: 704_Binary_Search.py
Date: 2019/04/11 20:27:29
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] == target:
                return mid
            left = mid + 1 if nums[mid] < target else left
            right = mid - 1 if nums[mid] > target else right
        return -1        
