class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        n=len(nums)
        self.nums=nums
        self.sums=[0]*(n+1)
        for i in range(0,n):
            j=i+1
            while j<=n:
                self.sums[j]+=self.nums[i]
                j+=j&(-j)
	print self.sums
                
    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        c=val-self.nums[i]
        self.nums[i]=val
        n=len(self.nums)
        j=i+1
        while j<=n:
            self.sums[j]+=c
            j+=j&(-j)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        b=0
        k=j+1
        while k>0:
            b+=self.sums[k]
            k-=k&(-k)
        a=0
        k=i
        while k>0:
            a+=self.sums[k]
            k-=k&(-k)
        return b-a
        
        


# Your NumArray object will be instantiated and called as such:
nums=[1,3,5]
numArray = NumArray(nums)
numArray.sumRange(0, 1)
numArray.update(1, 10)
numArray.sumRange(1, 2)
