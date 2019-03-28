"""
File: 746_Min_Cost_Climbing_Stairs.py
Date: 2019/03/28 11:04:00
"""
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cur_cost, next_cost = cost[-2], cost[-1]
        for v in cost[::-1][2:]:
            cost = min(cur_cost, next_cost) + v
            next_cost, cur_cost = cur_cost, cost 
        return min(cur_cost, next_cost)
