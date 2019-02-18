"""
File: 898_Bitwise_ORs_of_Subarrays.py
Date: 2019/02/18 19:05:24
"""
class Solution(object):
    def subarrayBitwiseORs(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        pre_res, res = set(), set()
        for a in A:
            cur_res = set([a])
            for k in pre_res:
                 cur_res.add(a | k)
            res |= cur_res
            pre_res = cur_res
        return len(res)       
