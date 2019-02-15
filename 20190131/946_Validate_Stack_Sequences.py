"""
File: 946_Validate_Stack_Sequences.py
Date: 2019/02/15 14:57:40
"""
class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        i, j, n = 0, 0, len(pushed)
        while i < n:
            stack.append(pushed[i])
            i += 1
            while stack and j < n and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        if i == n and j == n and len(stack) == 0:
            return True
        return False
