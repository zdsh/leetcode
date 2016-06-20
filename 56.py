Solution for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        ret=[]
        intervals=sorted(intervals,key=lambda x:x.start)
        i=0
        pre=None
        while i<len(intervals):
            if pre==None:
                pre=intervals[i]
            else:
                if pre.end<intervals[i].start:
                    ret.append(pre)
                    pre=intervals[i]
                elif pre.end>=intervals[i].start and pre.end<intervals[i].end:
                    pre=Interval(pre.start,intervals[i].end)
                else:
                    pass
            i+=1
        if pre!=None:
            ret.append(pre)
        return ret
        
