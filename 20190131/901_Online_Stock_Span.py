"""
File: 901_Online_Stock_Span.py
Date: 2019/02/18 20:41:51
"""
class StockSpanner(object):

    def __init__(self):
        self.days = 0
        self.stack = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        self.days += 1
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
   
        if self.stack:
            ret = self.days - self.stack[-1][1]
        else:
            ret = self.days
        self.stack.append((price, self.days))
        return ret           


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

