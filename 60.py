class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def solve(res,k):
            if k==1:
                return res
            size=len(res)
            i=2
            import math
            while k>=math.factorial(i):
                i+=1
            t=i
            res=res[0:size-(i-1)]+res[size-(i-1):][::-1]
            if k-math.factorial(t-1)==0:
                return res
            i=size-1
            while i>0 and res[i-1]>res[i]:
                i-=1
            j=size-1
            while res[j]<res[i-1]:
                j-=1
            res[i-1],res[j]=res[j],res[i-1]
            res=res[0:i]+res[i:][::-1]
            return solve(res,k-math.factorial(t-1))
            
        
        res=[i+1 for i in range(0,n)]
        ret=solve(res,k)
        return ''.join([str(i) for i in ret])
