"""
File: 961_N-Repeated_Element_in_Size_2N_Array.py
Date: 2019/02/03 15:56:49
"""

class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res_dic = {}
        for a in A:
            if a in res_dic:
                return a
            else:
                res_dic[a] = 1
