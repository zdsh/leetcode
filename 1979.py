class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_num, max_num = nums[0], nums[0]
        for num in nums:
            min_num = min(num, min_num)
            max_num = max(num, max_num)
        while max_num % min_num != 0:
            max_num, min_num = min_num, max_num % min_num 
        return min_num
