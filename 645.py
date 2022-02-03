class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [sum(nums)-sum(set(nums)), len(nums)*(len(nums)+1)/2 - sum(set(nums))]
