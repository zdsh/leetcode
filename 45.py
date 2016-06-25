class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n<=1:
            return 0
        ret=1
        i=0
        while i<=n-2:
            if nums[i]+i>=n-1:
                return ret
            else:
                ret+=1
                v,max_j=-1,i
                for j in range(i+1,nums[i]+i+1):
                    if nums[j]+j>=v:
                        v,max_j=nums[j]+j,j
                i=max_j
