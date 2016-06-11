from heapq import *

class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.heaps=[],[]
        #self.nums=[]
        
    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        large,small=self.heaps
        heappush(small, -heappushpop(large,num))
        if len(large)<len(small):
            heappush(large, -heappop(small))
        '''
        import bisect
        bisect.insort_left(self.nums,num)
        '''
        
    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        large,small=self.heaps
        if len(large)>len(small):
            return float(large[0])
        return (large[0]-small[0])/2.0
        
        '''
        size=len(self.nums)
        if size%2==0:
            return (self.nums[size/2-1]+self.nums[size/2])/2.0
        else:
            return self.nums[size/2] 
        '''
# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()
