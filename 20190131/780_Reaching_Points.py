"""
File: 780_Reaching_Points.py
Date: 2019/03/07 11:22:33
"""
class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        if sx > tx or sy > ty:
            return False
        if sx == tx and (ty - sy) % sx == 0:
            return True
        if sy == ty and (tx - sx) % sy == 0:
            return True

        if tx > ty:
            return self.reachingPoints(sx, sy, tx % ty, ty)
        else:
            return self.reachingPoints(sx, sy, tx, ty % tx)

if __name__ == '__main__':
    solution = Solution()
    print solution.reachingPoints(35,
13,
455955547,
420098884)
