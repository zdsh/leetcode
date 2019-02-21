"""
File: 855_Exam_Room.py
Date: 2019/02/21 14:03:01
"""
class ExamRoom(object):

    def __init__(self, N):
        """
        :type N: int
        """
        self.N = N
        self.seats = []

    def seat(self):
        """
        :rtype: int
        """
        if len(self.seats) == 0:
             res = 0
        else:
            d, res = self.seats[0], 0
            for i in range(1, len(self.seats)):
                if (self.seats[i] - self.seats[i - 1]) / 2 > d:
                    d = (self.seats[i] - self.seats[i - 1]) / 2
                    res = (self.seats[i] + self.seats[i - 1]) / 2
            if self.N - 1 - self.seats[-1] > d:
                res = self.N - 1
        bisect.insort(self.seats, res)
        return res 

    def leave(self, p):
        """
        :type p: int
        :rtype: void
        """
        self.seats.remove(p)        


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)
