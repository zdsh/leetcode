class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num==0:
            res=[0]
        elif num==1:
            res=[0,1]
        else:
            res=[0,1]
            n=len(res)
            while num+1>n:
                i=0
                while i<n and n+i<=num:
                    res.append(res[i]+1)
                    i+=1
                n=len(res)
        return res
                
