class Solution(object):
    
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        size=len(prices)
        if size<=1:
            return 0
        cooldown=[0]*size
        buy=[0]*size
        sell=[0]*size
        buy[0]=-prices[0]
        for i in xrange(1,size):
            cooldown[i]=max(cooldown[i-1],sell[i-1])
            buy[i]=max(cooldown[i-1]-prices[i],buy[i-1])
            sell[i]=buy[i-1]+prices[i]
            print(cooldown[i],buy[i],sell[i])
        return max([cooldown[size-1],buy[size-1],sell[size-1]])
