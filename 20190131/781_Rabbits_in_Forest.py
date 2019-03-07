"""
File: 781_Rabbits_in_Forest.py
Date: 2019/03/07 11:15:47
"""
class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        ret, res = 0, {}
        for answer in answers:
            if answer not in res or res[answer] == 0:
                ret += answer + 1
                res[answer] = answer
            else:
                res[answer] -= 1
        return ret

              
