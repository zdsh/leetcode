"""
File: 764_Largest_Plus_Sign.py
Date: 2019/02/27 10:51:23
"""
class Solution(object):
    def orderOfLargestPlusSign(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        res = 0
        mines_set = set()
        for mine in mines:
            mines_set.add(tuple(mine))

        for r in range(0, N):
            for c in range(0, N):
                if (r, c) in mines_set:
                    continue
                if r < res or N - 1 - r < res or c < res or N - 1 - c < res:
                    continue
                k = 0
                while r >= k and r + k < N and c >= k and c + k < N and \
                    (r - k, c) not in mines_set and (r + k, c) not in mines_set and \
                    (r, c - k) not in mines_set and (r, c + k) not in mines_set:
                    k += 1
                res = max(res, k)
        return res 
