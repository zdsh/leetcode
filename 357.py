class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 1
        if n==1:
            return 10
        i,cur=1,1
        val=0
        while i<n:
            cur*=(10-i)
            val+=cur
            i+=1
        val*=9
        return 10+val
            
