"""
File: 954_Array_of_Doubled_Pairs.py
Date: 2019/02/16 19:32:03
"""
class Solution(object):
    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        counter_dic = {}
        for a in A:
            counter_dic[a] = counter_dic.get(a, 0) + 1

        s = 0
        for a in sorted(counter_dic.keys()):
             if a * 2 in counter_dic and counter_dic[a * 2] > 0:
                 n = min(counter_dic[a], counter_dic[a * 2])
                 if a == 0:
                     n = n / 2
                 counter_dic[a * 2] -= n
                 counter_dic[a] -= n
                 s += n
        
        return s >= len(A) / 2  
