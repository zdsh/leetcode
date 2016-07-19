class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n=len(prices)
        if n<=0:
            return 0
        if k>n/2:
            k=n/2
        if k==n/2:
            ret=0
            for i in range(1,n):
                if prices[i]>prices[i-1]:
                    ret+=prices[i]-prices[i-1]
            return ret
        res=[[0 for _ in range(k+1)] for _ in range(n)]
        for i in range(1,k+1):
            cur=res[0][i-1]-prices[0]
            for j in range(1,n):
                res[j][i]=max(res[j-1][i],prices[j]+cur)
                cur=max(cur,res[j][i-1]-prices[j])
        return res[n-1][k]