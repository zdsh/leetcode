class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        size=len(nums)
        i=size-1
        while i>0 and nums[i-1]>=nums[i]:
            i-=1
        if i==0:
            j=0
            while i+j<=(i+size-1)/2:
                nums[i+j],nums[size-1-j]=nums[size-1-j],nums[i+j]
                j+=1
        else:
            j=size-1
            while nums[j]<=nums[i-1]:
                j-=1
            nums[i-1],nums[j]=nums[j],nums[i-1]
            j=0
            while i+j<=(i+size-1)/2:
                nums[i+j],nums[size-1-j]=nums[size-1-j],nums[i+j]
                j+=1
