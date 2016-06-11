class FenwickTree(object):
    def __init__(self,n):
        self.n=n
        self.sums=[0]*(n+1)
        
    def add(self,x,val):
        #print(self.sums)
        while x<=self.n:
            self.sums[x]+=val
            x+=self.lowbit(x)
        #print(self.sums)
    
    def lowbit(self,x):
        return x&(-x)
        
    def sum(self,x):
        ret=0
        while x>0:
            ret+=self.sums[x]
            x-=self.lowbit(x)
        return ret

class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        sums=nums[:]
        #print(sums)
        for i in range(1,len(sums)):
            sums[i]+=sums[i-1]
        sorted_sums=sorted(set(sums))
        #print(sums)
        #print(sorted_sums)
        
        tree=FenwickTree(len(sorted_sums))
        import bisect
        ret=0
        for s in sums:
            left=bisect.bisect_left(sorted_sums,s-upper)
            right=bisect.bisect_right(sorted_sums,s-lower)
            #print('left,right',left,right)
            ret+=tree.sum(right) - tree.sum(left)
            if s>=lower and s<=upper:
                ret+=1
            #print('add position',bisect.bisect_right(sorted_sums,s))
            tree.add(bisect.bisect_right(sorted_sums,s),1)
        return ret
            
