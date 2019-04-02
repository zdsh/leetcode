"""
File: 748_Shortest_Completing_Word.py
Date: 2019/03/28 11:31:07
"""
class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        res = collections.defaultdict(int)
        for l in licensePlate.lower():
            if l.isalpha():
                res[l] += 1
        ret = None
        for word in words:
            c = collections.Counter(word.lower())
            if all([c[k] >= res[k] for k in res]):
                ret = word if ret == None or len(word) < len(ret) else ret
        return ret
