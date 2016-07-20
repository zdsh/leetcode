class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        
        n=len(s)
        if n<=0:
            return [[]]
        res=[[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
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
                        
        def solve(s,i,j):
            ret=[]
            if res[i][j]:
                ret.append([s[i:j+1]])
            for k in range(i,j):
                if res[i][k]:
                    for v in solve(s,k+1,j):
                        nv=[s[i:k+1]]+v
                        ret.append(nv)
            return ret
        return solve(s,0,n-1)

