class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m=len(dungeon)
        if m<=0:
            return 0
        n=len(dungeon[0])
        res=[0]*(n+1)
        res[n]=1
        for i in range(n-1,-1,-1):
            v=dungeon[m-1][i]-res[i+1]
            res[i]=1 if v>=0 else -v
            
        for j in range(m-2,-1,-1):
            v=dungeon[j][n-1]-res[n-1]
            res[n-1]=1 if v>=0 else -v
            for i in range(n-2,-1,-1):
                v=dungeon[j][i]-min(res[i+1],res[i])
                res[i]= 1 if v>=0 else -v
        return res[0]

