class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m,n=len(s),len(t)
        if m<n:
            return 0
        res=[ [0]*(m+1) for _ in range(n+1)]
        res[0]=[1]*(m+1)
        for i in range(n):
            for j in range(m):
                if t[i]==s[j]:
                    res[i+1][j+1]=res[i][j]+res[i+1][j]
                else:
                    res[i+1][j+1]=res[i+1][j]
        return res[n][m]
