"""
File: 921_Minimum_Add_to_Make_Parentheses_Valid.py
Date: 2019/02/13 21:12:02
"""
class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        for s in S:
            if len(stack) == 0:
                stack.append(s)
            else:
                if s == ')' and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(s)
        return len(stack)
        
