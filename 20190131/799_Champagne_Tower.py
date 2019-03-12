"""
File: 799_Champagne_Tower.py
Date: 2019/03/12 10:32:16
"""
class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        def getPositive(x):
            return 0.0 if x <= 1 else x - 1
        ret = 0.0
        if poured <= 0:
            return ret
        for row in range(query_row + 1):
            if row == 0:
                cur_row = [poured]
            else:
                cur_row = [0.0] * (row + 1)
                cur_row[0], cur_row[-1] = 0.5 * getPositive(last_row[0]), 0.5 * getPositive(last_row[-1])
                for i in range(1, row):
                    cur_row[i] = 0.5 * (getPositive(last_row[i-1]) + getPositive(last_row[i]))
            last_row = cur_row
        return cur_row[query_glass] if cur_row[query_glass] <= 1 else 1
