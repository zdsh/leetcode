"""
File: 856_Score_of_Parentheses.py
Date: 2019/02/21 15:15:13
"""
class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        for s in S:
            if s == '(':
                stack.append('(')
            if s == ')':
                if stack[-1] == '(':
                    stack[-1] = 1
                else:
                    res = 0
                    while stack[-1] != '(':
                       res += stack.pop()
                    stack[-1] = 2 * res
        return sum(stack)  
