class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n=len(nums)
        if n<=1:
            return n
        i,tag,ret=0,0,1
        pre=nums[i]
        while i<n-1:
            if tag==0:
                if nums[i+1]-nums[i]>0:
                    tag=1
                    ret+=1
                elif nums[i+1]-nums[i]<0:
                    tag=-1
                    ret+=1
            elif tag==1:
                if nums[i+1]<nums[i]:
                    tag=-1
                    ret+=1
            elif tag==-1:
                if nums[i+1]>nums[i]:
                    tag=1
                    ret+=1
            i+=1
        return ret
