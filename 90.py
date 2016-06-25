class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret=[]
        n=len(nums)
        nums.sort()
        for i in range(0,2**n):
            v=[]
            for j in range(0,n):
                if (i>>j)&1==1:
                    v.append(nums[j])
            if v not in ret:
                ret.append(v)
        return ret
