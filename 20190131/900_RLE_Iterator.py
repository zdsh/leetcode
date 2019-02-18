"""
File: 900_RLE_Iterator.py
Date: 2019/02/18 20:09:51
"""
class RLEIterator(object):

    def __init__(self, A):
        """
        :type A: List[int]
        """
        self.values = []
        self.num = []
        self.all_num = 0
        for i in range(len(A) / 2):
            if A[2 * i] != 0:
                self.num.append(A[2 * i])
                self.values.append(A[2 * i + 1])
                self.all_num += A[2 * i]        

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n > self.all_num:
            self.all_num = 0
            return -1
        
        while self.num[0] < n:
            self.all_num -= self.num[0]
            n -= self.num[0]
            del self.num[0]
            del self.values[0]
        self.all_num -= n
        self.num[0] -= n
        return self.values[0]        


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)
