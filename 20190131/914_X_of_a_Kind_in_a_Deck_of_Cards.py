"""
File: 914_X_of_a_Kind_in_a_Deck_of_Cards.py
Date: 2019/02/13 15:27:54
"""
class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        if len(deck) <= 1:
            return 0
        count = {}
        for v in deck:
            count[v] = count.get(v, 0) + 1
        count_list = [count[v] for v in count]
        min_count = min(count_list)
        for n in range(2, min_count + 1):
            i = 0
            while i < len(count_list):
                if count_list[i] % n != 0:
                    break
                i += 1
            if i == len(count_list):
                return True
        return False
            
                 
