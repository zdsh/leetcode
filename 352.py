# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.begin=[]
        self.end=[]

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        n=len(self.begin)
        if n==0:
            self.begin.append(val)
            self.end.append(val)
        elif val<self.begin[0]:
            if val==self.begin[0]-1:
                self.begin[0]=val
            else:
                self.begin=[val]+self.begin
                self.end=[val]+self.end
        elif val>self.end[-1]:
            if val==self.end[-1]+1:
                self.end[-1]=val
            else:
                self.begin=self.begin+[val]
                self.end=self.end+[val]
        else:
            l,h=0,n-1
            while l<=h:
                m=(l+h)/2
                if self.begin[m]>val:
                    h=m-1
                elif self.begin[m]<val:
                    l=m+1
                else:
                    return
            begin=h
            
            l,h=0,n-1
            while l<=h:
                m=(l+h)/2
                if self.end[m]>val:
                    h=m-1
                elif self.end[m]<val:
                    l=m+1
                else:
                    return
            end=l
        
            if begin!=end:
                if self.end[begin]==val-1 and self.begin[end]==val+1:
                    self.begin=self.begin[0:begin+1]+self.begin[end+1:]
                    self.end=self.end[0:begin]+self.end[end:]
                elif self.end[begin]==val-1:
                    self.end[begin]=val
                elif self.begin[end]==val+1:
                    self.begin[end]=val
                else:
                    self.begin=self.begin[0:begin+1]+[val]+self.begin[end:]
                    self.end=self.end[0:begin+1]+[val]+self.end[end:]

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        return [[self.begin[i],self.end[i]] for i in range(len(self.begin))]
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()