"""
File: 777_Swap_Adjacent_in_LR_String.py
Date: 2019/03/05 17:27:03
"""
class Solution(object):
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        if len(start) != len(end):
            return False
        i, n = 0, len(start)
        start, end = list(start), list(end)
        while i < n:
            if start[i] != end[i]:
                if end[i] == 'L' and start[i] == 'X':
                    j = i + 1
                    while j < n and start[j] == 'X':
                        j += 1
                    if j < n and start[j] == end[i]:
                        start[j], start[i] = start[i], end[i]
            i += 1
        i = n-1
        while i >= 0:
            if end[i] == 'R' and start[i] == 'X':
                j = i - 1
                while j >= 0 and start[j] == 'X':
                    j -= 1
                if j >= 0 and start[j] == end[i]:
                    start[j], start[i] = start[i], end[i]
            i -= 1
        return start == end
