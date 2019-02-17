"""
File: 935_Knight_Dialer.py
Date: 2019/02/17 12:30:49
"""
class Solution(object):
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        poses = [[4, 6], [6, 8], [7, 9], [4, 8], [0, 3, 9], [], [0, 1, 7], [2, 6], [1, 3], [2, 4]]

        if N == 1:
            return 10
        pre_loc = [1] * 10
        for i in range(2, N + 1):
            cur_loc = [0] * 10
            for j in xrange(10):
                for k in poses[j]:
                    cur_loc[k] += pre_loc[j]
            pre_loc = cur_loc
        return sum(pre_loc) % (10**9 + 7)        
