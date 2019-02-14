"""
File: 953_Verifying_an_Alien_Dictionary.py
Date: 2019/02/14 20:12:12
"""
class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        n = len(words)
        if n <= 1:
            return True

        order_dic = {}
        for m, o in enumerate(order):
            order_dic[o] = m

        for i in range(0, n - 1):
            k = 0
            while k < len(words[i]) and k < len(words[i+1]):
                 if order_dic[words[i][k]] > order_dic[words[i+1][k]]:
                     return False
                 if order_dic[words[i][k]] < order_dic[words[i+1][k]]:
                     break
                 k += 1
            if k == len(words[i+1]) and len(words[i]) > len(words[i+1]):
                return False

        return True        
