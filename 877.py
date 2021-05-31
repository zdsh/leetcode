class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        n = len(piles)
        dp = []
        for i in range(0, n):
            dp.append([0] * n)
        for i in range(0, n):
            for j in range(0, n-i):
                if i == 0:
                    dp[j][j] = piles[j]
                else:
                    dp[j][j+i] = max(dp[j][j] - dp[j+1][j+i], dp[j+i][j+i] - dp[j][j+i-1])
        return dp[0][n-1] > 0        
