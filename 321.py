class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        def pick(num,n):
            ret=[]
            i,size=0,len(num)
            while i<size:
                while len(ret)>0 and num[i]>ret[-1] and size-1-i+len(ret)>=n:
                    del ret[-1]
                if len(ret)<n:
                    ret.append(num[i])
                i+=1
            return ret
        
        def merge(num1,num2):
            return [max(num1,num2).pop(0) for _ in num1+num2]
            
        ret=[]
        for i in range(max(0,k-len(nums2)),min(k,len(nums1))+1):
            num1=pick(nums1,i)
            num2=pick(nums2,k-i)
            ret=max(ret,merge(num1,num2))
        return ret
