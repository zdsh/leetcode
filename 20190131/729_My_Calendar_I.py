"""
File: 729_My_Calendar_I.py
Date: 2019/04/04 17:11:59
"""
ass MyCalendar(object):

    def __init__(self):
        self.used = [] 

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        ps = bisect.bisect_right(self.used, start)
        pe = bisect.bisect_left(self.used, end)
        if ps != pe or ps % 2 or pe % 2:
            return False
        if ps > 0 and self.used[ps-1] == start:
            self.used[ps-1] = end
        elif pe < len(self.used) and self.used[pe] == end:
            self.used[pe] = start
        else:
            bisect.insort(self.used, start)
            bisect.insort(self.used, end)
        return True

        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
