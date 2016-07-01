class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        i,j,m,n=0,0,len(s),len(p)
        res=None
        back=None
        while i<m:
            if j<n and (p[j]=='?' or s[i]==p[j]):
                i+=1
                j+=1
            elif j<n and p[j]=='*':
                res,back=j,i
                j+=1
            elif res!=None:
                j=res+1
                back+=1
                i=back
            else:
                return False
        while j<n and p[j]=='*':
            j+=1
        return j==n
        
