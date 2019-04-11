"""
File: 703_Kth_Largest_Element_in_a_Stream.py
Date: 2019/04/11 20:36:30
"""
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        nums.sort()
        self.nums = nums 
        self.k = k

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        bisect.insort(self.nums, val)
        return self.nums[-1*self.k]       
