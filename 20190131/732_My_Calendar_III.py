"""
File: 732_My_Calendar_III.py
Date: 2019/04/11 14:39:50
"""
class MyCalendarThree(object):

    def __init__(self):
        self.data = collections.defaultdict(int)

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: int
        """
        self.data[start] += 1
        self.data[end] -= 1
        ret, s = 1, 0
        for k in sorted(self.data):
            s += self.data[k]
            ret = s if s > ret else ret
        return ret


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)

