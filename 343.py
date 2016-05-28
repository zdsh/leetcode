class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==2:
            res=1
        elif n==3:
            res=2
        else:
            t=n/3
            import math
            if n%3==0:
                res=math.pow(3,t)
            elif n%3==1:
                res=math.pow(3,t-1)*4
            elif n%3==2:
                res=math.pow(3,t)*2
        return int(res)
                
        
