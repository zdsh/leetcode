"""
File: 754_Reach_a_Number.py
Date: 2019/03/20 20:16:54
"""
class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target = abs(target)
        n = int(math.sqrt(2*target))
        s = n * (n+1) / 2
        while s < target or (s - target) % 2 :
            s += n + 1
            n += 1
        return n
