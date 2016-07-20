class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        n=len(s)
        if n<=0:
            return 0
            
        res=[[False for _ in range(n)]for _ in range(n)]
        
        for i in range(0,n):
            res[i][i]=True
            
        for i in range(1,n):
            for j in range(0,n-i):
                res[j][j+i]
                if i>1:
                    if res[j+1][j+i-1]==True:
                        if s[j]==s[j+i]:
                            res[j][j+i]=True
                else:
                    if s[j]==s[j+i]:
                        res[j][j+i]=True
    
        cnt=[ i for i in range(0,n)]
        for i in range(0,n):
            if res[0][i]:
                cnt[i]=0
            else:
                for j in range(0,i):
                    if res[j+1][i]:
                        cnt[i]=min(cnt[i],cnt[j]+1)
        return cnt[n-1]
 
