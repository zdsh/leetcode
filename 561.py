class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort() 
        return sum([nums[i] if i%2 == 0 else 0 for i in range(len(nums))])
