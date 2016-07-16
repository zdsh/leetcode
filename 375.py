class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        res=[ [0 for __ in range(n+2) ] for _ in range(n+2)]
        
        for i in range(1,n):
            for j in range(1,n+1-i):
                res[j][j+i]=min( [max(res[j][k-1],res[k+1][j+i])+k for k in range(j,j+i+1) ])
        return res[1][n]

