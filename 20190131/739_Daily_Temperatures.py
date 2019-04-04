"""
File: 739_Daily_Temperatures.py
Date: 2019/04/04 14:20:11
"""
class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        n = len(T)
        ret, stack = [0] * n, []
        for id, t in enumerate(T):
            while len(stack) > 0 and stack[-1][1] < t:
                ret[stack[-1][0]] = id - stack[-1][0]
                stack.pop()
            stack.append((id, t))
        return ret        
