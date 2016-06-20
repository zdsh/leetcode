'''
class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<2:
            return 0
        A=min(nums)
        B=max(nums)
        bucket_range=max(1,int((B-A-1)/(len(nums)-1))+1)
        bucket_len=(B-A)/bucket_range+1
        buckets=[None]*bucket_len
        for num in nums:
            loc=(num-A)/bucket_range
            bucket=buckets[loc]
            if bucket==None:
                buckets[loc]=[num,num]
            else:
                bucket[0]=min(bucket[0],num)
                bucket[1]=max(bucket[1],num)
        ret=0
        x=0
        while x<bucket_len-1:
            if buckets[x] is None:
                continue
            y=x+1
            while y<bucket_len and buckets[y] is None:
                y+=1
            if y<bucket_len:
                ret=max(ret,buckets[y][0]-buckets[x][1])
            x=y
        return ret
'''

class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<2:
            return 0
        size=len(str(max(nums)))
        for i in xrange(size):
            record=[[] for _ in xrange(10)]
            for num in nums:
                a=int(math.pow(10,i+1))
                b=a/10
                record[(num%a)/b].append(num)
            nums=[n for _ in xrange(10) for n in record[_]]
        ret=-1
        
        for i in range(0,len(nums)-1):
            ret=max(ret,nums[i+1]-nums[i])
        return ret
