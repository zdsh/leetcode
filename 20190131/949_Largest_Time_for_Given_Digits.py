"""
File: 949_Largest_Time_for_Given_Digits.py
Date: 2019/02/14 20:46:06
"""
class Solution(object):
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        def check(hour, minute):
            if hour >= 24:
                return False
            if minute >= 60:
                return False
            return True
        ret = []
        for h1, h2, m1, m2 in itertools.permutations(A):
            hour = h1 * 10 + h2
            minute = m1 * 10 + m2
            if check(hour, minute):
                if len(ret) <= 0:
                    max_time = hour * 60 + minute
                    ret = [h1, h2, m1, m2]
                elif hour * 60 + minute  > max_time:
                    max_time = hour * 60 + minute
                    ret = [h1, h2, m1, m2]
        if len(ret) <= 0:
            return ''
        return str(ret[0]) + str(ret[1]) + ':' + str(ret[2]) + str(ret[3])        
