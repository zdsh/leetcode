"""
File: 860_Lemonade_Change.py
Date: 2019/02/21 21:20:48
"""
class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        n5, n10 = 0, 0
        for bill in bills:
            if bill == 5:
                n5 += 1
            if bill == 10:
                if n5 <= 0:
                    return False
                n10 += 1
                n5 -= 1
            if bill == 20:
                if n10 > 0 and n5 > 0:
                    n5 -= 1
                    n10 -= 1
                elif n5 > 3:
                    n5 -= 3
                else:
                    return False
        return True
