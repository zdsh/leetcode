class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=0:
            return 0
        len_list=[]
        for i in range(0,len(nums)):
            l=1
            for j in range(0,i):
                if nums[i]>nums[j]:
                    l=max(l,len_list[j]+1)
            len_list.append(l)
        return max(len_list)
