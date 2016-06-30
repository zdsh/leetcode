class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m,n=len(s),len(p)
        self.res=[[] for _ in range(0,m+1) ]
        for i in range(0,m+1):
            self.res[i]=[None for _ in range(0,n+1)]
        self.res[m][n]=True
        
        def solve(s,p,x,y):
            if self.res[x][y]!=None:
                return self.res[x][y]
                
            i,j,m,n=x,y,len(s),len(p)
            
            if x==m:
                if len(p)>y+1 and p[y+1]=='*':
                    ret=solve(s,p,x,y+2)
                else:
                    ret=False
                self.res[x][y]=ret
                return self.res[x][y]
            elif y==n:
                self.res[x][y]=False
                return self.res[x][y]
            else:
                while i<m and j<n:
                    if j+1<n and p[j+1]=='*':
                        ret=False
                        ret=ret or solve(s,p,i,j+2)
                        if p[j]!='.':
                            while i<m and s[i]==p[j]:
                                ret=ret or solve(s,p,i+1,j+2)
                                i+=1
                        else:
                            while i<m:
                                ret=ret or solve(s,p,i+1,j+2)
                                i+=1
                        self.res[x][y]=ret
                        return ret
                    elif p[j]=='.' or s[i]==p[j]:
                        i+=1
                        j+=1
                    else:
                        return False
                self.res[x][y]=solve(s,p,i,j)
                return self.res[x][y]
        return solve(s,p,0,0)
        
        
