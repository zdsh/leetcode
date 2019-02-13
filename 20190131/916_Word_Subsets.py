"""
File: 916_Word_Subsets.py
Date: 2019/02/13 16:04:33
"""
class Solution(object):
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        def count_letter(word):
            num_list = [0] * 26
            for letter in word:
                num_list[ord(letter) - ord('a')] += 1
            return num_list

        ret = []
        max_count = [0] * 26
        for b in B:
            num_list = count_letter(b)
            for i in range(0, 26):
                max_count[i] = max(max_count[i], num_list[i])

        for a in A:
            if all(x >= y for x, y in zip(count_letter(a), max_count)):
                ret.append(a)
        return ret
