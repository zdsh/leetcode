"""
File: 720_Longest_Word_in_Dictionary.py
Date: 2019/03/20 10:24:42
"""
class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words_dic = {}
        for word in words:
            words_dic[word] = len(word)
        for k, v in sorted(words_dic.items(), key=lambda x:(-len(x[0]), x[0])):
            n = len(k)
            while n > 0 and k[0:n] in words_dic:
                n -= 1
            if n == 0:
                return k
        return ''
