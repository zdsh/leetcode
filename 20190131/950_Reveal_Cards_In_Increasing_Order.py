"""
File: 950_Reveal_Cards_In_Increasing_Order.py
Date: 2019/02/15 21:26:47
"""
class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        n = len(deck)
        if n <= 1:
            return deck
        deck = sorted(deck)
        ret_right = self.deckRevealedIncreasing(deck[(n + 1)/2:])
        if n % 2 != 0:
            ret_right = [ret_right[-1]] + ret_right[0:len(ret_right)-1]

        ret = [ 0 ] * n
        for i in xrange((n + 1) / 2):
            ret[2 * i] = deck[i]
        i = 0
        while 2 * i + 1 < n:
            ret[2 * i + 1] = ret_right[i]
            i += 1
        return ret

