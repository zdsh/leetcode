"""
File: 715_Range_Module.py
Date: 2019/04/10 16:22:50
"""
class RangeModule(object):

    def __init__(self):
        self.data = []        

    def addRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: None
        """
        start = bisect.bisect_left(self.data, left)
        end = bisect.bisect_right(self.data, right)
        if start == end:
            if start % 2 == 0:
                bisect.insort(self.data, left)
                bisect.insort(self.data, right)
        else:
            if start < len(self.data):
                self.data[start] = left if start % 2 == 0 else self.data[start]                
            self.data[end-1] = right if end % 2 == 0 else self.data[end-1]
            for i in range(start + (start % 2 == 0), end - (end % 2 == 0)):
                self.data.pop(start+(start % 2 == 0))
                
    def queryRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: bool
        """
        start = bisect.bisect_right(self.data, left)
        end = bisect.bisect_left(self.data, right)
        if start % 2 == 1:
            if start == end:
                 return True
        return False      

    def removeRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: None
        """
        start = bisect.bisect_left(self.data, left)
        end = bisect.bisect_right(self.data, right)
        for i in range(start, end):
            self.data.pop(start) 
        if start % 2 == 1:
            bisect.insort(self.data, left)
        if end % 2 == 1:
            bisect.insort(self.data, right)

# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
