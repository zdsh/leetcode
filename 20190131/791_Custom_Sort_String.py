"""
File: 791_Custom_Sort_String.py
Date: 2019/03/14 12:53:22
"""
class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        letter_dic = collections.defaultdict(int)
        for t in T:
            letter_dic[t] += 1
        ret = ''
        for s in S:
            ret += s * letter_dic[s]
        ret += ''.join([t * letter_dic[t] for t in letter_dic if t not in S])
        return ret
