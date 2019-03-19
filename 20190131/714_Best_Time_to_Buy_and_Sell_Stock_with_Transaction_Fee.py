"""
File: 714_Best_Time_to_Buy_and_Sell_Stock_with_Transaction_Fee.py
Date: 2019/03/19 20:39:01
"""
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        n = len(prices)
        hold, sold = [0 * prices[0]] * (n + 1), [0] * (n + 1)
        hold[0], hold[1] = float('-inf'), -1 * prices[0]
        for i in range(1, n):
            hold[i+1] = max(hold[i], sold[i] - prices[i])
            sold[i+1] = max(sold[i], hold[i] + prices[i] - fee)
        return max(hold[n], sold[n])     
