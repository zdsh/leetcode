"""
File: 731_My_Calendar_II.py
Date: 2019/04/06 20:22:54
"""
class MyCalendarTwo(object):

    def __init__(self):
        self.used = []
        self.used2 = [] 

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        ps = bisect.bisect_right(self.used2, start)
        pe = bisect.bisect_left(self.used2, end)
        if ps % 2 or pe % 2 or ps != pe:
            return False
        ps = bisect.bisect_right(self.used, start)
        pe = bisect.bisect_left(self.used, end)
        if ps == pe and ps % 2 == 0:
            bisect.insort(self.used, start)
            bisect.insort(self.used, end)
        else:
            for i in range(ps - (ps % 2 == 1), pe + (pe % 2 == 1), 2):
                bisect.insort(self.used2, max(self.used[i], start))
                bisect.insort(self.used2, min(self.used[i+1], end))
            if ps % 2 == 0:
                self.used[ps] = start
            if pe % 2 == 0:
                self.used[pe-1] = end
            for i in range(ps + (ps % 2 == 0), pe - (pe % 2 == 0)):
                self.used.pop(ps + (ps % 2 == 0))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)

