"""
File: 893_Groups_of_Special-Equivalent_Strings.py
Date: 2019/02/20 18:42:15
"""
class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        return len(set([''.join(sorted(a[::2])) + ''.join(sorted(a[::-1])) for a in A]))
