"""
File: 905_Sort_Array_By_Parity.py
Date: 2019/02/11 10:13:43
"""
class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd_list, even_list = [], []
        for a in A:
            if a % 2 == 0:
                even_list.append(a)
            else:
                odd_list.append(a)
        return even_list + odd_list
