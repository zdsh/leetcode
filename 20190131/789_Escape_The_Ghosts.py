"""
File: 789._Escape_The_Ghosts.py
Date: 2019/03/14 17:24:24
"""
class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        return False if any([abs(target[0] - ghost[0]) + abs(target[1] - ghost[1]) <= abs(target[0]) + abs(target[1]) for ghost in ghosts]) else True
