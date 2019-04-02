"""
File: 744_Find_Smallest_Letter_Greater_Than_Target.py
Date: 2019/04/02 19:32:21
"""
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        p =  bisect.bisect_right(letters, target)
        return letters[p] if p < len(letters) else letters[0] 
