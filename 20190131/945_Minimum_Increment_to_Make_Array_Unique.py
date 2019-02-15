"""
File: 945_Minimum_Increment_to_Make_Array_Unique.py
Date: 2019/02/15 15:28:57
"""
class Solution(object):
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ret = 0
        count_dic = {}
        for a in A:
            count_dic[a] = count_dic.get(a, 0) + 1
        keys_sort = sorted(count_dic.keys())
        i, n = 0, len(keys_sort)
        while i < n:
            a = keys_sort[i]
            if count_dic[a] > 1:
                ret += count_dic[a] - 1
                if a + 1 in count_dic:
                    count_dic[a + 1] = count_dic[a + 1] + count_dic[a] - 1
                    i += 1
                else:
                    count_dic[a + 1] = count_dic[a] - 1
                    keys_sort[i] = a + 1
            else:
                i += 1
        return ret
