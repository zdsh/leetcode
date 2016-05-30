class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        max_range=1
        ret=0
        i,size=0,len(nums)
        while max_range<=n:
            if i<size and nums[i]<=max_range:
                max_range+=nums[i]
                i+=1
            else:
                ret+=1
                max_range+=max_range
        return ret
