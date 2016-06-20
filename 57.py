Solution for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        i=0
        while i<len(intervals):
            interval=intervals[i]
            if interval.start>=newInterval.start:
                if interval.start<=newInterval.end:
                    if interval.end>newInterval.end:
                        newInterval.end=interval.end
                    intervals.remove(interval)
                else:
                    i+=1
            else:
                if interval.end>=newInterval.start:
                    if interval.end>=newInterval.end:
                        return intervals
                    else:
                        newInterval.start=interval.start
                        intervals.remove(interval)
                else:
                    i+=1
        intervals.append(newInterval)
        return sorted(intervals,key=lambda x:x.start)
