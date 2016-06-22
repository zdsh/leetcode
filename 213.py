class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size=len(nums)
        if size==0:
            return 0
        if size==1:
            return nums[0]
        res=[0]*size
        res[0]=nums[0]
        res[1]=max(nums[1],res[0])
        for i in range(2,size-1):
            res[i]=max(res[i-2]+nums[i],res[i-1])
        ret=res[size-2]
        res[0]=0
        res[1]=max(nums[1],res[0])
        for i in range(2,size):
            res[i]=max(res[i-2]+nums[i],res[i-1])
        ret=max(ret,res[size-1])
        return ret
