"""
File: 697_Degree_of_an_Array.py
Date: 2019/04/11 22:02:12
"""
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right, count = {}, {}, {}
        for i, v in enumerate(nums):
            if v not in left.keys():
                 left[v] = i
            right[v] = i
            if v not in count:
                 count[v] = 0
            count[v] += 1
        maxCount = max(count.values())
        ret = len(nums)
        for v in count:
            if count[v] == maxCount:
                ret = min(ret, right[v] - left[v] + 1)
        return ret
