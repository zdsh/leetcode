class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)<3:
            return False
        min_v=nums[0]
        mid_v=None
        for i in range(1,len(nums)):
            if nums[i]<=min_v:
                min_v=nums[i]
            else:
                if mid_v==None:
                    mid_v=nums[i]
                else:
                    if mid_v<nums[i]:
                        return True
                    else:
                        mid_v=min(nums[i],mid_v)
        return False
