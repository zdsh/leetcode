class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        ret = nums[-1]
        for i in range(0, len(nums)-k+1):
            ret = min(ret, nums[i+k-1] - nums[i])
        return ret 
