class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        coins=[1]+[num for num in nums if num>0]+[1]
        n=len(coins)
        dp=[[0]*n for _ in range(n)]
        for k in range(2,n):
            for left in range(0,n-k):
                right=left+k
                for i in range(left+1,right):
                    dp[left][right]=max(dp[left][right],coins[left]*coins[i]*coins[right]+dp[left][i]+dp[i][right])
        return dp[0][n-1]
